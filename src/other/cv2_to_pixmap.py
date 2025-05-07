import cv2
from PyQt5.QtGui import QPixmap, QImage


def cv2_to_pixmap(cv_img):
    # 通道顺序转换 BGR→RGB
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    # 获取图像维度信息
    height, width, channels = rgb_image.shape
    # 计算每行字节数（关键参数）
    bytes_per_line = 3 * width  # RGB三通道，每个像素3字节
    # 创建QImage对象
    qimage = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
    # 转换为QPixmap
    return QPixmap.fromImage(qimage)