# Django Heroku Apps 
Codes for small applications, for preventing we-writing whole things again

## License
I want to be popular, so if possible, make me popular 😋😅
You can do so, by mentioning e on your website or giving me a star, promoting my stuffs etc, none of these are important.

Except of that you may use this code for anything you want without my concern, all for free 

# Contents


### Mailer
Send mail through your gmail account

```
Note: You will have to setup two factor authentication and get password for app from gmail.
```
1. Usage:
    ```python
    from mail.mailer import GMailer
    GMailer.send_mail(
    "sender's email address",
    "bluedragon.ray@gmail.com", 
    "I love your codes, please tell me how can i donate you some money :)")
    
    GMailer.send_html_mail(
        ...,
        ...,
        'Body in HTML, string is required however django.shortcut.render can be also passed',
        'Body if not html i.e. in text form',
        subject=''
    )
    
    ```



