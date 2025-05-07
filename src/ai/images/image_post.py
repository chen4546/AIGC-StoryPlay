#!/usr/bin/env python
# encoding: utf-8
#vivo ai绘图 发送请求

import requests
import base64
import json
from src.auth.auth_util_image import gen_sign_headers
from src.auth.load_apikey import load_apikey

# 请注意替换APP_ID、APP_KEY
APP_ID =load_apikey()['app_id']
APP_KEY=load_apikey()['app_key']
URI = '/api/v1/task_submit'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'
def submit(prompt: "一只梵高画的猫",height=1024,width=768):
   params = {}
   data = {
    'height': height,
    'width': width,
    'prompt': prompt,
    'styleConfig': '7a0079b5571d5087825e52e26fc3518b',
    'userAccount': 'thisistestuseraccount'
   }

   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
   headers['Content-Type'] = 'application/json'

   url = 'http://{}{}'.format(DOMAIN, URI)
   response = requests.post(url, data=json.dumps(data), headers=headers)
   if response.status_code == 200:
        print(response.json())

        return response.json()
   else:
       print(response.status_code, response.text)
       print(1111111111)
       return (response.status_code, response.text)