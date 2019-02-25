# -*- coding: utf-8 -*-

# ############## 1. 2D图表—散点图和线图 ##############
# # 1-1 导入模块
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# # 1-2 通过rcParams设置全局横纵轴字体的大小
# mpl.rcParams['xtick.labelsize'] = 24
# mpl.rcParams['ytick.labelsize'] = 24
# # 设置字体样式，这里设置为中文黑体
# plt.rcParams['font.family'] = 'SimHei'
# # 1-3 x、y轴采样点的设置
# # 代表取100个值在0—5之间的数
# x = np.linspace(0, 5, 100)  # x轴的采样点
# # print('测试2--\n', x)  #设置测试的目的是为了分析和调试
# # 通过下面曲线加上噪声(随机生成)生成y轴的采样点y_data
# y = 2 * np.sin(x) + 0.3 * x ** 2
# # size=100代表取100个值
# y_data = y + np.random.normal(scale=0.3, size=100)
# # print('测试3--\n', y_data)  #设置测试的目的是为了分析和调试
# """
# 1-4 制作散点图的操作
# """
# # 1-4-1 散点图的文件名称和图表的标题设置
# plt.figure('散点图')  # figure()指定图标名称
# plt.title('散点图的一个示例')  # title()指定图标的标题
# # 1-4-2  绘制散点图
# # ' . '标明画散点图，每个散点的形状是一个个圆点来的
# plt.plot(x, y_data, '.')
# """
# 1-5 制作线形图的操作
# """
# # 1-5-1 线形图名称和标题
# plt.figure('线形图')  # figure()指定图标名称
# plt.title('线形图的一个示例')  # title()指定图标的标题
# # 1-5-2 绘制线型图
# # x,y代表x,y轴；
# # 'r - -'代表线是红色虚线，'k'代表黑色实线
# # lw=3, 代表线的宽度为3
# plt.plot(x, y, color='k', lw=3)
# """
# 1-6 制作散点图和线形图结合在一起的混合曲线
# """
# # 1-6-1 混合曲线名称和标题
# # figure()指定图标名称，将img1与img2混合在一起
# plt.figure('散点图 & 线形图')
# plt.title('混合图')  # title()指定图标的标题
# # 1-6-2 添加绘制的线形图
# plt.plot(x, y, color='r', lw=3)
# # 1-6-3 添加绘制的散点图（这种方式更方便）
# plt.scatter(x, y_data)
# # 1-7 将当前的figure图（混合图）保存到指定路径
# # 注意这里只能保存一个，需要的保存其他曲线图的，
# # 可以在其后面添加
# plt.savefig('hunhe.png')
# # 1-8 将图表显示在屏幕上
# plt.show()
#
# ################ 2. 2D图表—柱形图（条形图） ############
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.rcParams['font.family'] = 'SimHei'
# # 制作几部电影所获得的奥斯卡金像奖的数目
# # 2-1 建立x轴和y轴
# movies = ["Annie Hall", "Ben-hur", "Gasablanca", \
#           "Candhi", "West Side Story"]
# num = [5, 11, 3, 8, 10]
# # 2-2 设置y轴标志、条形图的标题和名称
# plt.figure('柱形图')
# plt.ylabel("获得的奥斯卡金像奖的数目")
# plt.title('最受欢迎de电影')
# # 2-3 条形的默认宽度是0.8，因此我们对左侧坐标加上0.1，
# # 这样每个条形就被放置在中心了
# xs = [i + 0.1 for i, _ in enumerate(movies)]
# # 2-4 使用电影的名字标记x轴，位置在x轴上条形的中心
# plt.xticks([i + 0.15 for i, _ in enumerate(movies)], movies)
# # 2-5 使用x坐标[xs]和高度[num]画条形图
# plt.bar(xs, num)
# # 2-6 展示条形图
# plt.show()
#
# ################ 3. 2D图表—饼形图 ############
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# # 3-1 设置字体样式,（中文黑体）
# mpl.rcParams['font.family'] = 'SimHei'
# # 3-2 随机产生5个在3—11之间的数据值，作为样本数据
# # 5个样本值，也就是说有5个饼块图
# data = np.random.randint(3, 11, 5)
# # print('测试---', data)
# # 3-3 设置饼图的名称和标题
# plt.figure('饼图练习')
# plt.title('欢迎关注【python是一个时代】')
# # 3-4 画一个饼图，自定义饼块的偏移量
# # 格式：pie(样本值，偏移量设置)
# plt.pie(data,explode=[0, 0.2, 0, 0, 0])
# # 3-5 将饼图显示在屏幕上
# plt.show()
#
# 显示中文的属性
"""
plt.rcParams['font.family'] = 'SimHei'
黑体  SimHei
微软雅黑    Microsoft YaHei
微软正黑体   Microsoft JhengHei
新宋体 NSimSun
新细明体    PMingLiU
细明体 MingLiU
标楷体 DFKai-SB
仿宋  FangSong
楷体  KaiTi
仿宋_GB2312   FangSong_GB2312
楷体_GB2312   KaiTi_GB2312
"""
# # 关于保存图标的问题：
# """
# 注意一个plt.savefig()只能保存一个图表，
# 需要的保存其他曲线图的，
# 可以在其后面一个个的添加
# plt.savefig('hunhe.png')
# """

