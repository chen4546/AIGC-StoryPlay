#vivo TTS 声音复刻
# -*- coding: utf-8 -*-
import aiohttp
import uuid
import time
import logging
import json
import os
import asyncio
import traceback
import inspect
from aiohttp import FormData
from src.auth.auth_util_story import gen_sign_headers
from src.auth.load_apikey import load_apikey

logger = logging.getLogger()


class tts_replical_session(object):
    def __init__(self, app_id=None,
                 app_key=None,
                 domain="api-ai.vivo.com.cn"
                 ):
        if isinstance(app_key, str):
            app_key = app_key.encode()
        self._app_id = app_id
        self._app_key = app_key
        self._domain = domain
    async def _request(self, uri=None, headers={}, *args, **kwargs):
        request_id = str(uuid.uuid4()) + "-" + str(int(time.time() * 1000))
        params = {"req_id": request_id}
        sign_headers = gen_sign_headers(app_id=self._app_id, app_key=self._app_key, method='POST', uri=uri,
                                        query=params)
        headers.update(sign_headers)
        url = f"https://{self._domain}{uri}?req_id={request_id}"
        f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]
        try:
            async with aiohttp.ClientSession() as session:
                for _ in range(3):
                    async with session.post(url=url, headers=headers, *args, **kwargs) as response:
                        if response.status != 200:
                            error_text = await response.text(encoding='utf-8')
                            logger.error(f"get http code {response.status}, content:{error_text}")
                            return None
                        ctx_dispos = response.content_disposition
                        if ctx_dispos:
                            data = await response.read()
                            logger.info(f"[{f_name}] get rsp: file[{ctx_dispos.filename}|{len(data)}]")
                            return ctx_dispos.filename, data
                        else:
                            t = await response.text(encoding='utf-8')
                            logger.info(f"[{f_name}] get rsp: {t}")
                            return t
        except Exception:
            logger.error(f"get exception:{str(traceback.format_exc())}")
        return None
    async def create_vcn_task(self, wav_buffer: bytes = None, text: str = None):
        uri = "/replica/create_vcn_task"
        data = FormData()
        data.add_field('audio', wav_buffer, filename='audio', content_type='application/octet-stream')
        data.add_field('text', text)
        headers = {}
        result_txt = await self._request(uri, headers, data=data, timeout=30)
        if not result_txt:
            return None
        return json.loads(result_txt)
    async def get_vcn_task(self, vcn: str = None):
        uri = "/replica/get_vcn_task"
        json_data = {
            "vcn": vcn
        }
        headers = {}
        result_txt = await self._request(uri, headers, json=json_data, timeout=30)
        if not result_txt:
            return None
        return json.loads(result_txt)
    async def get_vcn_task_list(self):
        uri = "/replica/get_vcn_task_list"
        headers = {}
        result_txt = await self._request(uri, headers, timeout=30)
        if not result_txt:
            return None
        return json.loads(result_txt)
    async def del_task(self, vcn: str = None):
        uri = "/replica/del_task"
        json_data = {
            "vcn": vcn
        }
        headers = {}
        result_txt = await self._request(uri, headers, json=json_data, timeout=5)
        if not result_txt:
            return None
        return json.loads(result_txt)


async def test_vcn_session(app_id=None, app_key=None):
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    audio_file = os.path.join(BASE_PATH, '1.wav')
    tts_obj = tts_replical_session(app_id, app_key)
    # 上传用户录音及文本
    with open(audio_file, 'rb') as fd:
        wav_buffer = fd.read()
    text = '在天气晴朗的夜晚，可以看到星星和月亮。'
    rsp_obj = await tts_obj.create_vcn_task(wav_buffer, text)
    vcn = rsp_obj['vcn']
    print('111')
    # 定时检测状态
    while True:
        await asyncio.sleep(3)
        vcn_result = await tts_obj.get_vcn_task(vcn)
        if vcn_result['error_code'] != 0:
            break
        if vcn_result['vcn_obj']['status'] >= 3:
            break
    # 拉取所有音色信息
    await tts_obj.get_vcn_task_list()

    print('222')
    # 删除音色
    await tts_obj.del_task(vcn)
    print('333')
async def  create_vcn_task(tts_obj,audio_file_path,text):
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    audio_file = os.path.join(BASE_PATH, audio_file_path)
    with open(audio_file, 'rb') as fd:
        wav_buffer = fd.read()
    #text = '在天气晴朗的夜晚，可以看到星星和月亮。'
    rsp_obj = await tts_obj.create_vcn_task(wav_buffer, text)
    vcn = rsp_obj['vcn']
    return vcn

async def get_vcn_task(tts_obj,vcn):
    while True:
        await asyncio.sleep(3)
        vcn_result = await tts_obj.get_vcn_task(vcn)
        if vcn_result['error_code'] != 0:
            break
        if vcn_result['vcn_obj']['status'] >= 3:
            break
    return vcn_result
async def get_vcn_task_list(tts_obj):
    result= await tts_obj.get_vcn_task_list()
    return result
async def get_vcn_list(tts_obj):
    vcn_list = []
    result = await get_vcn_task_list(tts_obj=tts_obj)
    vcn_obj_list = result['vcn_obj_list']
    for vcn_obj in vcn_obj_list:
        vcn_list.append(vcn_obj['vcn'])
    return (vcn_list)
async def delete_task(tts_obj,vcn):
    await tts_obj.del_task(vcn)
async def delete_all_task(tts_obj):
    vcn_list=[]
    result=await get_vcn_task_list(tts_obj=tts_obj)
    vcn_obj_list=result['vcn_obj_list']
    # print(vcn_obj_list)
    # print(type(vcn_obj_list))
    for vcn_obj in vcn_obj_list:
        # print(vcn_obj)
        # print(type(vcn_obj))
        vcn=vcn_obj['vcn']
        await delete_task(tts_obj=tts_obj,vcn=vcn)
        print(f'delete {vcn}')
        vcn_list.append(vcn_obj['vcn'])
    print(vcn_list)




if __name__ == '__main__':
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    loop = asyncio.get_event_loop()
    app_id = load_apikey()['app_id']
    app_key = load_apikey()['app_key']
    #loop.run_until_complete(test_vcn_session(app_id, app_key ))
    ########################################################
    tts_obj = tts_replical_session(app_id, app_key)
    audio_file_path = '1.wav'
    text = '在天气晴朗的夜晚，可以看到星星和月亮。'
    vcn=loop.run_until_complete(create_vcn_task(tts_obj=tts_obj,audio_file_path=audio_file_path,text=text))
    print(vcn)
    #loop.run_until_complete(get_vcn_task(vcn=vcn,tts_obj=tts_obj))
    #loop.run_until_complete(get_vcn_task_list(tts_obj=tts_obj))
    #loop.run_until_complete(delete_all_task(tts_obj))
    loop.run_until_complete(get_vcn_list(tts_obj))