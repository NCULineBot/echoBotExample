from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *


app = Flask(__name__)


line_bot_api = LineBotApi('5mbmhhiSWG1hnpZZ7jtkb4DBpSoVFUW7QDd35Aghz5WQk/0YE8PWKK0O7gO09ux5nUrnO5Yk3Tg2PLrwDYfm2FxQr5u4ld9TlyPqTRNktEauald/IPc/WJRIEe3oY6vaxKEutB9pQ50/Ch/Wkq+uaAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fdaddde4261e3c297530bd0325de9186')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(msg)
    msg = msg.encode('utf-8')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=msg))

if __name__ == "__main__":
    app.run(debug=True,port=80)
