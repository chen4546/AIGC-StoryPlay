# 奇幻大陆冒险游戏项目文档

## 项目概述

基于Python的奇幻大陆冒险游戏项目，通过调用AI接口生成互动故事文本、场景图像和语音音效，提供沉浸式文字冒险体验。

## 项目结构

```
StoryPlay/
├── README.md                   # 项目说明
├── requirements.txt            # 项目依赖
│
├── assets/                     # 游戏资源文件夹
│   ├── images/                 # 图像资源
│   │   ├── 2025_05_07_22_51_33.jpg
│   │   ├── 2025_05_07_22_52_48.jpg
│   │   └── README.md           # 图像资源说明
│   └── sounds/                 # 音效资源
│       ├── README.md           # 音效资源说明
│       └── manbo/              # 特定角色音效
│           ├── 2025_05_07_22_51_35_pcm.wav
│           └── 2025_05_07_22_52_50_pcm.wav
│
├── config/                     # 配置文件夹
│   ├── apikey.json             # API 密钥配置(需自行配置)
│   ├── apikey_example.json     # API 密钥示例
│   └── README.md               # 配置文件说明
│
├── docs/                       # 文档文件夹
│   └── README.md               # 文档说明
│
└── src/                        # 源代码文件夹
    ├── main.py                 # 项目入口
    ├── README.md               # 源代码总说明
    └── story_generation.py     # 故事生成代码
    └─ai/                       # AI 相关功能
    │  ├── images/              # 图像生成
    │  │   ├── image.py
    │  │   ├── image_get.py
    │  │   ├── image_post.py
    │  │   └── README.md        # 图像生成说明
    │  │
    │  ├── prompts/             # 提示模板
    │  │   ├── act_game_prompts.txt
    │  │   ├── images_prompts.txt
    │  │   ├── load_prompts.py
    │  │   ├── martial_arts_prompts.txt
    │  │   ├── README.md        # 提示模板说明
    │  │   └── start_prompts.txt
    │  │
    │  ├── sounds/              # 语音合成
    │  │   ├── README.md        # 语音合成说明
    │  │   ├── story_tell.py
    │  │   ├── video.py
    │  │   ├── video_copy.py
    │  │   └── video_decode.py
    │  │
    │  └── text/                # 文本处理
    │      ├── README.md        # 文本处理说明
    │      └── vivo_70B.py
    │
    ├─auth/                     # API 认证
    │   ├── README.md           # API 认证说明
    │   ├── auth_util.py
    │   ├── auth_util_image.py
    │   ├── auth_util_story.py
    │   └── load_apikey.py
    │
    ├─data/                     # 数据管理
    │   ├── README.md           # 数据管理说明
    │   ├── json_ls.py
    │   └── history/            # 对话历史记录
    │       ├── chat_history.json
    │       └── README.md       # 对话历史说明
    │
    ├─other/                    # 其他工具
    │   ├── README.md           # 其他工具说明
    │   └── cv2_to_pixmap.py
    │
    ├─utils/                    # 通用工具
    │   └── README.md           # 通用工具说明
    │
    └─ui/                       # 用户界面
        ├── main_window.py      # 主界面代码
        └── README.md           # 用户界面说明
        
```

## 依赖安装

```
pip install -r requirements.txt
```

## 使用说明

1. 配置API密钥到`config/apikey.json`文件
2. 运行`src/main.py`启动游戏
3. 在游戏界面中输入指令体验冒险故事

## 注意事项

* 确保API密钥有效
* 保持网络连接正常以调用AI接口服务