# ############ 1.3D（三维）图表—立体柱形图（条形图） ###########
# # 1-1 导入模块
# import matplotlib.pyplot as plt
# import numpy as np
# # 导入3D三维绘图工具包
# from mpl_toolkits.mplot3d import Axes3D
# # 设置中文黑体字体，保证中文在图表中正常显示
# plt.rcParams['font.family'] = 'SimHei'
# # 1-2 创建Axes3D对象
# fig = plt.figure('3D（三维）图表—立体柱形图（条形图）')
# # 1-2-1 第一种创建方法（推荐，容易理解）
# ax = Axes3D(fig)
# # 1-2-2 第二种创建方法
# # ax = fig.add_subplot(111, projection='3d')
# # 1-3 自定义图标的标题
# ax.set_title('欢迎关注【python是一个时代】\n更多精彩内容等着你')
# # 1-4 （核心）立体柱形图的设置
# # zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
# for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
#     xs = np.arange(20)  # 1-4-1 生成x轴的值
#     print('测试点：xs', xs)  # 注意：为了分析和调试专用的
#     ys = np.random.rand(20) # 1-4-2 生成y轴的值
#     print('测试点：ys', ys)  # 注意：为了分析和调试专用的
#     cs = [c] * len(xs)  # 1-4-3 生成不同的颜色
#     print('测试点：cs', cs)  # 注意：为了分析和调试专用的
#     cs[0] = 'c'
#     # 1-4-4 bar()是生成柱形图的函数
#     ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
# # 1-5 设置x,y,z轴的标签
# ax.set_xlabel('【这是X轴】')
# ax.set_ylabel('【这是Y轴】')
# ax.set_zlabel('【Z轴】')
# # 1-6 将图表展示到屏幕
# plt.show()

################## 2. 3D图表—长方体 #######################
# 导入模块
import numpy as np
import matplotlib.pyplot as plt
# 2-1 导入3D三维绘图工具包
from mpl_toolkits.mplot3d import Axes3D
# 设置中文黑体字体，保证中文在图表中正常显示
plt.rcParams['font.family'] = 'SimHei'
# 2-2 创建Axes3D对象
fig = plt.figure('3D图表—长方体')
ax = Axes3D(fig)
# 自定义图标的标题
ax.set_title('欢迎关注【python是一个时代】\n更多精彩内容等着你')
# 2-3 随机生成2行100列的随机数
x, y = np.random.rand(2, 100) * 4
# print(x,'y\n\n', y)
# 2-4 创建直方图hist与随机bin(容器)内容：
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])
# print('测试--\n', hist,'\n\n\n', xedges, '\n',yedges)
# 2-5 从一个坐标向量xedges、yedges中返回一个坐标矩阵
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
# 2-6 将多个列表中的元素合成一个列表的元素
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
# print('xpos/ypos:\n', xpos,'\n\n\n', ypos)  # 为了分析而设置的输出
zpos = np.zeros_like(xpos)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()
# 2-7 bar3d是生成长方体的函数
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
# 2-8 将图表显示在屏幕上
plt.show()

