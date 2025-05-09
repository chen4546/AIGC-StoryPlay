该模块负责游戏数据的存储和加载，包括对话历史记录等，确保游戏状态的连续性和数据的持久化。
主要功能
json_ls.py：处理 JSON 格式的游戏数据，如保存和加载对话历史。
history：存储对话历史记录文件（如 chat_history.json）。
使用方法
保存对话历史：
save_message_to_json(messages)
加载对话历史：
messages = load_message_from_json()
注意事项
对话历史文件存储在 data/history 文件夹，请确保该路径存在且可写。数据文件采用 JSON 格式，易于阅读和编辑，但请注意不要在运行时直接修改，以免造成数据不一致。