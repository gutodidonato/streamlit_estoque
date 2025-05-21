import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obter credenciais do .env
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

def enviar_mensagem(mensagem_texto: str,
                    sender: str,
                    assunto: str,
                    senha_pass_sv: str,
                    destinatario: str) -> bool | None:
    try:
        print("Iniciando Envio...")
        print(f"Destinatário: {destinatario}")

        # Criar o e-mail
        mensagem = EmailMessage()
        mensagem.set_content(mensagem_texto)
        mensagem["Subject"] = assunto
        mensagem["From"] = sender
        mensagem["To"] = destinatario

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, senha_pass_sv)
            server.send_message(mensagem)

        print("E-mail enviado com sucesso!")
        return True

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
