import requests
from flask import Flask, Response, request
from bot_parser import parse_message

app = Flask(__name__)

TOKEN = '1023120359:AAHSXx5ayrjLbJRehpozKJSECOBV4ZQNTzI'

@app.route('/sanity')
def sanity():
    return "Server is running YAZAN ;)"


def establish_connection():
    TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://1e22489e.ngrok.io/message'.format(TOKEN)
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    req = request.get_json()
    try:
        message = req['message']['text']

        response = parse_message(message)

        chat_id = req['message']['chat']['id']
        res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                           .format(TOKEN, chat_id, response))
        return Response("success")
    except:
        return Response("Error")

if __name__ == '__main__':
    establish_connection()
    app.run(port=5002)
