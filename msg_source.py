from linebot.models import *

about_me = TemplateSendMessage(
    alt_text='All About Me',
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
interest = TextSendMessage(text='在工作之餘，我喜歡一切和音樂相關的事物，也喜歡創作，閒暇之餘打打電動也是我的樂趣之一！')


experience = TemplateSendMessage(
    alt_text='My Experience',
    template=ButtonsTemplate(
        thumbnail_image_url='https://miro.medium.com/fit/c/256/256/2*Ka2wd39BpMA6lm4zanG1ng.png',
        title='經歷',
        text='好奇我的經歷嗎？ 選一個你想知道的吧！',
        actions=[
            MessageTemplateAction(label='學歷', text='學歷'),
            MessageTemplateAction(label='工作經歷', text='工作經歷'),
        ]
    )
)

education = TemplateSendMessage(
    alt_text='My Education',
    template=ButtonsTemplate(
        thumbnail_image_url='https://miro.medium.com/fit/c/256/256/2*Ka2wd39BpMA6lm4zanG1ng.png',
        title='學歷',
        text='碩士：國立臺北科技大學 - 資訊工程所\n大學：國立臺北科技大學 - 資訊工程系',
        actions=[
            URITemplateAction(label='臺北科技大學 - 資訊工程系', uri='https://csie.ntut.edu.tw/csie/index_i.htm'),
        ]
    )
)

work = TemplateSendMessage(
    alt_text='My Work',
    template=ButtonsTemplate(
        thumbnail_image_url='https://miro.medium.com/fit/c/256/256/2*Ka2wd39BpMA6lm4zanG1ng.png',
        title='工作經歷',
        text='SkyREC：後端工程師 _ 2018/10 ~ 2019/11',
        actions=[
            URITemplateAction(label='SkyREC', uri='https://www.skyrec.cc/'),
        ]
    )
)

responseDict = {
    '關於我': about_me,
    '個性': personality,
    '興趣': interest,
    '經歷': experience,
    '學歷': education,
    '工作經歷': work
}
