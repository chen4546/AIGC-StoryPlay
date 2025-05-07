import asyncio
import datetime
import os.path
from contextlib import suppress

from .video_copy import tts_replical_session, logging
from .video_decode import other_audio
from src.auth.load_apikey import load_apikey


def story_tell(text, api_id, api_key):
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    app_id = api_id
    app_key = api_key
    tts_obj = tts_replical_session(app_id, app_key)

    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y_%m_%d_%H_%M_%S")

    vcn_other = {
        'wy': '9156908368_742653_791d1506-7264-49bc-990c-81458df7e6dc_v3',
        'jtt': '9156908368_742653_068ea6aa-1725-4acc-b250-9f81f90abfe1_v3',
        'mvp': '9156908368_742653_c1e2ccf6-5794-4eae-aa12-706ba8a51b3c_v3',
        'manbo': '9156908368_742653_27cac71a-cea9-4abf-bb7d-78018916abd9_v3',
        "engineid": "tts_replica",

    }

    # text_need = input("输入文本")
    text_need = text
    player = 'manbo'
    vcn = vcn_other[player]
    engineid = vcn_other['engineid']
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    sounds_dir_name = os.path.join(PROJECT_ROOT, "assets/sounds/")
    sounds_player_dir_name = os.path.join(sounds_dir_name, player)
    if not os.path.exists(sounds_player_dir_name):
        os.mkdir(sounds_player_dir_name)
    file_name = os.path.join(sounds_player_dir_name, formatted_date)

    # 确保异步操作在事件循环中执行
    async def async_wrapper():
        return other_audio(
            app_id=app_id,
            app_key=app_key,
            vcn=vcn,
            text=text_need,
            engineid=engineid,
            file_name=file_name
        )

    try:
        loop.run_until_complete(async_wrapper())
    finally:
        # 清理事件循环
        with suppress(Exception):
            loop.close()

    # other_audio(app_id=app_id, app_key=app_key, vcn=vcn, text=text_need, engineid=engineid,
    #             file_name=file_name)

    return file_name
