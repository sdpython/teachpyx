import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import os


def envoyer_mail (aqui, sujet, contenu, files = []):
    de = "email de l'auteur"
    msg = MIMEMultipart()
    msg['From'] = de
    msg['To'] = aqui
    msg['Date'] = formatdate (localtime = True)
    msg['Subject'] = sujet

    msg.attach(MIMEText(contenu))
    for file in files:
        part = MIMEBase('application', 'octet-stream')
        with open(file,'rb') as f:
            content = f.read()
        part.set_payload(content)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',  \
                        f'attachment; filename="{os.path.basename(file)}"')
        msg.attach(part)

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("login", "mot_de_passe")

    smtp.sendmail(de, aqui, msg.as_string())
    smtp.close()


envoyer_mail("destinataire", "sujet","contenu", ["mail.py"])
