from linebot.models import (
    MessageAction, URIAction, TextSendMessage, TemplateSendMessage, ButtonsTemplate
)


SKILLS_COMMAND_TEXT = 'Get skills info'
SKILLS_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/skills_SwsAapQcEg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459707045'


skillsActions = [
    MessageAction(
        label='My skills',
        text=SKILLS_COMMAND_TEXT
    ),
    URIAction(
        label='My Projects',
        uri='https://github.com/ricky9667'
    )
]


skillsTemplateMessage = TemplateSendMessage(
    alt_text='Skills template',
    template=ButtonsTemplate(
        title='My Skills',
        text='Get my skills in programming and my projects.',
        thumbnail_image_url=SKILLS_IMAGE_URL,
        actions=skillsActions
    )
)


skillsTextMessage = TextSendMessage(text='''
Skills info
''')
