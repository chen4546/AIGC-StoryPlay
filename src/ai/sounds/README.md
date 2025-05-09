该模块实现了将游戏故事文本转换为语音音效的功能，通过调用 vivo 的 TTS 服务，生成角色对话和叙述的语音文件。
主要功能
story_tell.py：将文本转换为语音，并保存为音频文件。
video.py：演示语音合成的使用场景和流程。
video_copy.py：声音复刻相关功能，创建和管理音色克隆任务。
video_decode.py：音频数据处理和解码功能。
使用方法
在需要生成语音时，调用 story_tell.py 中的 story_tell 函数：
audio_path = story_tell(text, api_id, api_key)
注意事项
音色克隆任务需要提前创建并获取音色标识符（vcn）。
语音生成可能涉及异步操作，请确保正确处理事件循环。
音频文件保存路径为 assets/sounds 文件夹及其子文件夹，确保路径可写。