import asyncio
import logging
import datetime
import os.path

from .video_copy import tts_replical_session, logging, create_vcn_task, get_vcn_list, get_vcn_task, get_vcn_task_list,delete_task, delete_all_task
from .video_decode import other_audio


def story_tell(text):
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    loop = asyncio.get_event_loop()
    app_id = '2025978227'
    app_key = 'MGrAUHueZkEchisd'
    tts_obj = tts_replical_session(app_id, app_key)

    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y_%m_%d_%H_%M_%S")

    vcn_other = {
        'wy': '9156908368_742653_791d1506-7264-49bc-990c-81458df7e6dc_v3',
        'jtt': '9156908368_742653_068ea6aa-1725-4acc-b250-9f81f90abfe1_v3',
        'mvp': '9156908368_742653_c1e2ccf6-5794-4eae-aa12-706ba8a51b3c_v3',
        'smn': '9156908368_742653_27cac71a-cea9-4abf-bb7d-78018916abd9_v3',
        "engineid": "tts_replica",

    }

    # text_need = input("输入文本")
    text_need = text
    player = 'smn'
    vcn = vcn_other[player]
    engineid = vcn_other['engineid']
    if not os.path.exists(player):
        os.mkdir(player)
    file_name = os.path.join(player, formatted_date)
    other_audio(app_id=app_id, app_key=app_key, vcn=vcn, text=text_need, engineid=engineid,
                file_name=file_name)

    return file_name


