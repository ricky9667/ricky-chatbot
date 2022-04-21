import os
import sys
from argparse import Action, ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent
)

from overview import greetingTextMessage, carouselTemplateMessage
from src.about import aboutTemplateMessage, aboutTextMessage, ABOUT_COMMAND_TEXT
from src.skills import skillsTemplateMessage, skillsTextMessage, SKILLS_COMMAND_TEXT
from src.interests import interestsTemplateMessage, interestsTextMessage, INTERESTS_COMMAND_TEXT
from src.contact import contactTextMessage, contactTemplateMessage, CONTACT_COMMAND_TEXT


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if isinstance(event, FollowEvent):
            line_bot_api.reply_message(event.reply_token, greetingTextMessage)

        if isinstance(event, MessageEvent):
            if isinstance(event.message, TextMessage):
                handle_text_message(event, event.message.text)

    return 'OK'


def handle_text_message(event, message):
    if message.lower() in ['o', 'overview']:
        line_bot_api.reply_message(event.reply_token, carouselTemplateMessage)
    elif message.lower() in ['a', 'about']:
        line_bot_api.reply_message(event.reply_token, aboutTemplateMessage)
    elif message.lower() in ['s', 'skills']:
        line_bot_api.reply_message(event.reply_token, skillsTemplateMessage)
    elif message.lower() in ['i', 'interests']:
        line_bot_api.reply_message(event.reply_token, interestsTemplateMessage)
    elif message.lower() in ['c', 'contact']:
        line_bot_api.reply_message(event.reply_token, contactTextMessage)
    elif message.lower() in ['h', 'help']:
        line_bot_api.reply_message(event.reply_token, greetingTextMessage)
    elif message == ABOUT_COMMAND_TEXT:
        line_bot_api.reply_message(event.reply_token, aboutTextMessage)
    elif message == SKILLS_COMMAND_TEXT:
        line_bot_api.reply_message(event.reply_token, skillsTextMessage)
    elif message == INTERESTS_COMMAND_TEXT:
        line_bot_api.reply_message(event.reply_token, interestsTextMessage)
    elif message == CONTACT_COMMAND_TEXT:
        line_bot_api.reply_message(event.reply_token, contactTextMessage)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='You said ' + event.message.text + '!'))


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
