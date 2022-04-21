from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction, URIAction, ButtonsTemplate, MessageTemplateAction
)

from src.about import ABOUT_IMAGE_URL, aboutActions
from src.skills import SKILLS_IMAGE_URL, skillsActions
from src.interests import INTERESTS_IMAGE_URL, interestsActions
from src.contact import CONTACT_IMAGE_URL, contactActions

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
                title='About Me',
                text='My basic introduction.',
                actions=aboutActions
            ),
            CarouselColumn(
                thumbnail_image_url=SKILLS_IMAGE_URL,
                title='My Skills',
                text='Get my skills in programming and my projects.',
                actions=skillsActions
            ),
            CarouselColumn(
                thumbnail_image_url=INTERESTS_IMAGE_URL,
                title='Interests',
                text='Get my interests and activities.',
                actions=interestsActions
            ),
            CarouselColumn(
                thumbnail_image_url=CONTACT_IMAGE_URL,
                title='Contact',
                text='My contacts',
                actions=contactActions
            )
        ]
    )
)
