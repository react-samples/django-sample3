import requests
  
key = 'Your Key'

def send_mail(to, subject, html):

    request_url = "https://api.mailgun.net/v3/mail.nakanoh.net/messages"
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'hello@mail.nakanoh.net',
        'to': to,
        'subject': subject,
        'html': html
    })
