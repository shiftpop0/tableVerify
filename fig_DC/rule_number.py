import matplotlib.pyplot as plt

# x = [118, 467, 2013, 5212, 9586, 17906, 37811, 137637, 281402, 1240243]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [15.9684685, 15.982222, 15.986154, 15.980337, 15.973837, 15.969805, 15.9753585, 15.9775715, 15.9886405, 15.9799635]

# y_ingress = [31.936937, 31.964444, 31.972308, 31.960674, 31.947674, 31.93961, 31.950717, 31.955143, 31.977281, 31.959927]
# y_ingress = [item - 15.8 for item in y_ingress]

y_wang = [31.93984418, 31.96490961, 31.96856683, 31.95962808, 31.94537014, 31.93837538, 31.94926508, 31.95477292, 31.97, 31.96]
y_wang = [item - 15.805 for item in y_wang]

y_wang_std_dev = [0.003021658, 0.002223133, 0.001757682, 0.002892279, 0.002628366, 0.003015894, 0.003358768, 0.000384976, 0, 0]

plt.figure(figsize=(10, 5), linewidth=6)
plt.plot(x, y, marker='o', markersize=4, linestyle='-', color='r', label='bit-based')
# plt.plot(x, y_ingress, marker='s', markersize=6, linestyle='-', color='blue', label='ingress-based')
plt.plot(x, y_wang, marker='^', markersize=6, linestyle='-', color='purple', label='openflow-rule-based')
# plt.errorbar(x, y_wang, yerr=y_wang_std_dev, fmt='_', capsize=4, markersize=4, color='purple', ecolor='blue')

# axes = plt.axes()
plt.xticks(fontsize=14, fontweight='bold')
# plt.yticks([0.5, 1.0, 1.5, 2.0,2.5], ['50%', '100%', '150%', '200%','250%'],fontsize=18, fontweight='bold')
plt.yticks([16, 16.18], ['16', '32'], fontsize=18, fontweight='bold')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['118', '467', '2013', '5212', '9586', '17906', '37811', '137637', '281402', '1240243'], fontsize=18, fontweight='bold', rotation=45)

# 设置图表标题和标签
plt.xlabel('Rule Number', fontsize=20, fontweight='bold')
plt.ylabel('Average ASL(times)', fontsize=20, fontweight='bold')
plt.ylim(15.9, 16.3)
# 获取图的边框对象并设置粗细
for spine in plt.gca().spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2
# 添加图例
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.gca().set_facecolor(None)
plt.savefig('C:/Users/Administrator/OneDrive/吴欣泽/Paper/数据中心版/Fig1/'+'rule_number.png', transparent=True)
plt.show()
