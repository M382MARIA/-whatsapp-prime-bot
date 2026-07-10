from flask import Flask, request, jsonify
from twilio.rest import Client
from config import config
from database import db, init_db
from handlers import process_message
from utils import sanitize_phone_number
import os

# Inicializar Flask
app = Flask(__name__)

# Carregar configurações
config_name = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Inicializar banco de dados
init_db(app)

# Inicializar Twilio
client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])

@app.route('/', methods=['GET'])
def index():
    """Página inicial"""
    return jsonify({
        'status': 'running',
        'message': 'WhatsApp Prime Bot está online! 🤖',
        'version': '1.0.0'
    }), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook para receber mensagens do WhatsApp via Twilio
    """
    try:
        # Extrair dados da mensagem
        incoming_msg = request.values.get('Body', '').strip()
        sender_phone = request.values.get('From', '').strip()
        
        if not incoming_msg or not sender_phone:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Processar mensagem
        bot_response = process_message(sender_phone, incoming_msg)
        
        # Enviar resposta via Twilio
        send_whatsapp_message(sender_phone, bot_response)
        
        # Log
        from utils.helpers import log_message
        log_message(sender_phone, incoming_msg, bot_response)
        
        return jsonify({'status': 'success'}), 200
        
    except Exception as e:
        print(f'❌ Erro no webhook: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/send', methods=['POST'])
def send_message():
    """
    Endpoint para enviar mensagens manualmente
    """
    try:
        data = request.get_json()
        phone = data.get('phone')
        message = data.get('message')
        
        if not phone or not message:
            return jsonify({'error': 'Phone and message required'}), 400
        
        send_whatsapp_message(phone, message)
        
        return jsonify({
            'status': 'success',
            'message': 'Mensagem enviada com sucesso'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def send_whatsapp_message(to_phone, message_body):
    """
    Envia mensagem via WhatsApp usando Twilio
    
    Args:
        to_phone (str): Número de telefone do destinatário
        message_body (str): Corpo da mensagem
    """
    # Formatar número para Twilio
    if not to_phone.startswith('whatsapp:'):
        to_phone = f'whatsapp:{to_phone}'
    
    try:
        message = client.messages.create(
            from_=app.config['TWILIO_WHATSAPP_NUMBER'],
            body=message_body,
            to=to_phone
        )
        print(f'✅ Mensagem enviada: {message.sid}')
        return message
    except Exception as e:
        print(f'❌ Erro ao enviar mensagem: {str(e)}')
        raise

@app.route('/health', methods=['GET'])
def health_check():
    """Health check do bot"""
    return jsonify({
        'status': 'healthy',
        'service': 'WhatsApp Prime Bot'
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handler para rotas não encontradas"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para erros internos"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print('🚀 WhatsApp Prime Bot iniciando...')
    print(f'🌐 Servidor rodando em http://{app.config["HOST"]}:{app.config["PORT"]}')
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
