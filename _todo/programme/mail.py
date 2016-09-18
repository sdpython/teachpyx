import smtplib
from email.MIMEMultipart    import MIMEMultipart
from email.MIMEBase         import MIMEBase
from email.MIMEText         import MIMEText
from email.Utils            import formatdate
from email                  import Encoders
import os

def envoyer_mail (aqui, sujet, contenu, files = []):
    de              = "email de l'auteur"
    msg             = MIMEMultipart()
    msg ['From']    = de
    msg ['To']      = aqui
    msg ['Date']    = formatdate (localtime = True)
    msg ['Subject'] = sujet

    msg.attach(  MIMEText (contenu) )
    for file in files:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload ( open(file,'rb').read () )
        Encoders.encode_base64 (part)
        part.add_header ('Content-Disposition',  \
                         'attachment; filename="%s"' % os.path.basename (file))
        msg.attach (part)

    smtp = smtplib.SMTP ("smtp.gmail.com", 587)
    smtp.ehlo ()
    smtp.starttls ()
    smtp.ehlo ()
    smtp.login ("login", "mot_de_passe")

    smtp.sendmail (de, aqui, msg.as_string () )
    smtp.close()
    
envoyer_mail ( "destinataire", "sujet","contenu", ["mail.py"] )