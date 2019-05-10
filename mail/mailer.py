def _get_dict():
        return {
            "sender_email_id": "",
            "sender_email_id_password": ""   
        }

class GMailer():

    @staticmethod
    def get_data():
        """
        Initialize an empty json file indicating the values required, if it doesn't exists else
        return tha data gathered
        """
        import json

        try:
            r = open("settings.json", "r")
            r.close()
        except FileNotFoundError:
            r = open("settings.json", "w")
            r.write(json.dumps(_get_dict()))
            r.close()
        
        r = open("settings.json", "r")
        data = json.loads(r.read())
        r.close()
        return data

    @staticmethod
    def send_mail(_from, _to, _body):
        import smtplib
        data = GMailer.get_data()
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(data['sender_email_id'], data["sender_email_id_password"]) 

        s.sendmail(_from, _to, _body) 
        s.quit()
