import matplotlib.pyplot as plt
import numpy as np

# Hs=1000,LS=100,m=2下的数据结果
# 数据
x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.3978, 0.421, 0.4556, 0.4612, 0.494, 0.4982, 0.5082, 0.5194, 0.5572]
for index,item in enumerate(y):
    y[index] = item/1.92
y_std_dev = [0.07396729, 0.094588583, 0.081514661, 0.079990999, 0.071916618, 0.099119927, 0.083191105, 0.072191689, 0.079146447]

y_ingress = [1.0992223901734226, 1.1168010635612726, 1.1241817090409758, 1.1569524139098375, 1.1071404520143495, 1.1134850986772018, 1.1413604740265375, 1.126612330695611, 1.1406407716603968]
ingress_std_dev = [0.21652401624611445, 0.21992084808095838, 0.24478229047557185, 0.24803140556185646, 0.213106693455983, 0.22959623545722108, 0.23719970539801863, 0.22282657426635488, 0.22202475827903062]

y_two_sw = [0.82, 0.81, 0.83, 0.81, 0.82, 0.83, 0.82, 0.81, 0.83]

y_wang = [1.129850779807684, 1.1280357060483885, 1.1378113147848503, 1.1396105415049955, 1.1339511036164056, 1.1432855616392563, 1.1531590825480158, 1.0773685097879544, 1.131971193503169]



plt.figure(figsize=(10, 5), linewidth=6)
plt.errorbar(x, y, yerr=y_std_dev, fmt='_', capsize=4, markersize=4, color='red', ecolor='red')
plt.plot(x, y, marker='o', markersize=4, linestyle='-', color='r', label='Min-max_load()')

plt.errorbar(x, y_ingress, yerr=ingress_std_dev, fmt='_', capsize=4, markersize=4, color='blue', ecolor='blue')
plt.plot(x, y_ingress, marker='s', markersize=6, linestyle='-', color='blue', label='ingress-based')
# plt.plot(x, y_one_sw, marker='^', markersize=8, linestyle='-', color='blue', label='Min-max_load() with filtering-depth=1')
plt.plot(x, y_two_sw, marker='v', markersize=6, linestyle='-', color='green', label='Min-max_load() with filtering-depth=2')

plt.plot(x, y_wang, marker='^', markersize=6, linestyle='-', color='purple', label='rule-based')

plt.xticks(fontsize=14, fontweight='bold')
plt.yticks([0.3, 0.6, 0.9, 1.2, 1.5, 1.8], ['30%', '60%', '90%', '120%', '150%', '180%'], fontsize=18, fontweight='bold')

# 设置图表标题和标签
plt.xlabel('New links', fontsize=20, fontweight='bold')
plt.ylabel('Utilization(%)', fontsize=20, fontweight='bold')
plt.xlim(2, 10)

# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
