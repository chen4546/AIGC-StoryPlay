import json


def save_message_to_json(messages, filename='chat_history.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)
        print(f'[系统] 对话历史已保存至 {filename}')
    except Exception as e:
        print(f"[错误] 保存失败: {str(e)}")

def load_message_from_json(filename='chat_history.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            messages = json.load(f)
            print(f"[系统] 已从 {filename} 加载历史对话")
            return messages
    except FileNotFoundError:
        print("[提示] 未找到历史文件，新建对话")
        return []
    except Exception as e:
        print(f"[错误] 加载失败: {str(e)}")
        return []