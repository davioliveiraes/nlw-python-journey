import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def send_email(to_addrs, body):
   try:
      from_addr = os.getenv('EMAIL_FROM_ADDR')
      login = os.getenv('EMAIL_LOGIN')
      password = os.getenv('EMAIL_PASSWORD')

      if not from_addr or not login or not password:
         raise ValueError("Variáveis de ambiente não encontrada.")

      msg = MIMEMultipart()
      msg["from"] = "viagens_confirmar@email.com"
      msg["to"] = ', '.join(to_addrs)
      msg["Subject"] = "Confirmação de Viagem!"
      msg.attach(MIMEText(body, 'plain'))

      server = smtplib.SMTP("smtp.ethereal.email", 587)
      server.starttls()
      server.login(login, password)
      text = msg.as_string()

      for email in to_addrs:
         server.sendmail(from_addr, email, text)
      
      server.quit()
      return True
         
   except Exception as e:
      print(f"Erro ao enviar email: {e}")
      return False
