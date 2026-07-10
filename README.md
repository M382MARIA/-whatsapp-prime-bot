# WhatsApp Prime Bot 🤖

Bot automatizado para WhatsApp usando Flask e Python.

## 📋 Requisitos

- Python 3.8+
- Flask
- Twilio (para integração WhatsApp)
- SQLAlchemy (banco de dados)
- python-dotenv

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/M382MARIA/-whatsapp-prime-bot.git
cd -whatsapp-prime-bot
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env`:
```bash
cp .env.example .env
```

5. Execute o bot:
```bash
python app.py
```

## 📚 Estrutura do Projeto

```
-whatsapp-prime-bot/
├── app.py                 # Arquivo principal da aplicação
├── config.py              # Configurações
├── requirements.txt       # Dependências
├── .env.example           # Variáveis de ambiente (exemplo)
├── .gitignore             # Arquivos a ignorar
├── database.py            # Configuração do banco de dados
├── handlers/
│   ├── __init__.py
│   └── message_handler.py # Processamento de mensagens
├── models/
│   ├── __init__.py
│   └── user.py            # Modelo de usuário
└── utils/
    ├── __init__.py
    └── helpers.py         # Funções auxiliares
```

## 🔧 Configuração

### Twilio Setup

1. Crie uma conta em [Twilio](https://www.twilio.com/)
2. Obtenha suas credenciais (Account SID, Auth Token)
3. Configure um número WhatsApp
4. Configure o webhook para: `http://seu-dominio.com/webhook`

## 📖 Uso

O bot responde automaticamente às mensagens recebidas no WhatsApp.

## 🛠️ Desenvolvimento

Para adicionar novos handlers, edite `handlers/message_handler.py`.

## 📝 Licença

MIT
