from linebot.models import (
    MessageAction, URIAction, TextSendMessage, TemplateSendMessage, ButtonsTemplate
)


CONTACT_COMMAND_TEXT = 'Get contact info'
CONTACT_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/contact_rc3Yhe5QY.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650468251959'


contactActions = [
    MessageAction(
        label='Contact me',
        text=CONTACT_IMAGE_URL
    ),
    URIAction(
        label='My Website',
        uri='https://ricky-hu.com/'
    )
]


contactTemplateMessage = TemplateSendMessage(
    alt_text='Interests template',
    template=ButtonsTemplate(
        title='My Interests',
        text='Get my interests and activities.',
        thumbnail_image_url=CONTACT_IMAGE_URL,
        actions=contactActions
    )
)


contactTextMessage = TextSendMessage(text='''
Contact info
''')
