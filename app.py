from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('a3TkYbqReZf76zVjRGABT5JRxCRYhqce54rWGj9kYERH4vDsqOOaFIhaq0JMmjfoAvfUjUPTIJcUy/7lRHr7LM8ta4OgL3Fg1ZP0I00tkSKU6rXwM+l2bS8CSYv4W0vUUFqeSAvqkNYxH6IrdhEwxgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e2b7c41930af4139a5e5088b70513fd5')


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
    msg = event.message.tex
    r = '我聽不懂你在說什麼?'

    if msg in ['hi', 'Hi', '嗨']:
        r = 'hi 你好唷唷唷~~~  我是 cathy 機器人  你可以問我cathy今天過得好不好 , 或是David今天在幹嘛而已!'
    
    elif msg in ['cathy今天過的好不好']:
        r = '她把機器人寫出來了'

    elif msg in ['David今天在']:
        r = '他一直在睡覺! 想看他怎樣睡覺的話 可以打  想看'

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


#     if '想看' in msg:
#         sticker_message = StickerSendMessage(
#         package_id='1',
#         sticker_id='1'
# )

#         line_bot_api.reply_message(
#         event.reply_token,
#         sticker_message)
    
#         return

if __name__ == "__main__":
    app.run()