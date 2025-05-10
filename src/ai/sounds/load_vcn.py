import json
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
#print(PROJECT_ROOT)
vcn_path = os.path.join(PROJECT_ROOT, r'config\vcn.json')


def load_vcn(vcn_path=vcn_path):
    try:
        with open(vcn_path, 'r', encoding='utf-8') as f:
            api_key = json.load(f)
            return api_key
    except FileNotFoundError:
        print(f"[提示] 未找到密钥文件，请查看 {vcn_path} 是否存在")
    except Exception as e:
        print(f"[错误] 加载密钥失败: {str(e)}")

