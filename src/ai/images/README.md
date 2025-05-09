该模块包含与 AI 图像生成相关的代码，通过调用 vivo 的 AI 绘图服务，根据场景描述提示生成相应的游戏场景图像。
主要功能
image.py：整合图像生成流程，从提交生成任务到下载保存图像。
image_post.py：向 AI 绘图服务提交图像生成任务。
image_get.py：查询图像生成任务进度和获取结果。
使用方法
在需要生成图像时，调用 image.py 中的 image_draw 函数，并传入描述场景的提示文本：
image_path = image_draw("描述场景的提示文本")
注意事项
确保 API 密钥配置正确（参考 config/apikey.json）。
图像生成可能需要一定时间，请合理处理等待逻辑。
图像保存路径为 assets/images 文件夹，确保该路径有效且可写。