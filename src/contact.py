from linebot.models import (
    MessageAction, URIAction, TextSendMessage, TemplateSendMessage, ButtonsTemplate
)


CONTACT_COMMAND_TEXT = 'Get contact info'
CONTACT_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/contact_rc3Yhe5QY.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650468251959'


contactActions = [
    MessageAction(
        label='Contact Me',
        text=CONTACT_IMAGE_URL
    ),
    URIAction(
        label='My Website',
        uri='https://ricky-hu.com/'
    )
]


contactTemplateMessage = TemplateSendMessage(
    alt_text='Contact',
    template=ButtonsTemplate(
        title='Contact Me',
        text='Connect to me if you are interested!',
        thumbnail_image_url=CONTACT_IMAGE_URL,
        actions=contactActions
    )
)


contactTextMessage = TextSendMessage(
    text='''Feel free to connect to me by methods below:\n
My email: ricky9667@gmail.com
My linkedin: https://www.linkedin.com/in/ricky9667/\n
Or use other platforms to contact me in my website.''')
