import os
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("email.html").read_text())
email=EmailMessage()
email["from"]="Pasi P."
email["to"]= os.environ['email_address'] #EMAIL ADDRESS HERE
email["subject"]="hahahahahah genius I say"

email.set_content(html.substitute({"name": "Tintti"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() #encryption mechanism to ensure secure connection
    my_secret = os.environ['app_password']
    smtp.login(os.environ['email_address'], my_secret)    #EMAIL ADDRESS HERE, password is set for my own email
    smtp.send_message(email)
    print("All clear, boss!")


    
