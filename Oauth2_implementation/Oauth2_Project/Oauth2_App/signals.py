import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_emails(sender, instance, **kwargs):
    print "instance", instance.email
    message = Mail(
        from_email='from_email@example.com',
        to_emails= str(instance.email),
        subject= "You are registered with Alok's portal",
        html_content='<strong>welcome to Alok World </strong>')
    try:
        sg = SendGridAPIClient('add your sendgrid key generaterd by you from sendgrid console')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
