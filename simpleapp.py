from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "secret"

ACCESS_TOKEN = "EAAFDS8txrPIBAK2ZCiphUeg6YxGKgZCxsXmr1XGuhkLVu01xiDleLZBALC74Qpr6ZAZCMWOm1s1wl2wWKAMEmJlfdJHKiXMQZCU4GOlT29Me6SFfrr6YANlbcL2BIV1Wl27QbZBl8iWvTi4tBxyxsk5uuzI21cfYQ5MdAdFFrMGLAZDZD"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message[::-1])

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
