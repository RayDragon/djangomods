
def verify(request, min_score = 0.5):
    import requests, json
    from django.conf import settings
    a = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret':settings.SETTINGS_RECAP['RECAP3']['SECRET_KEY'], 
                    'response':request.POST.get('token')
                }
            )
    data = json.loads(a.text)
    if data['success']:
        if data['score'] >= min_score:
            return True
    return False