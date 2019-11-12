from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('D58OS0qU1VlWqew/SSXAD4IQ9NMJ2AGYTcK/2qsWSvX6AYtmClfYNA2mqfOCw65T6qR7xtw5oZ2n0AAx2lwroR2MxUVLnkdswMvJSgVorWGVYHu/ImeyG/TgmMBqVBXk73JgzQ8zZuXfCN7TcyuO+QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8588759d098d0a074029363b120a59e1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hello, 我是 Kerwin'))


if __name__ == "__main__":
    app.run()