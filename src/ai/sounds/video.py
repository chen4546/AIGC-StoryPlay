import asyncio
import logging
import datetime
import os.path

from src.auth.load_apikey import load_apikey
from .video_copy import tts_replical_session,logging,create_vcn_task,get_vcn_list,get_vcn_task,get_vcn_task_list,delete_task,delete_all_task
from video_decode import other_audio
if __name__=='__main__':
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO,format=FORMAT)
    loop=asyncio.get_event_loop()
    app_id = load_apikey()['app_id'], app_key = load_apikey()['app_key']
    tts_obj=tts_replical_session(app_id,app_key)

    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y_%m_%d_%H_%M_%S")

    audio_file_path='1.wav'
    audio='smn.wav'
    text = '在天气晴朗的夜晚，可以看到星星和月亮。'
    text1='只羡鸳鸯不羡仙'
    text2 = '床前明月光,疑是地上霜,举头望明月,低头思故乡'
    text_wy='闺蜜,闺蜜,想不想和我玩sky光遇,喵喵喵'
    #vcn=loop.run_until_complete(create_vcn_task(tts_obj=tts_obj,audio_file_path=audio_file_path,text=text))
    #print(vcn)
    # loop.run_until_complete(get_vcn_task(vcn=vcn,tts_obj=tts_obj))
    # loop.run_until_complete(get_vcn_task_list(tts_obj=tts_obj))


    #loop.run_until_complete(delete_all_task(tts_obj))

    vcn_other={
        'wy':'9156908368_742653_791d1506-7264-49bc-990c-81458df7e6dc_v3',
        'jtt':'9156908368_742653_068ea6aa-1725-4acc-b250-9f81f90abfe1_v3',
        'mvp': '9156908368_742653_c1e2ccf6-5794-4eae-aa12-706ba8a51b3c_v3',
        'smn':'9156908368_742653_27cac71a-cea9-4abf-bb7d-78018916abd9_v3',
        "engineid": "tts_replica",

    }

    # vcn_list=loop.run_until_complete(get_vcn_list(tts_obj))
    # print(vcn_list)
    # with open('vcn.json','w') as f:
    #     for vcn in vcn_list:
    #         f.write(vcn)

    #loop.run_until_complete(get_vcn_task(vcn=vcn_other['jtt'],tts_obj=tts_obj))

    text_need=input("输入文本")
    player='wy'
    vcn=vcn_other[player]
    engineid=vcn_other['engineid']
    if not os.path.exists(player):
        os.mkdir(player)
    other_audio(app_id=app_id, app_key=app_key, vcn=vcn, text=text_need, engineid=engineid, file_name=os.path.join(player,formatted_date))

    # for vcn in vcn_list:
    #     vcn_obj=loop.run_until_complete(get_vcn_task(vcn=vcn, tts_obj=tts_obj))
    #     print(vcn_obj)
    #     engineid=vcn_obj['vcn_obj']['engineid']
    #     other_audio(app_id=app_id, app_key=app_key, vcn=vcn, text=text_need,engineid=engineid,file_name='123')

    #
    # text3='快要高考了，有粉丝说想象清华，但考不上咋办？今天教你向金华的五种方法。方法一通过数学物理化学生物信息学。'
    # vcn = loop.run_until_complete(create_vcn_task(tts_obj=tts_obj, audio_file_path=audio, text=text3))
    # print(vcn)
    # vcn_obj = loop.run_until_complete(get_vcn_task(vcn=vcn, tts_obj=tts_obj))
    # print(vcn_obj)
    # engineid=vcn_obj['vcn_obj']['engineid']
    # other_audio(app_id=app_id, app_key=app_key, vcn=vcn, text='你好',engineid=engineid,file_name='test')
