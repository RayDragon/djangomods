class GMailer():

    def __init__(self, email, password):
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
