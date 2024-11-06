import matplotlib.pyplot as plt
import numpy as np

# Hs=1000,LS=100,m=2下的数据结果
# 数据
k=8000
end_time = k/815
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, end_time]
y_base = []
y_8 = []
y_16 = []
y_24 = []
y_28 = []
for index,item in enumerate(x):
    if index == len(x)-1:
        y_base.append(1)
        y_8.append(74 * end_time / k)
        y_16.append(118 * end_time / k)
        y_24.append(312 * end_time / k)
        y_28.append(555 * end_time / k)
        break
    y_base.append(815*item/k)
    y_8.append(74*item/k)
    y_16.append(118*item/k)
    y_24.append(312*item/k)
    y_28.append(555*item/k)




plt.figure(figsize=(10, 5),linewidth=6)
# plt.errorbar(x, y, yerr=std_dev, fmt='_', capsize=4, markersize=4, color='red', ecolor='red')
# plt.errorbar(x, y, yerr=[y_err_lower, y_err_upper], fmt='_', markersize=4, capsize=5, color='b', ecolor='r', elinewidth=2, capthick=2, label='Data with Error Bars')
plt.plot(x, y_base, marker='o', markersize=4, linestyle='-', color='r', label='ingress-based')
plt.plot(x, y_8, marker='p', markersize=8, linestyle='-', color='blue', label='delegated 8 bits')
plt.plot(x, y_16, marker='s', markersize=8, linestyle='-', color='blue', label='delegated 16 bits')
plt.plot(x, y_24, marker='*', markersize=8, linestyle='-', color='blue', label='delegated 24 bits')
plt.plot(x, y_28, marker='h', markersize=8, linestyle='-', color='blue', label='delegated 28 bits')



plt.xticks(fontsize=14, fontweight='bold')
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ['20%', '40%', '60%', '80%','100%'],fontsize=18, fontweight='bold')

# 设置图表标题和标签
plt.xlabel('Attack duration(seconds)',fontsize=20,fontweight='bold')
plt.ylabel('Table fill rate(%)',fontsize=20,fontweight='bold')
plt.xlim(0.8, 9.3)

# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
