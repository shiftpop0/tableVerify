import matplotlib.pyplot as plt
import numpy as np

x = [2,3,4,5,6,7,8,9,10]

y = [0.8770128932902079, 0.4178525897651371, 0.21069524850165916, 0.10448727907103848, 0.05379533244244419, 0.028151173008519527, 0.014363003860515344, 0.007435925494414433, 0.0038269715943987826]
y_std_dev = [0.15985823804308785, 0.08847833010993786, 0.032740323320885695, 0.013227597281502657, 0.004815249572893598, 0.002564641374212603, 0.0010516397432553943, 0.0004745001546967338, 0.00020484950698374327]

y_wang = [1.9979634437468923, 1.9579440466566373, 1.9715315423615476, 1.8611362744980724, 1.954740531150638, 1.9678952074509428, 1.9294977229576071, 2.0046912169274322, 1.9488644241696798]
wang_std_dev = [0.37062502799323127, 0.40540839359744896, 0.3992336513806417, 0.34673145162143704, 0.3999501897294283, 0.4049849103907228, 0.3862154555084688, 0.4365376607399371, 0.400702397782545]

y_single = [1.9827974331701899, 2.010093317750802, 1.98460866028152, 2.0129743507301843, 2.103996103516774, 1.9715574699522185, 1.9324498501928014, 1.9736140725181397, 1.9446780287216894]
y_single_std_dev = [0.4590317027903051, 0.3949857301224559, 0.3857119237347334, 0.38923827380051734, 0.4148562355138232, 0.42002624045694453, 0.43049302181072696, 0.39516036909089564, 0.4095132396588078]

plt.figure(figsize=(10, 5), linewidth=6)
plt.plot(x, y, marker='o', markersize=4, linestyle='-', color='r', label='bit-based()')
plt.errorbar(x, y, yerr=y_std_dev, fmt='_', capsize=4, markersize=4, color='red', ecolor='red')

plt.plot(x, y_wang, marker='^', markersize=6, linestyle='-', color='purple', label='rule-based')
plt.errorbar(x, y_wang, yerr=wang_std_dev, fmt='_', capsize=4, markersize=4, color='purple', ecolor='purple')

plt.plot(x, y_single, marker='s', markersize=6, linestyle='-', color='blue', label='single switch')
plt.errorbar(x, y_single, yerr=y_single_std_dev, fmt='_', capsize=4, markersize=4, color='blue', ecolor='blue')

plt.xticks(fontsize=14, fontweight='bold')
plt.yticks([0.5, 1.0, 1.5, 2.0, 2.5], ['50%', '100%', '150%', '200%', '250%'], fontsize=18, fontweight='bold')

# 设置图表标题和标签
plt.xlabel('High', fontsize=20, fontweight='bold')
plt.ylabel('Max Load(%)', fontsize=20, fontweight='bold')
plt.xlim(2, 10)
# plt.gca().invert_xaxis()
# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.gca().set_facecolor(None)
plt.savefig('C:/Users/Administrator/OneDrive/吴欣泽/Paper/数据中心版/Fig1/'+'Tree_high.png', transparent=True)
plt.show()