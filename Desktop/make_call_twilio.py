import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACb7b82019d8ae4c7d50c8ee1dd9faf49e']
auth_token = os.environ['9c1c409cb633d0db5510a1abd2bad27b']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+8801756843882',
                        from_='+18646572804'
                    )

print(call.sid)