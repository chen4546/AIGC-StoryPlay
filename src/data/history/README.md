# 对话历史存储文档

## 文件说明

存储玩家与 AI 的对话记录，保障游戏对话的连续性和可追溯性。

## 核心文件

* `chat_history.json` - 结构化存储对话记录

## 数据结构

```
{
  "messages": [
    {
      "role": "user|assistant|system",
      "content": "消息内容",
    }
  ]
}
```

**使用规范：**

* 通过 `src/data/json_ls.py` 进行存取操作
* 禁止直接修改历史文件以避免数据异常
