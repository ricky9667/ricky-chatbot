from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackAction, MessageAction, URIAction
)


greetingTextMessage = TextSendMessage(
    text='''
    Welcome to Ricky Hu Chatbot!
    
    To start, you can try the following commands to know more about me:
    (O)verview: an overview of my information
    (A)bout: my basic introduction
    (S)kills: my experiences in programming and my projects
    (I)nterests: my interests and activities
    (C)ontact: my contact information.
    (H)elp: show this message again
    '''
)

carouselTemplateMessage = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/about_yPYPVDqsg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459693293',
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
                thumbnail_image_url='https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/skills_SwsAapQcEg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459707045',
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
                thumbnail_image_url='https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/interests_4D9iFN2ly.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459677025',
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
                thumbnail_image_url='https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/contact_rc3Yhe5QY.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650468251959',
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