################ 3. 3D图表—自定义图表：########################
# 导入模块
import numpy as np
import matplotlib.pyplot as plt
# 3-1 导入3D三维绘图工具包
from mpl_toolkits.mplot3d import Axes3D
# 设置中文黑体字体，保证中文在图表中正常显示
plt.rcParams['font.family'] = 'SimHei'
# 3-2 创建Axes3D对象
fig = plt.figure('3D图表')
ax = Axes3D(fig)
# 3-3 自定义图标的标题
ax.set_title('欢迎关注【python是一个时代】\n更多精彩内容等着你')
# 3-4 创建x,y,z轴的数据
# 生成[-6，6] 间隔0.25的数列，间隔越小，曲面越平滑
# 这里的数值影响图表的样子，可自定义
X = np.arange(-12, 12, 0.5)
Y = np.arange(-12, 12, 0.5)
# 格点矩阵，原来的x行向量向下复制len(y)此形成
X, Y = np.meshgrid(X, Y)
# 数组开平方处理
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
# 3-5 cmap指color map
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2, 2)
# 3-6 添加右侧的色卡条
# shrink表示整体收缩比例，aspect值越大，bar越窄
fig.colorbar(surf, shrink=0.6, aspect=8)
# 3-7 savefig('D:/文件夹/plot3d_ex.png',dpi=48)  # 可保存
# 3-8 将图表显示在屏幕上
plt.show()

################# 4. 3D图表
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
#
# fig = plt.figure(figsize=(16, 12))
# ax = fig.gca(projection="3d")
#
# # 准备数据
# x = np.arange(-5, 5, 0.25)  # 生成[-5，5] 间隔0.25的数列，间隔越小，曲面越平滑
# y = np.arange(-5, 5, 0.25)
# x, y = np.meshgrid(x, y)  # 格点矩阵，原来的x行向量向下复制len(y)此形成
# # len(y)*len(x)的矩阵，即为新的x矩阵；原来的y列向量向右复制len(x)次，形成
# # len(y)*len(x)的矩阵，即为新的y矩阵；新的x矩阵和新的y矩阵shape相同
# r = np.sqrt(x ** 2 + y ** 2)
# z = np.sin(r)
#
# surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)  # cmap指color map
#
# # 自定义z轴
# ax.set_zlim(-1, 1)
# ax.zaxis.set_major_locator(LinearLocator(20))  # z轴网格线的疏密，刻度的疏密，20表示刻度的个数
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # 将z的value子符串转为float，保留2位小数
#
# # 设置坐标轴的label和标题
# ax.set_xlabel('x', size=15)
# ax.set_ylabel('y', size=15)
# ax.set_zlabel('z', size=15)
# ax.set_title("Surface plot", weight='bold', size=20)
#
# # 添加右侧的色卡条
# fig.colorbar(surf, shrink=0.6, aspect=8)  # shrink表示整体收缩比例，aspect仅对bar的宽度有影响，
# # aspect值越大，bar越窄
# plt.show()

"""
# 行实现设置坐标标记点
ax.set_xticks([0,25,50,75,100]) 
# 设置图片的标题
ax.set_title('Demo Figure')
# 设置横轴的名称
ax.set_xlabel('Time')  # x轴标签
ax.set_ylabel('Time')  # y轴标签
"""
################## 画直方图 #####################
"""
matplotlib库中提供了一个画直方图的工具，它的常用参数如下
plt.hist(x, bins=None, range=None)
参数x代表要使用的数据，bins表示要划分区间数，range表示区间的范围

具体使用如下
import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(1000)#产生1000个正太分布的随机点
plt.hist(x=data,bins=100,range=(-5,5),label='aa')#在[-5,5]上划分100个区间
plt.show()


###################### 画散点图 ###################
# 注意参数要写成这种形式 color='blue'， 不能直接 'r'， 否则报错
plt.scatter(dataset_x, dataset_y, color='blue')  # 散点图
plt.show()
"""
