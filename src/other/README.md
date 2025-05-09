该模块包含一些项目中使用的辅助工具函数，如 OpenCV 图像到 PyQt 图像格式的转换工具。
主要功能
cv2_to_pixmap.py：将 OpenCV 图像格式转换为 PyQt 的 QPixmap 格式，用于在界面中显示图像。
使用方法
在需要将 OpenCV 图像显示到 PyQt 界面时，调用转换函数：
pixmap = cv2_to_pixmap(cv_img)
注意事项
确保 OpenCV 和 PyQt 已正确安装。输入图像应为有效的 OpenCV 图像格式（numpy 数组）。