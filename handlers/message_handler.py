from database import db
from models.user import User
from datetime import datetime

def process_message(sender, message_body):
    """
    Processa mensagens recebidas do WhatsApp
    
    Args:
        sender (str): Número do telefone do remetente
        message_body (str): Corpo da mensagem
    
    Returns:
        str: Resposta do bot
    """
    
    # Criar ou atualizar usuário
    user = User.query.filter_by(phone_number=sender).first()
    if not user:
        user = User(phone_number=sender)
        db.session.add(user)
        db.session.commit()
    
    # Processar comandos
    message_lower = message_body.lower().strip()
    
    # Comando: Olá
    if message_lower in ['oi', 'ola', 'olá', 'e aí']:
        return f'Olá {user.name or "visitante"}! 👋 Como posso ajudar?'
    
    # Comando: Ajuda
    elif message_lower in ['ajuda', 'help', 'menu']:
        return (
            'Menu de Comandos:\n'
            '1. oi - Saudação\n'
            '2. hora - Ver hora atual\n'
            '3. info - Informações do bot\n'
            '4. sair - Encerrar conversa'
        )
    
    # Comando: Hora
    elif message_lower == 'hora':
        hora_atual = datetime.now().strftime('%H:%M:%S')
        return f'⏰ Hora atual: {hora_atual}'
    
    # Comando: Info
    elif message_lower == 'info':
        return (
            'WhatsApp Prime Bot v1.0\n'
            'Bot automatizado para WhatsApp\n'
            'Digite "ajuda" para ver comandos'
        )
    
    # Resposta padrão
    else:
        return 'Desculpe, não entendi. Digite "ajuda" para ver os comandos disponíveis.'
