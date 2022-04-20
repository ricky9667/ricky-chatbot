from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction, URIAction, ButtonsTemplate, MessageTemplateAction
)


ABOUT_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/about_yPYPVDqsg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459693293'
SKILLS_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/skills_SwsAapQcEg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459707045'
INTERESTS_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/interests_4D9iFN2ly.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459677025'
CONTACT_IMAGE_URL = 'https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/contact_rc3Yhe5QY.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650468251959'


greetingTextMessage = TextSendMessage(text='''
Welcome to Ricky Hu Chatbot!

To start, you can try the following commands to know more about me:

(O)verview: an overview of my information
(A)bout: my basic introduction
(S)kills: my experiences in programming and my projects
(I)nterests: my interests and activities
(C)ontact: my contact information
(H)elp: show this message again
''')


carouselTemplateMessage = TemplateSendMessage(
    alt_text='Help template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url=ABOUT_IMAGE_URL,
                title='About',
                text='My basic introduction.',
                actions=[
                    MessageAction(
                        label='About',
                        text='About'
                    ),
                    URIAction(
                        label='My Site',
                        uri='https://ricky-hu.com/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url=SKILLS_IMAGE_URL,
                title='Skills',
                text='Get my skills in programming and my projects.',
                actions=[
                    MessageAction(
                        label='Skills',
                        text='Skills'
                    ),
                    URIAction(
                        label='My Site',
                        uri='https://ricky-hu.com/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url=INTERESTS_IMAGE_URL,
                title='Interests',
                text='Get my interests and activities.',
                actions=[
                    MessageAction(
                        label='Interests',
                        text='Interests'
                    ),
                    URIAction(
                        label='My Site',
                        uri='https://ricky-hu.com/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url=CONTACT_IMAGE_URL,
                title='Contact',
                text='My contacts',
                actions=[
                    MessageAction(
                        label='Contact',
                        text='Contact'
                    ),
                    URIAction(
                        label='My Site',
                        uri='https://ricky-hu.com/'
                    )
                ]
            )
        ]
    )
)


aboutText = '''
I am a undergraduate student from Taipei Tech, studying Computer Science and Information Engineering. 
I am passionate about learning new skills in programming, and enjoy particiating in activities and meet new people.
I also have interest in Rubik's cube and table tennis.
'''


aboutTemplateMessage = TemplateSendMessage(
    alt_text='About template',
    template=ButtonsTemplate(
        title='About me',
        text=aboutText,
        thumbnail_image_url=ABOUT_IMAGE_URL,
        actions=[
            MessageAction(
                label='View my projects',
                text='Skills'
            ),
            URIAction(
                label='My Site',
                uri='https://ricky-hu.com/'
            )
        ]
    )
)
