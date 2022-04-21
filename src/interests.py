from linebot.models import (
    MessageAction, URIAction, TextSendMessage, TemplateSendMessage, ButtonsTemplate
)


INTERESTS_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/interests_4D9iFN2ly.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459677025'
INTERESTS_COMMAND_TEXT = 'Get about info'


interestsActions = [
    MessageAction(
        label='About me',
        text=INTEREST_COMMAND_TEXT
    ),
    URIAction(
        label='My Website',
        uri='https://ricky-hu.com/'
    )
]


interestsTemplateMessage = TemplateSendMessage(
    alt_text='Interests template',
    template=ButtonsTemplate(
        title='My Interests',
        text='Get my interests and activities.',
        thumbnail_image_url=INTERESTS_IMAGE_URL,
        actions=interestsActions
    )
)


interestsTextMessage = TextSendMessage(text='''
Interests info
''')
