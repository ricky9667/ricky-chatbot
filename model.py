from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackAction, MessageAction, URIAction
)


greetingTextMessage = TextSendMessage(
    '''
    Welcome to Ricky Hu Chatbot!
    '''
)

carouselTemplateMessage = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/about_yPYPVDqsg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459693293',
                title='About Me',
                text='Get my basic introduction here.',
                actions=[
                    PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message1',
                        text='message text1'
                    ),
                    URIAction(
                        label='uri1',
                        uri='https://ricky-hu.com/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/skills_SwsAapQcEg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459707045',
                title='My Skills',
                text='Get my skills in programming and my projects.',
                actions=[
                    PostbackAction(
                        label='postback2',
                        display_text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageAction(
                        label='message2',
                        text='message text2'
                    ),
                    URIAction(
                        label='uri2',
                        uri='https://ricky-hu.com/'
                    )
                ]
            )
        ]
    )
)

carouselJson = {
    "type": "template",
    "altText": "This is a carousel template",
    "template": {
        "type": "carousel",
        "columns": [
            {
                "thumbnailImageUrl": "https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/about_yPYPVDqsg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459693293",
                "imageBackgroundColor": "#FFFFFF",
                "title": "About me",
                "text": "Get my basic introduction here.",
                "defaultAction": {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://example.com/page/123"
                },
                "actions": [
                    {
                        "type": "message",
                        "label": "About me",
                        "text": "This is about me text."
                    },
                ]
            },
            {
                "thumbnailImageUrl": "https://ik.imagekit.io/pxhytijjnsj/RickyChatbot/skills_SwsAapQcEg.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1650459707045",
                "imageBackgroundColor": "#000000",
                "title": "My skills",
                "text": "Get my skills in programming and my projects.",
                "defaultAction": {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://example.com/page/222"
                },
                "actions": [
                    {
                        "type": "message",
                        "label": "My skills",
                        "text": "This is my skills text."
                    },
                ]
            }
        ],
        "imageAspectRatio": "rectangle",
        "imageSize": "cover"
    }
}
