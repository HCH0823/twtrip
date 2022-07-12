from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, PostbackEvent, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

from module import func
from urllib.parse import parse_qsl
from func3api.models import *


line_bot_api = LineBotApi('vswYITakGKDqTeBRGYd/647D84k935oXZKiUSO9hmmu6vZAx4nyRwo73vyalA1xo13NlUg59VXRkP55eFdiId+bLvZNKZUOsQWms8TUwppxWSZwlPktYLepUDDaDiMrW69zzHSWPPqFSHb5RPL1mjwdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('a7c994f2b3939e1cc230cb91fc97c6b8')

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@實體通路':
                        func.Shop(event)
    
                    elif mtext == '@熱賣商品':
                        func.Popular(event)
    
                    elif mtext == '@健康小教室':
                        func.Health(event)
    
                    elif mtext == '@專業團隊':
                        func.team(event)
                    

 
                    
            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件
                backdata = dict(parse_qsl(event.postback.data))
                if backdata.get('action') == 'A':
                    func.sendBack_A(event, backdata)
                elif backdata.get('action') == 'B':
                    func.sendBack_B(event, backdata)
                elif backdata.get('action') == 'C':
                    func.sendBack_C(event, backdata)
                elif backdata.get('action') == 'D':
                    func.sendBack_D(event, backdata)
                #elif backdata.get('action') == 'E':# 暫時沒用
                    #func.sendBack_E(event, backdata)
                elif backdata.get('action') == 'F':
                    func.sendBack_F(event, backdata)
                #elif backdata.get('action') == 'G':# 未使用
                    #func.sendBack_G(event, backdata)
                

 
                    
 
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
