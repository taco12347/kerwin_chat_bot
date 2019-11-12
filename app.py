from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

import msg_source as msg_src

app = Flask(__name__)

line_bot_api = LineBotApi('y6fGpVhSeIeD4GqrxuP0If8LsdBWWCVtAI6/X/RQMcMBFc7ZVWDbdGDkEys0+l616qR7xtw5oZ2n0AAx2lwroR2MxUVLnkdswMvJSgVorWEID7Q7Uq5tYkWcI3LfJImVKpmtaftMkGgjMDBAW2Qt0wdB04t89/1O/w1cDnyilFU=')
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

@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.push_message(event.source.user_id, StickerSendMessage(package_id=11539, sticker_id=52114133))
    line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Hello, 歡迎你加入 Kerwin-Bot 的好友行列\n希望你玩得開心~'))
    line_bot_api.push_message(event.source.user_id, TextSendMessage(text='點擊下方選單了解更多資訊...\n輸入 help 查詢所有指令。'))
    line_bot_api.push_message(event.source.user_id, TextSendMessage(text='使用說明：\nhttps://github.com/taco12347/kerwin_chat_bot/blob/master/README.md'))

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        profile = line_bot_api.get_profile(event.source.user_id)
        app.logger.info("display_name: " + profile.display_name)
        app.logger.info("user_id: " + profile.user_id)
        app.logger.info("picture_url: " + profile.picture_url)
        app.logger.info("status_message: " + profile.status_message)
    except LineBotApiError:
        app.logger.error("Can not get user profile.")

    for key in msg_src.responseDict.keys():
        if key in event.message.text:
            line_bot_api.reply_message(event.reply_token, msg_src.responseDict[key])
            return None

    if 'help' in event.message.text:
        message = '你可以使用的關鍵字有：'
        for key in msg_src.responseDict.keys():
            message += key + ', '
        message += 'help'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
        return None

    line_bot_api.push_message(event.source.user_id, TextSendMessage(text='我好像沒辦法理解「' + event.message.text + '」，或許換個方式問問看？'))

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # echo sticker
    app.logger.info(event.message.package_id, event.message.sticker_id)
    try:
        line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id=event.message.package_id, sticker_id=event.message.sticker_id))
    except LineBotApiError:
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text='我也想要這個貼圖>口<!!!!'))
        line_bot_api.push_message(event.source.user_id, StickerSendMessage(package_id=11539, sticker_id=52114141))

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data in msg_src.postbackDict.keys():
        for msg in msg_src.postbackDict[event.postback.data]:
            line_bot_api.push_message(event.source.user_id, msg)

if __name__ == "__main__":
    app.run()