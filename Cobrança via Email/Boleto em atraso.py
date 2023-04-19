import smtplib
import mysql.connector
from datetime import datetime, timedelta

# Conectar ao banco de dados MySQL
db = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="sua_base_de_dados"
)

# Definir a data de hoje e a data limite para o pagamento
hoje = datetime.today()
limite_pagamento = hoje - timedelta(days=7)  # 7 dias de atraso

# Selecionar os alunos que estão com o pagamento atrasado
cursor = db.cursor()
cursor.execute(f"SELECT nome, email FROM alunos WHERE data_pagamento < '{limite_pagamento}'")

# Enviar um e-mail para cada aluno selecionado
for nome, email in cursor.fetchall():
    remetente = 'seuemail@outlook.com'
    senha = 'sua_senha'
    destinatario = email
    assunto = 'Atraso de boleto'
    mensagem = f'Olá {nome},\n\nO seu pagamento está atrasado. Por favor, regularize a situação o mais breve possível.\n\nAtenciosamente,\n'
    
    # Configurar o servidor SMTP do Outlook
    server = smtplib.SMTP('smtp-mail.outlook.com',587)
    server.starttls()
    server.login(remetente, senha)
    
    # Enviar o e-mail
    server.sendmail(remetente, destinatario, f'Subject: {assunto}\n\n{mensagem}')
    
    # Fechar a conexão com o servidor SMTP
    server.quit()
