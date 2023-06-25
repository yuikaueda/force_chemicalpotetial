import numpy as np
import math
import matplotlib.pyplot as plt

#定数の設定
k = 1.38e-23 #ボルツマン定数
a = 1 #ゴム曲がりの幅

mb = 600 #βアクチン数
MB = 100 #αSMAの収束値
r = 0.01 #自然増加率
mb0 = 1 #初期結合数

N = mb
Na = N*a

x = np.linspace(0, 500, 1000)

#ゴムモデルエントロピー
S1 = k*N*(np.log(2)-1/2*(1+x/Na)*np.log(1+x/Na)-1/2*(1-x/Na)*np.log(1-x/Na))

#介入エントロピー
rMB = r/(2*MB)
def ma(x, MB, rMB, mb0): 
    return (MB*np.exp(rMB*x**2) - MB + mb0)/np.exp(rMB*x**2)

M = ma(x, MB, rMB, mb0) + mb

S2 = k*(M*np.log(M) - ma(x, MB, rMB, mb0)*np.log(ma(x, MB, rMB, mb0)) - mb*np.log(mb))

S = S1 + S2

plt.plot(x, S1, label='S1', color='red')
plt.plot(x, S2, label='S2', color='blue')
plt.plot(x, S, label='Stotal', color='black')

plt.xlabel('l',fontsize=20)
plt.ylabel('S',fontsize=20)

plt.savefig('paturn2_entropy_SS1S2.png')

plt.legend()
plt.show()
