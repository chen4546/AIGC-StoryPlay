#vivo tts 音频生成_解码
# -*- coding: utf-8 -*-
import wave
import io


class ShortTTS(object):
    vivoHelper = "vivoHelper"
    yunye = "yunye"
    wanqing = "wanqing"
    xiaofu = "xiaofu"
    yige_child = "yige_child"
    yige = "yige"
    yiyi = "yiyi"
    xiaoming = "xiaoming"


class LongTTS(object):
    x2_vivoHelper = "vivoHelper"
    x2_yige = "x2_yige"
    x2_yige_news = "x2_yige_news"
    x2_yunye = "x2_yunye"
    x2_yunye_news = "x2_yunye_news"
    x2_M02 = "x2_M02"
    x2_M05 = "x2_M05"
    x2_M10 = "x2_M10"
    x2_F163 = "x2_F163"
    x2_F25 = "x2_F25"
    x2_F22 = "x2_F22"
    x2_F82 = "x2_F82"


class Humanoid(object):
    F245_natural = "F245_natural"  # 知性柔美
    M24 = "M24"  # 俊朗男声
    M193 = "M193"  # 理性男声
    GAME_GIR_YG = "GAME_GIR_YG"  # 游戏少女
    GAME_GIR_MB = "GAME_GIR_MB"  # 游戏萌宝
    GAME_GIR_YJ = "GAME_GIR_YJ"  # 游戏御姐
    GAME_GIR_YJ = "GAME_GIR_LTY"  # 电台主播
    YIGEXIAOV = "YIGEXIAOV"  # 依格
    FY_CANTONESE = "FY_CANTONESE"  # 粤语
    FY_SICHUANHUA = "FY_SICHUANHUA"  # 四川话
    FY_MIAOYU = "FY_MIAOYU"  # 苗语


'''
input:
    pcmdata: pcm audio data
output:
    wav file-like object
'''


def pcm2wav(pcmdata: bytes, channels=1, bits=16, sample_rate=24000):
    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))
    io_fd = io.BytesIO()
    wavfile = wave.open(io_fd, 'wb')
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcmdata)
    wavfile.close()
    io_fd.seek(0)
    return io_fd

from .video_make import TTS, AueType
def short_audio(app_id,app_key,vcn,text):

    for k, v in ShortTTS.__dict__.items():
        if k.find('__') != -1:
            continue
        if v !=vcn:
            print(k, v)
            continue
        input_params = {
            # 修改为你的app_id 和 app_key
            'app_id': app_id,
            'app_key': app_key.encode('utf-8'),
            'engineid': 'short_audio_synthesis_jovi'
        }
        tts = TTS(**input_params)
        tts.open()
        # pcm
        pcm_buffer = tts.gen_radio(aue=AueType.PCM, vcn=k, text=text)
        wav_io = pcm2wav(pcm_buffer)
        with open(f'{k}_pcm.wav', 'wb') as fd:
            fd.write(wav_io.read())
        break
def long_audio(app_id,app_key,vcn,text):
    for k, v in LongTTS.__dict__.items():
        if k.find('__') != -1:
            continue
        if v != vcn:
            print(k, v)
            continue
        input_params = {
            # 修改为你的app_id 和 app_key
            'app_id': app_id,
            'app_key': app_key.encode('utf-8'),
            'engineid': 'long_audio_synthesis_screen'
        }
        tts = TTS(**input_params)
        tts.open()
        # pcm
        pcm_buffer = tts.gen_radio(aue=AueType.PCM, vcn=k, text=text)
        wav_io = pcm2wav(pcm_buffer)
        with open(f'{k}_pcm.wav', 'wb') as fd:
            fd.write(wav_io.read())
        break
def human_audio(app_id,app_key,vcn,text):
    for k, v in Humanoid.__dict__.items():
        if k.find('__') != -1:
            continue
        if v != vcn:
            print(k, v)
            continue
        input_params = {
            # 修改为你的app_id 和 app_key
            'app_id': app_id,
            'app_key': app_key.encode('utf-8'),
            'engineid': 'tts_humanoid_lam'
        }
        tts = TTS(**input_params)
        tts.open()
        # pcm
        pcm_buffer = tts.gen_radio(aue=AueType.PCM, vcn=k, text=text)
        wav_io = pcm2wav(pcm_buffer)
        with open(f'{k}_pcm.wav', 'wb') as fd:
            fd.write(wav_io.read())
        break
def other_audio(app_id,app_key,vcn,text,engineid,file_name):
    input_params = {
        'app_id': app_id,
        'app_key': app_key.encode('utf-8'),
        'engineid': engineid
    }
    tts = TTS(**input_params)
    tts.open()
    # pcm
    pcm_buffer = tts.gen_radio(aue=AueType.PCM, vcn=vcn, text=text)
    wav_io = pcm2wav(pcm_buffer)
    with open(f'{file_name}_pcm.wav', 'wb') as fd:
        fd.write(wav_io.read())

if __name__ == '__main__':
    app_id='2025978227'
    app_key='MGrAUHueZkEchisd'
    text='床前明月光,疑是地上霜,举头望明月,低头思故乡'

    human_audio(app_id=app_id,app_key=app_key,vcn="FY_SICHUANHUA",text=text)
    long_audio(app_id=app_id, app_key=app_key,vcn="x2_F22", text=text)
    short_audio(app_id=app_id, app_key=app_key, vcn='yiyi',text=text)