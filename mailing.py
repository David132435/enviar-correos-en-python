#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#### Variables #######
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = ''  # Correo desde el que se va a mandar
password = ''  # COntraseña de el correo desde el que se va a mandar
from_email = '' # Correo desde el que se va a mandar (otra vez)



# Configura los detalles del correo
to_email = '' # A quien va dirigido el correo
subject = '' # Asunto del correo
message = '' # Mensaje del correo


def send_email(destination, subject, message):

	# Message
	msg = MIMEMultipart()
	msg['From'] = from_email
	msg['To'] = destination
	msg['Subject'] = subject
	msg.attach(MIMEText(message, 'plain'))

	# Inicia la conexión con el servidor SMTP
	server = smtplib.SMTP(smtp_server, smtp_port)
	server.starttls()
	server.login(username, password)

	# Envía el correo
	server.sendmail(from_email, to_email, msg.as_string())

	# Cierra la conexión
	server.quit()



























