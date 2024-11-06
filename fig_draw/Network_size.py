import matplotlib.pyplot as plt
import numpy as np

# Hs=1000,LS=100,m=2下的数据结果
# 数据
x = [100, 150, 200, 250, 300, 350, 400, 450, 500]

y = [0.3978, 0.3948, 0.3742, 0.3704, 0.3464, 0.3406, 0.3126, 0.3072, 0.3]
for index, item in enumerate(y):
    y[index] = item / 1.92

y_std_dev = [0.07396729, 0.090801762, 0.103471542, 0.080621585, 0.082795169, 0.109488082, 0.107094538, 0.085628033, 0.070823725]

y_ingress = [1.1760648050574167, 1.1566723950520845, 1.1294032515120416, 1.1342361199281623, 1.1333241317296636, 1.1124636816123865, 1.128032402873859, 1.1407390112320963, 1.1302971159284025]
ingress_std_dev = [0.22713153851940235, 0.22882846922216885, 0.22336521430766024, 0.23177002080853829, 0.2282732914613301, 0.21919631468612313, 0.2376520540576475, 0.2263900199737081, 0.2209993075210522]

y_two_sw = [0.83, 0.83, 0.81, 0.81, 0.82, 0.83, 0.82, 0.81, 0.82]

y_wang = [1.1625516107481453, 1.12458519044094, 1.1306986355291313, 1.1802433692149454, 1.117990305615932, 1.1162418858637395, 1.1227091395645585, 1.1469082007982971, 1.1484042437952495]
wang_std_dev = [0.2546944736911106, 0.2279729795513224, 0.227195167188799, 0.2295162790289934, 0.22487431595975998, 0.24187705938544327, 0.2515975320623965, 0.23059563358701515, 0.24443939651843294]

plt.figure(figsize=(10, 5), linewidth=6)
plt.errorbar(x, y, yerr=y_std_dev, fmt='_', capsize=4, markersize=4, color='red', ecolor='red')
# plt.errorbar(x, y, yerr=[y_err_lower, y_err_upper], fmt='_', markersize=4, capsize=5, color='b', ecolor='r', elinewidth=2, capthick=2, label='Data with Error Bars')
plt.plot(x, y, marker='o', markersize=4, linestyle='-', color='r', label='Min-max_load()')

plt.errorbar(x, y_ingress, yerr=ingress_std_dev, fmt='_', capsize=4, markersize=4, color='blue', ecolor='blue')
plt.plot(x, y_ingress, marker='s', markersize=6, linestyle='-', color='blue', label='ingress-based')
# plt.plot(x, y_one_sw, marker='^', markersize=8, linestyle='-', color='blue', label='Min-max_load() with filtering-depth=1')
plt.plot(x, y_two_sw, marker='v', markersize=6, linestyle='-', color='green', label='Min-max_load() with filtering-depth=2')

plt.plot(x, y_wang, marker='^', markersize=6, linestyle='-', color='purple', label='rule-based')

plt.xticks(fontsize=14, fontweight='bold')
plt.yticks([0.3, 0.6, 0.9, 1.2, 1.5, 1.8], ['30%', '60%', '90%', '120%', '150%', '180%'], fontsize=18, fontweight='bold')

# 设置图表标题和标签
plt.xlabel('Network size', fontsize=20, fontweight='bold')
plt.ylabel('Utilization(%)', fontsize=20, fontweight='bold')
plt.xlim(100, 500)
plt.gca().invert_xaxis()
# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
