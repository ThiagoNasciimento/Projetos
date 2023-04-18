#bibliotecas
import smtplib
from email.message import EmailMessage
from segredos import senha # pylint: contendo a senha de acesso ao email

#configurar email
EMAIL = 'seuemail@outlook.com'
EMAIL_SENHA = senha

#mensagem de email
msg = EmailMessage()
msg['Subject'] = 'A Carga chegou'
msg['From'] = 'seuemail@outlook.com'
msg['To'] = 'destino1@outlook.com', 'destino2@gmail.com'
msg.set_content('mensagem')

#conectar ao server do email
with smtplib.SMTP('smtp-mail.outlook.com',587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL, EMAIL_SENHA)

    smtp.send_message(msg) #enviar email

