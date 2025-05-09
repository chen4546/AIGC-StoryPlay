import os
import threading
import uuid

import cv2
import numpy as np
import winsound
from PyQt5.Qt import QWidget, QTextEdit, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer

from src.ai.prompts.load_prompts import load_prompts
from src.auth.load_apikey import load_apikey
from src.other.cv2_to_pixmap import cv2_to_pixmap
from src.story_generation import image_draw, story_tell, ai_content_split, sync_vivogpt, load_message_from_json, \
    get_path

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class GameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.logo = "assets/images/logo.png"
        self.ai_content = None
        self.uuid_user = str(uuid.uuid4())
        self.messages = load_message_from_json()

        self.initUI()
        self.media_player = QMediaPlayer()

        # 启动初始故事
        threading.Thread(target=self.init_story).start()

    def initUI(self):
        # 可视化组件
        self.setWindowTitle('奇幻大陆冒险')
        self.setGeometry(300, 300, 1200, 800)
        self.setWindowIcon(QIcon(os.path.join(ROOT_PATH, self.logo)))

        # 故事文本显示
        self.story_view = QTextEdit()
        self.story_view.setReadOnly(True)

        # 输入框
        self.input_edit = QLineEdit()
        self.input_edit.returnPressed.connect(self.send_command)

        # 图片显示
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # 控制按钮
        self.btn_send = QPushButton("发送")
        self.btn_send.clicked.connect(self.send_command)

        # 布局管理
        main_layout = QVBoxLayout()
        media_layout = QHBoxLayout()

        media_layout.addWidget(self.image_label, 3)
        media_layout.addWidget(self.story_view, 2)

        main_layout.addLayout(media_layout)
        main_layout.addWidget(self.input_edit)
        main_layout.addWidget(self.btn_send)

        self.setLayout(main_layout)

    def init_story(self):
        # 初始化故事内容
        system_prompts = {
            "role": "system",
            "content": load_prompts('act_game')
        }
        start_prompts = {
            "role": "system",
            "content": load_prompts('start')
        }
        image_prompts = {
            "role": "system",
            "content": load_prompts('images')
        }
        user_init = {"role": "user", "content": "开始吧"}

        self.messages += [system_prompts, start_prompts, image_prompts]
        result = sync_vivogpt(messages=self.messages, chat=user_init, uuid_user=self.uuid_user)
        self.messages = result[0]
        self.ai_content = result[1]
        self.process_ai_response(self.ai_content)

    def send_command(self):
        # 异步处理用户输入
        user_input = self.input_edit.text()
        self.input_edit.clear()
        self.story_view.append(f"\n> Player：{user_input}")

        threading.Thread(target=self.process_user_input, args=(user_input,)).start()

    def process_user_input(self, command):
        chat = {"role": "user", "content": command}
        result = sync_vivogpt(self.messages, chat, self.uuid_user)
        self.messages = result[0]
        self.process_ai_response(result[1])

    def process_ai_response(self, ai_content):
        # 解析并更新可视化内容
        plot_and_scene = ai_content_split(ai_content)
        plot = plot_and_scene[0]
        scene = plot_and_scene[1]

        # 更新故事文本
        self.story_view.append(f"\n==== 故事进展 ====\n{plot}")

        # 加载并显示图片
        image_path = get_path(image_draw(scene), 'image')
        print(image_path)
        cv_img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        pixmap = cv2_to_pixmap(cv_img)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

        # 播放语音
        sound_path = get_path(story_tell(plot, api_id=load_apikey()['app_id'], api_key=load_apikey()['app_key']),
                              'sound')
        print(sound_path)
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)

    # @staticmethod
    # def get_path(file_name, file_class):
    #     # 路径处理方法保持不变
    #     current_path = os.path.abspath(__file__)
    #     father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    #     return os.path.join(father_path, f"{file_name}.jpg" if file_class == 'image' else f"{file_name}_pcm.wav")
    #
