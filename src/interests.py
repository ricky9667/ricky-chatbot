from linebot.models import (
    MessageAction, URIAction, TextSendMessage, TemplateSendMessage, ButtonsTemplate
)


INTERESTS_COMMAND_TEXT = 'Get interests info'
INTERESTS_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/interests_4D9iFN2ly.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459677025'


interestsActions = [
    MessageAction(
        label='My Interests',
        text=INTERESTS_COMMAND_TEXT
    ),
    URIAction(
        label='Watch my comp video',
        uri='https://youtu.be/eo2NZoZ2hw0'
    )
]


interestsTemplateMessage = TemplateSendMessage(
    alt_text='Interests',
    template=ButtonsTemplate(
        title='My Interests',
        text='Get my interests and activities.',
        thumbnail_image_url=INTERESTS_IMAGE_URL,
        actions=interestsActions
    )
)


interestsTextMessage = TextSendMessage(
    text='''To be honest, I am actually a speedcuber since 2015.\n
I have attended more than 20 competitions and held 3 competitions.\n
I am specialized in events such as 3x3, 2x2, 3x3 One-handed, and 3x3 fewest moves.\n
Click "Watch my comp video" to watch me solve a Rubik's cube one handed in 10 seconds!''')
