# 游戏音效资源文档说明

## 文件夹用途

本文件夹用于存储特定角色的音效资源，包含通过语音合成技术生成的游戏故事文本音频文件，旨在增强游戏的沉浸式体验。

## 子文件夹结构

* 该子文件夹专门存储对应角色相关的音效文件

## 音效生成方式

* 使用项目自建的 TTS（Text-to-Speech） 服务生成
* 音效内容基于游戏故事文本自动合成
* 相关实现代码位于 src/ai/sounds 目录

## 使用规范

* 音效文件由系统自动生成，原则上禁止手动修改

* 如需调整情节朗读音色，请通过以下途径：

  * 自行拷贝音色
  * 待完善
