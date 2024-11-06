import matplotlib.pyplot as plt
import numpy as np

# Hs=1000,LS=100,m=2下的数据结果
# 数据
x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [0.3346, 0.3596, 0.3978, 0.4296, 0.4344, 0.4446, 0.4524, 0.4588, 0.4692, 0.4738, 0.4764]
for index,item in enumerate(y):
    y[index] = item/1.92
y_std_dev = [0.11127821, 0.092821549, 0.07396729, 0.094762018, 0.0749976, 0.088084278, 0.076721835, 0.070757049, 0.086829488, 0.077185232, 0.105009714]

y_ingress = [1.0977237066194991, 1.1154811740852555, 1.1205464913411256, 1.1071903511349197, 1.125908416958195, 1.1480300367723557, 1.152092389193359, 1.1310578296005083, 1.1282255821018616, 1.1186024097603953, 1.140006051680362]
ingress_std_dev = [0.2067739670004566, 0.23256703922700336, 0.21586550291113732, 0.23208594972455573, 0.2251098409309682, 0.25271660709127103, 0.22005260474346244, 0.2333665454338011, 0.22997508213700327, 0.2419169681466161, 0.22335300830511026]

y_two_sw = [0.83, 0.83, 0.81, 0.81, 0.82, 0.83, 0.82, 0.81, 0.82, 0.8, 0.82]

y_wang = [1.1206499318541296, 1.1296360737747784, 1.13120825053715, 1.1385414454424874, 1.165885293496788, 1.1139596244711205, 1.145172119560687, 1.146041630217974, 1.1140275929700416, 1.1270667382797384, 1.1103016817999343]


plt.figure(figsize=(10, 5), linewidth=6)
plt.errorbar(x, y, yerr=y_std_dev, fmt='_', capsize=4, markersize=4, color='red', ecolor='red')
plt.plot(x, y, marker='o', markersize=4, linestyle='-', color='r', label='Min-max_load()')

plt.errorbar(x, y_ingress, yerr=ingress_std_dev, fmt='_', capsize=4, markersize=4, color='blue', ecolor='blue')
plt.plot(x, y_ingress, marker='s', markersize=6, linestyle='-', color='blue', label='ingress-based')
plt.plot(x, y_two_sw, marker='v', markersize=6, linestyle='-', color='green', label='Min-max_load() with filtering-depth=2')

plt.plot(x, y_wang, marker='^', markersize=6, linestyle='-', color='purple', label='rule-based')

plt.xticks(fontsize=14, fontweight='bold')
plt.yticks([0.3, 0.6, 0.9, 1.2, 1.5, 1.8], ['30%', '60%', '90%', '120%', '150%', '180%'], fontsize=18, fontweight='bold')

# 设置图表标题和标签
plt.xlabel('Number of Border Service', fontsize=20, fontweight='bold')
plt.ylabel('Utilization(%)', fontsize=20, fontweight='bold')
plt.xlim(2, 12)

# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
