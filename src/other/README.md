## 辅助工具模块文档

### 模块概述

该模块包含项目中使用的**辅助工具函数**，主要用于 OpenCV 图像格式与 PyQt 图像格式之间的转换。

### 主要功能

* `cv2_to_pixmap.py`：实现 OpenCV 图像格式到 PyQt `QPixmap` 格式的转换，支持在 GUI 界面中显示图像

### 使用方法

在需要将 OpenCV 图像显示到 PyQt 界面时，调用转换函数：

```
pixmap = cv2_to_pixmap(cv_img)
```

### 注意事项

* 确保已正确安装 OpenCV 和 PyQt 依赖库
* 输入图像必须为有效的 OpenCV 图像格式（`numpy` 数组）
