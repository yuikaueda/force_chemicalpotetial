import numpy as np
import matplotlib.pyplot as plt

# 定数の設定
r = 0.5 #自然増加率
k = 60 #収容数
N_0 = 0 #初期数

A = 0.01 #エントロピー弾性

a = r / (2*k)
b = N_0 - k

# xの範囲を設定
x = np.linspace(0, 100, 1000)

# yの値を計算
y1 = -r*x*(k-N_0) / np.exp(a*x**2) / k + A*x  #力
y2 = -r*(k-N_0) / np.exp(a*x**2) / k + A #ヤング率
y3 = (k*np.exp(a*x**2) + b) / np.exp(a*x**2) #N

# プロット
plt.plot(x, y2, color='k')

# 軸のラベルとタイトルを設定
plt.xlabel('l',fontsize=20)
plt.ylabel('E',fontsize=20)
#plt.title('Plot of y = L*(exp(rL^2)+b)/(exp(L^2))')

# グリッドを表示
#plt.grid()
plt.xticks([])
plt.yticks([])

plt.savefig('negative_Evsl.png')
# プロットを表示
plt.show()

