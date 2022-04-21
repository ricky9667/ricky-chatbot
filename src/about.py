from linebot.models import (
    MessageAction, URIAction, TextSendMessage, TemplateSendMessage, ButtonsTemplate
)


ABOUT_COMMAND_TEXT = 'Get about info'
ABOUT_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/about_yPYPVDqsg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459693293'


aboutActions = [
    MessageAction(
        label='About me',
        text=ABOUT_COMMAND_TEXT
    ),
    URIAction(
        label='My Website',
        uri='https://ricky-hu.com/'
    )
]


aboutTemplateMessage = TemplateSendMessage(
    alt_text='About template',
    template=ButtonsTemplate(
        title='About Me',
        text='Get my basic introduction.',
        thumbnail_image_url=ABOUT_IMAGE_URL,
        actions=aboutActions
    )
)


aboutTextMessage = TextSendMessage(text='''
I am a undergraduate student from Taipei Tech, studying Computer Science and Information Engineering. 
I am passionate about learning new skills in programming, and enjoy particiating in activities and meet new people.
I also have interest in Rubik's cube and table tennis.
''')
