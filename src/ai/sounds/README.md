# 语音合成模块文档

## 模块描述

该模块实现了将游戏故事文本转换为语音音效的功能，通过调用 vivo 的 TTS 服务，生成角色对话和叙述的语音文件。

## 主要功能

* **story\_tell.py** - 文本转语音并保存为音频文件
* **video.py** - 演示语音合成的使用场景和流程
* **video\_copy.py** - 声音复刻功能（创建/管理音色克隆任务）
* **video\_decode.py** - 音频数据处理与解码

## 使用方法

调用 `story_tell` 函数生成语音：

```
audio_path = story_tell(text, api_id, api_key, plater_setting)
```

## 注意事项

* 音色克隆需提前创建并获取音色标识符（vcn）
* 语音生成可能涉及异步操作，需正确处理事件循环
* 音频文件默认保存路径：`assets/sounds` 及其子文件夹
* `story_tell` 接口初始使用 `video_decode` 中的 `human_audio`函数,音色默认使用 `GAME_GIR_LTY` ,如需修改自定义音色,可修改