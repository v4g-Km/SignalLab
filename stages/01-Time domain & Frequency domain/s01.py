# s01 waveform

import numpy as np
import matplotlib.pyplot as plt

# 让 matplotlib 能显示中文（macOS 用苹方等字体）
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Hiragino Sans GB', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False   # 负号正常显示

# 三要素
A = 2
f = 1
phi = 0

# 建横坐标
t = np.linspace(0,1,1000)
# 建纵坐标
y = A*np.sin(2*np.pi*f*t + phi) # 1Hz的正弦波


plt.plot(t,y)
plt.axhline(color="gray")
plt.xlabel("时间 t （秒）")
plt.ylabel("幅值")
plt.title(f"正弦波：{f}Hz")
plt.grid(True)
plt.show()