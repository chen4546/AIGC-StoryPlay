import json
import os.path

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(PROJECT_ROOT)
apikey_path = os.path.join(PROJECT_ROOT, r'config\apikey.json')


def load_apikey(apikey_path=apikey_path):
    try:
        with open(apikey_path, 'r', encoding='utf-8') as f:
            api_key = json.load(f)
            return api_key
    except FileNotFoundError:
        print(f"[提示] 未找到密钥文件，请查看 {apikey_path} 是否存在")
    except Exception as e:
        print(f"[错误] 加载密钥失败: {str(e)}")


load_apikey()
