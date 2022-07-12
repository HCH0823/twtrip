from django.conf import settings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn

line_bot_api = LineBotApi('vswYITakGKDqTeBRGYd/647D84k935oXZKiUSO9hmmu6vZAx4nyRwo73vyalA1xo13NlUg59VXRkP55eFdiId+bLvZNKZUOsQWms8TUwppxWSZwlPktYLepUDDaDiMrW69zzHSWPPqFSHb5RPL1mjwdB04t89/1O/w1cDnyilFU=')
baseurl = 'https://b21a-60-245-120-172.jp.ngrok.io/static/'



'''def connectDb(mydb):   #資料庫暫未使用到
    try:
        mysqldb = pymysql.connect(
                host="HOST",
                user="root",
                passwd="88888888",
                database=mydb,
                charset='utf8mb4'
        )
        return mysqldb
    except Exception as e:
        logging.error('Fail to connection mysql {}'.format(str(e)))
    return None'''

def Shop(event):  #實體通路
    try:
        message = TemplateSendMessage(
            alt_text='實體通路',
            template=ButtonsTemplate(
			    thumbnail_image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/62456477a1f80300128c485d/3200x.webp?source_format=jpg',
                title='實體販售通路',  #主標題
                text='請選擇區域：',  #副標題
                actions=[
                    PostbackTemplateAction(    #按鈕文字
                        label='北區區域',
                        data='action=A&item=北部區域'  #Postback資料
                    ),
                    PostbackTemplateAction(    #按鈕文字
                        label='中部區域',
                        data='action=B&item=中部區域'  #Postback資料
                    ),
                    PostbackTemplateAction(  
                        label='南部區域',      #按鈕文字
                        data='action=C&item=南部區域'  #Postback資料
                    ),
                    PostbackTemplateAction(  
                        label='東部+離島區域',  #按鈕文字
                        data='action=D&item=南部區域'  #Postback資料
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def Health(event):  #健康小教室
    try:
        message = TemplateSendMessage(
            alt_text='健康小教室',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/60bf3a2d0e31c6002048e9a0/3200x.webp?source_format=jpg',
                        action=URITemplateAction(
                            label='頭皮問題及保養',
                            uri='https://www.decentrossi.com/blog/posts/medical-scalpcare?utm_source=line_biz&utm_medium=multi_page_medialmessage_scalpcare'
                        )
                    ),ImageCarouselColumn(
                        image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/60bf3a2d0e31c6002048e9a0/3200x.webp?source_format=jpg',
                        action=URITemplateAction(
                            label='乾燥脫皮也是濕疹嗎?',
                            uri='https://www.decentrossi.com/blog/posts/medical-telogeneffluvium?utm_source=line_biz&utm_medium=multi_page_medialmessage_telogeneffluvium'
                        )
                    ),ImageCarouselColumn(
                        image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/60bf3a2d0e31c6002048e9a0/3200x.webp?source_format=jpg',
                        action=URITemplateAction(
                            label='異位性皮膚炎治療新法',
                            uri='https://www.decentrossi.com/blog/posts/medical-eczemacauses?utm_source=line_biz&utm_medium=multi_page_medialmessage_eczemacare'
                        )
                    ),ImageCarouselColumn(
                        image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/60bf3a2d0e31c6002048e9a0/3200x.webp?source_format=jpg',
                        action=URITemplateAction(
                            label='落髮也是疫情後遺症!?',
                            uri='https://www.decentrossi.com/blog/posts/medical-telogeneffluvium?utm_source=line_biz&utm_medium=multi_page_medialmessage_telogeneffluvium'
                        )
                    ),ImageCarouselColumn(
                        image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/60bf3a2d0e31c6002048e9a0/3200x.webp?source_format=jpg',
                        action=URITemplateAction(
                            label='查看更多醫學小知識',
                            uri='https://www.decentrossi.com/pages/medical-blog?utm_source=line_biz&utm_medium=multi_page_medialmessage_medical_blog'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def Popular(event):  #熱賣商品
    try:
        message = TemplateSendMessage(
            alt_text='熱賣商品',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/5fed9e44e256e6003818e38b/2000x.webp?source_format=jpg',
                        title='頭皮甦醒洗髮粉 試管口紅組 3g×3',
                        text='NT$570\n(會員首購優惠中)',
                        actions=[
                            URITemplateAction(
                                label='前往購買',
                                uri='https://www.decentrossi.com/products/hairwashpowder3gx3'
                            ),
                            URITemplateAction(
                                label='查看更多商品',
                                uri='https://liff.line.me/1657284876-1XxEGeMq'
                            ),
                            MessageTemplateAction(
                                label='查看實體通路',
                                text='@實體通路'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/61930e6d0e1631003b4b2544/800x.webp?source_format=jpg',
                        title='頭皮甦醒洗髮粉 50g',
                        text='NT$820\n(窄口設計不適用補充包)',
                        actions=[
                            URITemplateAction(
                                label='前往購買',
                                uri='https://www.decentrossi.com/products/decent-rossi-hair-wash-powder-40gn'
                            ),
                            URITemplateAction(
                                label='查看更多商品',
                                uri='https://liff.line.me/1657284876-1XxEGeMq'
                            ),
                            MessageTemplateAction(
                                label='查看實體通路',
                                text='@實體通路'
                            ),
                        ]
                    ),
					CarouselColumn(
                        thumbnail_image_url='https://shoplineimg.com/5b0a91434e22a6da870057cf/619311e7379490668b0b968d/800x.webp?source_format=jpg',
                        title='頭皮甦醒洗髮粉 補充包五入組 50g×5',
                        text='NT$3,050\n爲親愛的頭皮，準備一季清爽',
                        actions=[
                            URITemplateAction(
                                label='前往購買',
                                uri='https://www.decentrossi.com/products/hwprefillpack50gx5'
                            ),
                            URITemplateAction(
                                label='查看更多商品',
                                uri='https://liff.line.me/1657284876-1XxEGeMq'
                            ),
                            MessageTemplateAction(
                                label='查看實體通路',
                                text='@實體通路'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def team(event):  #專業團隊
    try:
        message = TemplateSendMessage(
            alt_text='專業團隊',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://cacaomag.co/wp-content/uploads/decent-rossi_Rossi%E5%80%8B%E4%BA%BA%E7%85%A7-768x768.png',
                        action=URITemplateAction(
                            label='(創辦人)楊家瑋 介紹',
                            uri='https://www.decentrossi.com/pages/medicalinfo-experts-phrossiyang'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://img.shoplineapp.com/media/image_clips/60c95517c83c8b00203048fc/original.jpg?1623807255',
                        action=URITemplateAction(
                            label='陳家駒 中醫師 介紹',
                            uri='https://www.decentrossi.com/pages/medicalinfo-experts-tcmdrjg'
                        )
                    ),
					ImageCarouselColumn(
                        image_url='https://img.shoplineapp.com/media/image_clips/61848ee2d99ef9002cc448e0/original.jpg?1636077281',
                        action=URITemplateAction(
                            label='吳婉華 醫師 介紹',
                            uri='https://www.decentrossi.com/pages/medicalinfo-experts-drwanwanwu'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_A(event, backdata):  #處理Postback
    try:
        message = TemplateSendMessage(
            alt_text='北部實體通路',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipMt2jYYTYqolvn1bZgtoff1sI1zhk6BGqO095wh=w408-h544-k-no',
                        title='(台北市)Yoga Vibes',
                        text='營業時間：週一到週六 9:00-21:30/週日 9:00-13:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/台北市大安區復興南路一段129號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=0976-276-606'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipMU07rGXcII-AhJd4gV1UIMYsZgOV61M4lsoprk=w426-h240-k-no',
                        title='(台北市)ACTIVE LIVING 信義大安運動會館',
                        text='營業時間：10:00-22:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/台北市大安區信義路四段61號5樓'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=02-2708-0250'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]    
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipNQ17qRnxYveq3ftLDE7J_BGT3Zs__RL5sc7MLS=w408-h544-k-no',
                        title='(台北市)綠杏大藥局',
                        text='營業時間：9:00-22:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/台北市信義區吳興街241號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=02-2758-2378'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipPb8c8B6DkQff7W273agKlIZYLNXafCeTsMvjcP=w408-h271-k-no',
                        title='(台北市)SPACE CYCLE',
                        text='營業時間：週一到週五 07:00-23:00 / 週六到週日07:00-22:00 (無公休日)',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/106台北市忠孝東路四段200號13樓'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=02-2773-0108'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    )
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_B(event, backdata):  #處理Postback
    try:
        message = TemplateSendMessage(
            alt_text='中部實體通路',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipN3MgYFoBimJLZOjZ6panwueVYeCdUMMRrnQoyC=w408-h272-k-no',
                        title='(台中市)ROCKLAND P.L.U.S.',
                        text='營業時間：週一至週日 12:00-21:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/台中市西區英才路534號B1'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=04-2301-1881'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipN3MgYFoBimJLZOjZ6panwueVYeCdUMMRrnQoyC=w408-h272-k-no',
                        title='(台中市)Philo salon菲羅髮藝',
                        text='營業時間：週二到週六 10:30-19:00 / 週日 10:30-18:00 (週一公休)',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/台北市大安區信義路四段61號5樓'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=04-2380-6909'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]    
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipMQEbkRVva9p7TdlcQFSQ1IPCDPkHtvk3Wb7Ls=w426-h240-k-no',
                        title='(台中市)ITELY 伊黛莉髮藝 (新光三越)',
                        text='營業時間：週一到週日 11:00-20:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/407台中市西屯區台灣大道3段301號8樓'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=04-2258-6661'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipOwDM5TROirWXluZN5rAMV487LK-K6OwEfhWBTu=w408-h543-k-no',
                        title='(台中市)Molecure分子藥局',
                        text='營業時間：週一到週五 07:00-23:00 / 週六到週日07:00-22:00 (無公休日)',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/407台中市西屯區惠來路二段236-1號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=04-2251-3080'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    )
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_C(event, backdata):  #處理Postback
    try:
        message = TemplateSendMessage(
            alt_text='南部實體通路',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipMrDtVBGJxt-5NR6bHXCbhIysEKk6rvGjhtz8Sm=w408-h408-k-no',
                        title='(台南市)菲堤舒療美顏',
                        text='週二到週日 10:30-19:30 (週一公休)',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/702台南市南區聖南街17號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=06-265-0732'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipNJioqQ0zSnATdRF52YMTaQWIW2Gwhl5j6h-Foj=w408-h306-k-no',
                        title='(台南市)誠品生活南紡店 - 誠品書店',
                        text='營業時間：週一至週日 11:00-22:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/70155台南市東區中華東路一段366號(南紡購物中心2F)'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=06-602-5600'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]    
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipO_8JorP0Q_0awWj6OkUTW7HNdsNorK9x8yJvMA=w408-h544-k-no',
                        title='(高雄市)德妍思藥局',
                        text='營業時間：週一到週六 09:00-21:00 / 週日 09:00-17:30',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/407807高雄市三民區松江街93號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=07-313-6266'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipN6IKC1eZwpsqOM7vHYnVbLL_pwU7xAUv3PT1YX=w426-h240-k-no',
                        title='(高雄市)誠品書店-誠品生活駁二店',
                        text='營業時間：週一至週日 11:00-21:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/803高雄市鹽埕區大勇路3號(駁二藝術特區C4倉庫)'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=07-963-1200'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    )
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_D(event, backdata):  #處理Postback
    try:
        message = TemplateSendMessage(
            alt_text='東部與離島實體通路',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipND-f4FIz2UkSEy-HMX-87hwRjhZU5zuL-zVMM6=w408-h306-k-no',
                        title='(花蓮市)健安藥局',
                        text='營業時間：週一到週六 08:00-22:00 (週日公休)',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/970花蓮市中山路537號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=03-832-3031'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipNR24Kf2w8QG4wEiM1pWEtaf1b9aqRpwM0uESI0=w426-h240-k-no',
                        title='(花蓮市)安康鳳林藥局',
                        text='營業時間：週一到週日 08:00-22:00',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/975花蓮縣鳳林鎮仁愛街10號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=03-876-2227'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]    
                    ),CarouselColumn(
                        thumbnail_image_url='https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=zOEnkmUi0YjD3k_xvUxjBg&cb_client=search.gws-prod.gps&w=408&h=240&yaw=48.84568&pitch=0&thumbfov=100',
                        title='(金門)林怡廷皮膚科診所',
                        text='門診時間：08:30-20:00 (週四、週日休診)',
                        actions=[
                            URITemplateAction(
                                label='查看地圖',
                                uri='https://www.google.com.tw/maps/search/893金門縣金城鎮莒光路178號'
                            ),
                            PostbackTemplateAction(
                                label='查詢電話',
                                data='action=F&item=08-232-2986'
                            ),
                            URITemplateAction(
                                label='查看所有實體店家',
                                uri='https://www.decentrossi.com/pages/shoplocal'
                            )
                        ]
                    )
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))




'''def sendBack_E(event, backdata):  #回傳店家地址  已鏈結按鈕
    try:
        text1 = 'https://www.google.com.tw/maps/search/'+ backdata.get('item') 
       
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text1))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))'''

def sendBack_F(event, backdata):  #回傳店家電話
    try:
        text1 =  backdata.get('item') 
       
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text1))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
