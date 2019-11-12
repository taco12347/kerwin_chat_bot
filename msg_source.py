from linebot.models import *

about_me = TemplateSendMessage(
    alt_text='Somthing About Me',
    template=ButtonsTemplate(
        thumbnail_image_url='https://media.proprofs.com/images/QM/user_images/1837008/3862113809.png',
        title='關於我',
        text='Hello, 我是 Kerwin, 點擊下方來了解更多的我吧！',
        actions=[
            MessageTemplateAction(label='個性', text='個性'),
            MessageTemplateAction(label='興趣', text='興趣'),
            MessageTemplateAction(label='經歷', text='經歷'),
            MessageTemplateAction(label='專長', text='專長')
        ]
    )
)

personality = TextSendMessage(text='我是一個樂觀進取的人，喜歡嘗試新的事物，不喜歡百無聊賴的人生，喜歡和人們接觸，一開始看起來有點難以接近，但認識之後就會發現不一樣的我')

responseDict = {
    '關於我': about_me,
    '個性': personality
}
