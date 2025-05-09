# 对话历史数据管理文档

## 模块功能

实现游戏数据（含对话历史）的持久化存储和加载，维护游戏状态连续性。

## 核心组件

* `json_ls.py` - JSON 数据处理器
* `history/` - 历史记录存储目录

## 接口示例

保存数据：

```
save_message_to_json(messages)
```

加载数据：

```
messages = load_message_from_json()
```

**维护要求：**

* 存储路径：`data/history/`（需确保可写权限）
* 运行时禁止直接修改 JSON 文件
* 建议通过版本控制管理历史文件变更