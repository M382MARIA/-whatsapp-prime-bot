import re

def sanitize_phone_number(phone):
    """
    Sanitiza número de telefone
    
    Args:
        phone (str): Número de telefone
    
    Returns:
        str: Número sanitizado
    """
    # Remove caracteres não numéricos
    clean = re.sub(r'\D', '', phone)
    return clean

def log_message(sender, message, response):
    """
    Registra mensagem em log
    
    Args:
        sender (str): Remetente
        message (str): Mensagem recebida
        response (str): Resposta enviada
    """
    timestamp = __import__('datetime').datetime.now().isoformat()
    print(f'[{timestamp}] {sender}: {message} -> BOT: {response}')
