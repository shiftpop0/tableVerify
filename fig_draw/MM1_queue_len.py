import numpy as np
import matplotlib.pyplot as plt


# x = np.linspace(0.1, 0.9999, 1000000)  # ρ ∈ (0,1)
cap = np.linspace(104.01, 154.01, 100000)
x_ingress = 104/cap
y_ingress = (x_ingress**2) / (1-x_ingress)

x = 29/cap #28 28 11
y = (x**2) / (1-x)

plt.figure(figsize=(10, 5), linewidth=6)
plt.plot(cap, y_ingress, label='ingress-based')
plt.plot(cap, y, label='bit-based distributed',linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5)  # 添加 y 轴
plt.axhline(0, color='gray', linewidth=0.5)  # 添加 x 轴
plt.xlim(104,154.01)
# plt.ylim(1/10**2, 10**4)

# 设置y轴刻度为对数刻度
plt.yscale('log')
plt.yticks(fontsize=10, fontweight='bold')
plt.xticks([104,114,124,134,144,154],fontsize=10, fontweight='bold')
# 设置y轴刻度的基数为10
# plt.yticks([10**i for i in range(0, 5)])
# plt.yticks([10**i for i in range(-1, 5)], ['10^-1','10^0', '10^1', '10^2', '10^3', '10^4'], fontsize=10, fontweight='bold')
# plt.ylim(0.001,100)
plt.legend()
# plt.title('M/M/1')
plt.xlabel('Capacity(Bits)', fontsize=16, fontweight='bold')
plt.ylabel('Number of Waiting in Queue', fontsize=16, fontweight='bold')

plt.grid(True)
plt.show()