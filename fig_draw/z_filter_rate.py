import matplotlib.pyplot as plt
import numpy as np

# Hs=1000,LS=100,m=2下的数据结果
# 数据
k=8000
x = [200, 433, 736, 1172]

#         8.54
y_base = [1,1,1,9945/9999]
y=[1,1,1,1]




plt.figure(figsize=(10, 5),linewidth=6)
# plt.errorbar(x, y, yerr=std_dev, fmt='_', capsize=4, markersize=4, color='red', ecolor='red')
# plt.errorbar(x, y, yerr=[y_err_lower, y_err_upper], fmt='_', markersize=4, capsize=5, color='b', ecolor='r', elinewidth=2, capthick=2, label='Data with Error Bars')
plt.plot(x, y_base, marker='o', markersize=4, linestyle='-', color='r', label='ingress-based')
plt.plot(x, y, marker='p', markersize=8, linestyle='-', color='blue', label='bit-based ')



plt.xticks(fontsize=14, fontweight='bold')
plt.yticks([0.9, 1.0,1.1], ['90%', '100%','110%'],fontsize=18, fontweight='bold')

# 设置图表标题和标签
plt.xlabel('Attack speed(packets/seconds)',fontsize=20,fontweight='bold')
plt.ylabel('Filter rate(%)',fontsize=20,fontweight='bold')
plt.xlim(100, 1200)

# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
