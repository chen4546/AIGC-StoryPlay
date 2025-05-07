#vivo ai生图 获取图片

import time
import requests
import base64
import json
from .auth_util_image import gen_sign_headers
from .image_post import submit

# 请注意替换APP_ID、APP_KEY
APP_ID = '2025978227'
APP_KEY = 'MGrAUHueZkEchisd'
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'GET'


def progress(task_id):
    params = {
        # 注意替换为提交作画任务时返回的task_id
        'task_id': task_id
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    uri_params = ''
    for key, value in params.items():
        uri_params = uri_params + key + '=' + value + '&'
    uri_params = uri_params[:-1]

    url = 'http://{}{}?{}'.format(DOMAIN, URI, uri_params)
    #print('url:', url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        #print(response.json())
        return response.json()['result']
    else:
        print(response.status_code, response.text)
        return (response.status_code, response.text)

