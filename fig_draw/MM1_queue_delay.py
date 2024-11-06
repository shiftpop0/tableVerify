import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(104.01, 154.01, 100000)
Np = 100000
y_ingress = 1 * 1000 /((x-104) * Np)

y = 3 * 1000 /((x-28) * Np)

plt.figure(figsize=(10, 5), linewidth=6)
plt.plot(x, y_ingress, label='ingress-based')
plt.plot(x, y, label='bit-based distributed', linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5)  # 添加 y 轴
plt.axhline(0, color='gray', linewidth=0.5)  # 添加 x 轴
plt.xlim(104, 154.01)
# plt.ylim(1/10**2, 10**4)

# 设置y轴刻度为对数刻度
plt.yscale('log')
plt.yticks(fontsize=10, fontweight='bold')
plt.xticks([104,114,124,134,144,154],fontsize=10, fontweight='bold')
plt.legend()
# plt.title('M/M/1')
plt.xlabel('Capacity(Bits)', fontsize=16, fontweight='bold')
plt.ylabel('Total Delay(ms)', fontsize=16, fontweight='bold')

plt.grid(True)
plt.show()