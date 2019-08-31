class GMailer():

    def __init__(self, email='#', password='#'):
        if email =='#':
            # picking from settings.py
            from django.conf import settings
            mailer_setting = settings.SETTINGS_DJANGOMODS['MAILER']
            email, password = mailer_setting['EMAIL_ID'], mailer_setting['EMAIL_PASSWORD']
    
        self.data = {
            "email_id": email,
            "password": password   
        }
   
    def send_mail(self, _from, _to, _body):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(self.data['email_id'], self.data["password"]) 
        s.sendmail(_from, _to, _body) 
        s.quit()

    def send_html_mail(self, _from, _to, _body, _body_text, _subject=""):
        if type(_body) != type('asd'):
            _body = str(_body._container[0], 'utf-8')
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        try:
            part1 = MIMEText(_body_text, 'plain')
            part2 = MIMEText(_body, 'html')

            message = MIMEMultipart('alternative')
            message['Subject'] = _subject
            message['From'] = _from
            message['To'] = _to
            message.attach(part1)
            message.attach(part2)

            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login(self.data['email_id'], self.data["password"]) 
            s.sendmail(_from, _to, message.as_string()) 
            s.quit()
            return True
        except Exception as e:
            return False, e