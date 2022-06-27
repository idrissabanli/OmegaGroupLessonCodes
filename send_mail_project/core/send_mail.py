import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.config import EmailConfig


class SendMail(EmailConfig):

    def __init__(self, data):
        self.body = data['body']
        self.recipients = data['recipients']
        self.subtype = data['subtype']
        self.subject = data['subject']
        self.send_mail_to_recipients()
    
    def send_mail_to_recipients(self):
        for recipient in self.recipients:
            message = self.prepare_massage_send_mail(recipient)
            if testing:
                self.send_mail(message)

    def prepare_massage_send_mail(self, recipient):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.EMAIL_HOST_USER
        message["To"] = recipient
        part = MIMEText(self.body, self.subtype)

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part)
        return message
        
        
    def send_mail(self)
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.EMAIL_HOST, self.EMAIL_PORT, context=context) as server:
            server.login(self.EMAIL_HOST_USER, self.EMAIL_HOST_PASSWORD)
            server.sendmail(
                self.EMAIL_HOST_USER, recipient, message.as_string()
            )


class Test():
    @classmethod
    def setUpClass(cls)
        cls.send_mail = SendMail(data={'body': 'Body text', 
        'recipients': ['idris@gmail.com', ],  
        'subtype': 'html',
        'subject': 'Subject'})

    def test_initialize_method(self):
        self.assertEqual(self.send_mail.body, 'Body text')
        self.assertEqual(self.send_mail.body, 'Body text')

    def test_prepare_message(self):
        message = self.send_mail.prepare_massage_send_mail()
        self.assertEqual(message['body'], 'Body text')

