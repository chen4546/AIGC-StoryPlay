# 蓝心70B模型文本生成
# encoding: utf-8
import uuid
import time
import requests
import json
from auth_util import gen_sign_headers
from json_ls import save_message_to_json

# 请替换APP_ID、APP_KEY
APP_ID = '2025978227'
APP_KEY = 'MGrAUHueZkEchisd'
URI = '/vivogpt/completions'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'


def sync_vivogpt(messages, chat, uuid_user):
    #print(type(messages))
    messages.append(chat)

    params = {
        'requestId': uuid_user  # str(uuid.uuid4())
    }
    print('requestId:', params['requestId'])

    data = {
        # 'prompt': '写一首春天的诗',
        "messages": messages,
        'model': 'vivo-BlueLM-TB-Pro',
        'sessionId': uuid_user,  # str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    start_time = time.time()
    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=data, headers=headers, params=params)

    if response.status_code == 200:
        res_obj = response.json()
        # print(f'response:{res_obj}')
        if res_obj['code'] == 0 and res_obj.get('data'):
            content = res_obj['data']['content']
            messages.append({
                "role": "assistant",
                "content": content
            })
            print(f'final content:\n{content}')
            # print(message)
            save_message_to_json(messages)
            return [messages,content]
    else:
        print(response.status_code, response.text)
    end_time = time.time()
    timecost = end_time - start_time
    # print('请求耗时: %.2f秒' % timecost)
