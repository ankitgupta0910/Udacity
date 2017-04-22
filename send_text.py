from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe3a9061e4052fee8326d2af56d27f33c"
# Your Auth Token from twilio.com/console
auth_token = "098e4d7a2e842838209047f67ccc91ca"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16692928363",
    from_="+12068666376",
    body="Hello from Python!")

print(message.sid)
