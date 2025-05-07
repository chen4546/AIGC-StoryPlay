# ai图片生成
import logging
import os.path

from .image_post import submit
from .image_get import progress
import time
import requests
import base64
import json
import datetime

def imageResult(prompt='一只猫正在画梵高', height=1024, width=1024):
    isResult = False
    submit_response_json = submit(prompt=prompt, height=height, width=width)
    # print(submit_response_json)
    submit_response_json_code = submit_response_json['code']
    if submit_response_json_code == 200:
        task_id = submit_response_json['result']['task_id']
        while (not isResult):
            time.sleep(0.5)
            result = progress(task_id)
            isResult = result['finished']
            # print(type(result))
        image_url = result['images_url'][0]
        print(image_url)
        #print(type(image_url))
        return image_url
    else:
        print(submit_response_json['msg'])
        return False


def image_download(image_url):
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y_%m_%d_%H_%M_%S")
    #image_dir_name="drawable_story"
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    image_dir_name=os.path.join(PROJECT_ROOT,"assets/images/")
    if not os.path.exists(image_dir_name):
        os.mkdir(image_dir_name)
    image_name=os.path.join(image_dir_name,formatted_date)
    image = requests.get(image_url)
    with open(image_name + '.jpg', 'wb') as file:
        file.write(image.content)
    return image_name


def image_draw(prompt):
    result = imageResult(prompt)
    if result is not False:
        # time.sleep(20)
        image_name=image_download(result)
        # 'https://ai-painting-image.vivo.com.cn/ai-painting/763783fb1774435cba505705b9d61377fb29bdce-0.png'
        return image_name

if __name__ == '__main__':
    prompt = '你走出家门，呼吸着清新的空气，感受着阳光的温暖。你穿过村庄，走向森林。森林里绿树成荫，鸟语花香，美不胜收。你沿着小路走着，突然听到了一阵呼救声。'

    image_draw(prompt)
