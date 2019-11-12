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
            MessageTemplateAction(label='工作', text='工作'),
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
        text='2018/10 ~ 2019/11\nSkyREC：後端工程師',
        actions=[
            URITemplateAction(label='SkyREC', uri='https://www.skyrec.cc/'),
        ]
    )
)

expertise = TemplateSendMessage(
    alt_text='My Expertise',
    template=ButtonsTemplate(
        thumbnail_image_url='https://pbs.twimg.com/profile_images/3338800670/ec418405dea1befbb825f836adea8b24_400x400.jpeg',
        title='專長',
        text='你想知道哪方面的專長呢？',
        actions=[
            MessageTemplateAction(label='技能', text='技能'),
            MessageTemplateAction(label='音樂', text='音樂'),
        ]
    )
)

skill = TextSendMessage(text='大學到碩班較常使用的是 C/C++ ，後來因為工作是跟機器學習相關因而開始轉向 Python 的跑道，平時使用 Linux 的系統做開發環境，也在上一份工作當中學會佈署 Docker')

music = TemplateSendMessage(
    alt_text='My Music',
    template=ButtonsTemplate(
        thumbnail_image_url='https://b.thumbs.redditmedia.com/obn8AkLEsnOkg_x2LfqOnAloHayRNfqr6yosGqkI_zo.png',
        title='音樂人生',
        text='工作之餘音樂是我不可或缺的部分人生，我平常會寫一些創作放到網站上，有時候也會辦一些很小很小的表演',
        actions=[
            URITemplateAction(label='Youtube', uri='https://www.youtube.com/watch?v=ENb51OHHgCA'),
            URITemplateAction(label='Street Voice', uri='https://streetvoice.com/taco12347/'),
        ]
    )
)

resume = TextSendMessage(text='這是我的履歷，點進去看看吧！\nhttps://www.cakeresume.com/s--BQxhyw5w6PFHD-ZYPB1iOA--/tako-huang')

responseDict = {
    '關於我': about_me,
    '個性': personality,
    '興趣': interest,
    '經歷': experience,
    '學歷': education,
    '工作': work,
    '專長': expertise,
    '技能': skill,
    '音樂': music,
    '履歷': resume
}
