该模块提供了生成 API 请求认证头部的工具函数。这些函数用于向 vivo 的各种服务发送请求时的身份验证和签名计算，确保请求的安全性和合法性。
主要功能
auth_util.py：通用认证工具函数。
auth_util_image.py：专门用于图像生成服务的认证。
auth_util_story.py：用于故事生成服务的认证。
load_apikey.py：加载 API 密钥配置。
使用方法
在向 vivo 服务发送请求时，调用相应的认证工具函数生成请求头部：
headers = gen_sign_headers(app_id, app_key, method, uri, query)
注意事项
确保 API 密钥文件（config/apikey.json）存在且内容正确。
不同的服务可能需要不同的认证参数，请参考具体服务的 API 文档。