#統計学は最強の学問である（数学編）の46.8式の実装と可視化
import numpy as np
import matplotlib.pyplot as plt

# シグモイド
# a:定数
# b:係数
# x:入力
def sigmoid(a, b, x):
    return 1 / (1 + np.exp(-(a+b*x)))

xlist = np.arange(0, 4, 0.001)
ylist = []
for x in xlist:
    y = -1.1 + sigmoid(-4.5, 1.3, x) + sigmoid(35.4, -8.8, x) + 0.1 * sigmoid(110.4, -46, x) + 0.1 * sigmoid(-119.6, 46, x)
    ylist.append(y)

plt.plot(xlist, ylist)
plt.show()