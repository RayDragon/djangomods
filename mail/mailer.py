class GMailer():

    def __init__(self, email, password):
        self.data = {
            "email_id": "",
            "password": ""   
        }
   
    def send_mail(self, _from, _to, _body):
        import smtplib
        data = GMailer.get_data()
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(self.data['sender_email_id'], self.data["sender_email_id_password"]) 
        s.sendmail(_from, _to, _body) 
        s.quit()
