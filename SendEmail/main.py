"""Envinado E-mails com Python"""
from dotenv import load_dotenv
import os 
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

#TODO: Caminho arquivo HTML
CAMINHO_HTML = Path(__file__).parent / 'content-email.html'


#TODO: dados do remetente e destinatário
sender = os.getenv("FROM_EMAIL", "")
recipient = os.getenv("TO_THE_EMAIL", "")


#TODO: Configurações SMTP
smtp_server = os.getenv("SMTP_SERVER", "")
smtp_port = os.getenv("SMTP_PORT", "")
smtp_username = sender
smtp_password = os.getenv("EMAIL_PASSWORD", "")


#TODO: Mensagem de texto
with CAMINHO_HTML.open('r') as file:
    text = file.read()
    format = Template(text)
    text_email = format.substitute(name="Jaime Tadeu")


#TODO: Transformar nossa mensagem em MIMEMultipart >> from, to, subject
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = "Este é o assunto do e-mail."

content_email = MIMEText(text_email, 'html', 'utf-8')  # arquivo de texto = 'plain'
mime_multipart.attach(content_email)


#TODO: Enviar o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()  # >> iniciando a conexão com o servidor SMTP "EXTENDED HELLO(ehlo)"
    server.starttls()  # >> inicia uma conexão segura
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email successfully sent.')
