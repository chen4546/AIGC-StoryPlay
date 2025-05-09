# API 请求认证模块文档

## 模块概述

提供生成 API 请求认证头部的工具函数，用于向 vivo 服务发送请求时的身份验证和签名计算，保障请求安全合法。

## 核心组件

* `auth_util.py` - 通用认证工具
* `auth_util_image.py` - 图像生成服务专用认证
* `auth_util_story.py` - 故事生成服务专用认证
* `load_apikey.py` - API 密钥配置加载器

## 调用示例

```
headers = gen_sign_headers(app_id, app_key, method, uri, query)
```

**注意事项：**

* 确认 `config/apikey.json` 文件存在且格式正确
* 不同服务需参考对应 API 文档的特殊认证要求，请参考具体服务的 API 文档。