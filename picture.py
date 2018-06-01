from PIL import Image
import numpy as np


print("程序主要参考自https://zhuanlan.zhihu.com/p/30264388?utm_source=com.tencent.tim&utm_medium=social")
print("\n输入素描图片黑度值（0-100 ，建议10-20):")
black_class = int(input())
print("输入图片路径(例如F:\壁纸\斯嘉丽\cool.jpg):")
address = input()
print("输入希望保存的路径(例如：F:\壁纸\斯嘉丽\cool_1.jpg):")
sava_addr = input()
print("创作中……")
a = np.asarray(Image.open(r'%s' % address).convert('L')).astype('float')

depth = black_class  # (0-100)
grad = np.gradient(a)  # 取图像灰度的梯度值
grad_x, grad_y = grad  # 分别取横纵图像梯度值
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
vec_az = np.pi / 4.  # 光源的方位角度，弧度值
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
dz = np.sin(vec_el)  # 光源对z 轴的影响

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))  # 重构图像
im.save(r'%s' % sava_addr)
print("创作完成^_^\n按任意键退出")
input()
