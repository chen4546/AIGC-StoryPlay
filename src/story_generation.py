# encoding: utf-8
import json
import os
import uuid

import cv2

from data.json_ls import load_message_from_json
from ai.prompts.load_prompts import load_prompts
from ai.text.vivo_70B import sync_vivogpt
import winsound
from ai.sounds.story_tell import story_tell
from ai.images.image import image_draw
from src.auth.load_apikey import load_apikey

def get_path(file_name, file_class):
    # 获取当前文件路径
    #current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    #father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    if file_class == 'sound':
        #sound_path = os.path.join(father_path, file_name) + "_pcm.wav"
        sound_path=file_name+"_pcm.wav"
        return sound_path
    elif file_class == 'image':
        #image_path = os.path.join(father_path, file_name) + ".jpg"
        image_path=file_name+".jpg"
        #print(file_name)
        print(image_path)
        return image_path


def sound_play(sound_path):
    print(sound_path)
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)


def image_play(image_path):
    img_path = image_path
    img = cv2.imread(img_path)
    cv2.namedWindow('scene', 0)
    cv2.resizeWindow('scene', 500, 500)
    cv2.imshow('scene', img)
    cv2.waitKey()
    cv2.destroyWindow('scene')


def ai_content_split(ai_content):
    content = json.loads(ai_content)
    plot = content['plot']
    scene = content['scene']
    #print(content)
    #print(type(content))
    return [plot, scene]


def main():
    uuid_user = str(uuid.uuid4())

    messages = load_message_from_json()

    # print(load_prompts())
    system_prompts = {
        "role": "system",
        "content": load_prompts('act_game')
        # "content": load_prompts('wuxia')
    }
    start_prompts = {
        "role": "system",
        "content": load_prompts('start')
    }
    image_prompts = {
        "role": "system",
        "content": load_prompts('images')
    }
    user_init = {
        "role": "user",
        "content": "开始吧"
    }
    messages.append(system_prompts)
    messages.append(start_prompts)
    messages.append(image_prompts)
    result = sync_vivogpt(messages, user_init, uuid_user)
    messages = result[0]
    ai_content = result[1]
    plot_and_scene = ai_content_split(ai_content)
    plot = plot_and_scene[0]
    scene = plot_and_scene[1]
    sound_path = get_path(story_tell(plot,api_id=load_apikey()['app_id'],api_key=load_apikey()['app_key']), 'sound')
    image_path = get_path(image_draw(scene), 'image')
    sound_play(sound_path=sound_path)
    image_play(image_path=image_path)

    # messages = [
    #     {
    #         "role": "system",
    #         "content": "I want you to play a text-based adventure game. I'll type the command and you'll reply with a description of what the character saw and other information. I hope you only reply the game output in Chinese and nothing else. Don't write explanations. Do not type commands unless I instruct you to do so. When I need supplementary settings, I put the text in brackets (like this). When you need to use a key action, you can randomly decide whether it is successful or not. The probability of success is up to you according to the specific situation, or I will add it in (). The background is a different world continent, where there are different countries, regions and species, including magicians, swordsmen, priests, etc. Please conceive the complete power and key figures. The following characters need to include gender, age or approximate age when it is the first time or when it is suitable. My gender is male and I am 18 years old. Tell me the gender and age of other characters. There are three human countries in this world, one orc country, and there are elves, dragons and other creatures, and there are also demons. Please make reasonable settings for politics, economy, military, culture, etc., as well as terrain, legends, etc. Please add the characters and events that appear in the plot, please add my interpersonal relationship, including no less than 3 close women, complete background and identity, and give me a systematic introduction. Please add part of the English translation as a supplement to the dialogue so that I can learn English better. Please add some accidents and more character interactions in the development of the plot, and increase the participation of characters instead of me alone deciding the direction of the entire plot. Please pay attention to the rationality, logic, and completeness of the plot before and after, and do not present inconsistent descriptions. Please finish the background and me, and start the plot when I walk out of the house"
    #     },
    # ]
    while True:
        user_input = input("111:")
        chat = {
            "role": "user",
            "content": user_input
        }

        result = sync_vivogpt(messages, chat, uuid_user)
        messages = result[0]
        ai_content = result[1]
        # story_tell(ai_content)
        plot_and_scene = ai_content_split(ai_content)
        plot = plot_and_scene[0]
        scene = plot_and_scene[1]
        sound_path = get_path(story_tell(plot,api_id=load_apikey()['app_id'],api_key=load_apikey()['app_key']), 'sound')
        image_path = get_path(image_draw(scene), 'image')
        sound_play(sound_path=sound_path)
        image_play(image_path=image_path)



if __name__ == '__main__':
    main()

    # ai_content_split("{\n  \"plot\": \"你名叫李清风，是一名18岁的青年剑士。你生活在一个名为光辉联盟的人类国家，这个国家以剑术和魔法闻名。你的父亲是一名著名的剑士，母亲则是一名魔法师。你在他们的教导下，从小就展现出了非凡的剑术天赋。今天是你18岁的生日，你决定离开家乡，去探索这个神秘的大陆。\",\n  \"scene\": \"你走出家门，看到了一片广袤的平原。平原上长满了绿油油的草地，远处有一座高山，山上有一座古老的城堡。你决定向城堡的方向前进。\"\n}")
