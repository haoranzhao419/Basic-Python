import matplotlib.pyplot as pit
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(3*x)
pit.scatter(x, y)
pit.plot(x, np.sin(x), "r-o",
         x, np.sin(2*x), "c-->")
z = np.random.randn(1000)   # 生成1000个随机数，绘制这1000个随机数的分布
pit.hist(z, 50)  # 一共有五十个条状
pit.show()
