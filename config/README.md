## 配置文件模块

该文件夹包含项目运行所需的配置文件，如API密钥配置等敏感信息。

### 文件说明

* `apikey.json` - 存储项目访问外部API服务所需的密钥信息(需自行创建)，包含字段：

  * app\_id - 应用标识符
  * app\_key - 应用认证密钥

* `apikey_example.json` - apikey格式示例文件
* `vcn.json` - 用户复刻音频vcn存放文件，具体查看 `src\ai\sounds` 目录下的说明

### 配置方法

1. 向vivo公司申请api密钥
2. 按以下格式保存密钥信息：

```
{
  "app_id": "你的应用ID",
  "app_key": "你的应用密钥"
}
```
