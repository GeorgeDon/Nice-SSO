# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import json
from django.http import HttpResponse
from common import log

@log("excute")
def sml(request):
    received_json_data = json.loads(request.body, encoding='utf-8')
    print received_json_data
    msg_from = received_json_data.get("msg_from")  # 发送方邮箱
    pwd = received_json_data.get("pwd")  # 填入发送方邮箱的授权码
    msg_to = received_json_data.get("msg_to")  # 收件人邮箱
    subject = received_json_data.get("subject")  # 主题
    content = received_json_data.get("content")
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)# 邮件服务器及端口号
        s.login(msg_from, pwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
    except smtplib.SMTPException,e:
        print "%s"%e
        response = HttpResponse("发送失败")
        return response
    # finally:
    #     s.close
    response = HttpResponse("发送成功")
    return response