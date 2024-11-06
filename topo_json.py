import matplotlib.pyplot as plt
import networkx as nx
import random
from graphviz import Digraph

class Node:
    def __init__(self, value, cap=50):
        self.value = value
        self.children = []
        self.cap = cap
        self.level_index = 0
        self.brv = 0

    def add_child(self, node):
        self.children.append(node)

    # 先序遍历
    def preorder_traversal(self, queue=[]):
        # print(self.value)
        queue.append(self)
        for child in self.children:
            child.preorder_traversal(queue)

    # 后序遍历
    def postorder_traversal(self, queue=[]):
        for child in self.children:
            child.postorder_traversal(queue)
        # print(self.value)
        queue.append(self)

    def level_traverse(self):
        queue = [self]
        k = 0
        while (len(queue)):
            node = queue.pop(0)
            node.level_index = k  # 层序
            k = k + 1
            # print(node.value)
            for child in node.children:
                queue.append(child)
        print("生成树节点数量:"+str(k),end=", ")
        return k

    def search_node(self, value):
        list = []
        self.postorder_traversal(list)
        for item in list:
            if item.value == value:
                return item
        return


def get_parent_node(root, node):
    if not node or root == node:
        return None  # 结点不存在或者为根节点，返回None表示不存在父节点
    queue = [root]
    while (len(queue)):
        n = queue.pop(0)
        for child in n.children:
            if child == node:  # 当前孩子节点等于查询结点
                return n
            else:
                queue.append(child)
    return None  # 左右子树中都未找到父节点，返回None表示不存在父节点s


def draw_tree(root):
    dot = Digraph()
    queue = [root]
    while (len(queue)):
        node = queue.pop(0)
        dot.node(str(id(node)), str(node.value) + ', ' + str(node.brv))
        for child in node.children:
            queue.append(child)
    queue = [root]
    while (len(queue)):
        node = queue.pop(0)
        for child in node.children:
            dot.edge(str(id(node)), str(id(child)))
            queue.append(child)
    return dot

def brite_read():
    # 标志以确定当前正在处理的部分是Nodes还是Edges
    is_nodes_section = False
    is_edges_section = False
    nodes_data=[]
    edges_data=[]
    with open('C:/Users/Administrator/Pictures/算法实验结果/100node.brite', 'r') as file:
        content = file.readlines()
    for line in content:
        if "Nodes:" in line:
            is_nodes_section = True
            is_edges_section = False
        elif "Edges:" in line:
            is_nodes_section = False
            is_edges_section = True
        elif is_nodes_section and 'RT_NODE' in str(line):
            nodes_data.append(line)
        elif is_edges_section and not line.strip().startswith("("):
            # 如果在Edges部分且行不以'('开头，则将其添加到Edges列表中
            edges_data.append(line)
    return nodes_data,edges_data



def get_topo_zoo():
    Lhasa = Node('s1')
    Lanzhou = Node('s2')
    Kashi = Node('s3')
    Shiquanhe = Node('s4')
    Jinan = Node('s5')
    Qingdao = Node('s6')
    Taiyuan = Node('s7')
    Shilazhuang = Node('s8')
    Shanghai = Node('s9')
    Suzhou = Node('s10')
    InternationalLink1 = Node('s11')
    InternationalLink2 = Node('s12')
    Nanning = Node('s13')
    Changsha = Node('s14')
    Guiyang = Node('s15')
    Chongqing = Node('s16')
    Chengdu = Node('s17')
    Kunming = Node('s18')
    Xian = Node('s19')
    Zhengzhou = Node('s20')
    InternationalLink4 = Node('s21')
    InternationalLink3 = Node('s22')
    Haikou = Node('s23')
    HongKong = Node('s24')
    Hangzhou = Node('s25')
    Wuhan = Node('s26')
    Hefei = Node('s27')
    Nanjing = Node('s28')
    Guangzhou = Node('s29')
    Xiamen = Node('s30')
    Fuzhou = Node('s31')
    Nandhang = Node('s32')
    Xining = Node('s33')
    Urumqi = Node('s34')
    Harbin = Node('s35')
    Changchun = Node('s36')
    Shenyang = Node('s37')
    Dalian = Node('s38')
    Tianjin = Node('s39')
    Beijing = Node('s40')
    Hohhot = Node('s41')
    Yinchuan = Node('s42')

    # 建立父子关系
    Lhasa.add_child(Chengdu)
    Lhasa.add_child(Shiquanhe)
    Lhasa.add_child(Beijing)
    Lanzhou.add_child(Xian)
    Lanzhou.add_child(Beijing)
    Kashi.add_child(Urumqi)
    Jinan.add_child(Shanghai)
    Qingdao.add_child(Tianjin)
    Taiyuan.add_child(Xian)
    Taiyuan.add_child(Beijing)
    Shilazhuang.add_child(Beijing)
    Shanghai.add_child(Tianjin)
    Shanghai.add_child(Beijing)
    Shanghai.add_child(Suzhou)
    Shanghai.add_child(InternationalLink2)
    Shanghai.add_child(Chengdu)
    Shanghai.add_child(Xian)
    Shanghai.add_child(HongKong)
    Shanghai.add_child(Hangzhou)
    Shanghai.add_child(Wuhan)
    Shanghai.add_child(Hefei)
    Shanghai.add_child(Nanjing)
    Shanghai.add_child(Guangzhou)
    Shanghai.add_child(Nandhang)
    Suzhou.add_child(Nanjing)
    InternationalLink1.add_child(Beijing)
    Nanning.add_child(Guangzhou)
    Changsha.add_child(Wuhan)
    Guiyang.add_child(Chengdu)
    Guiyang.add_child(Guangzhou)
    Chongqing.add_child(Chengdu)
    Chongqing.add_child(Guangzhou)
    Chengdu.add_child(Nanjing)
    Chengdu.add_child(Guangzhou)
    Kunming.add_child(Guangzhou)
    Xian.add_child(Xining)
    Xian.add_child(Urumqi)
    Xian.add_child(Yinchuan)
    Xian.add_child(Beijing)
    Xian.add_child(Hohhot)
    Xian.add_child(Wuhan)
    Xian.add_child(Nanjing)
    Xian.add_child(Guangzhou)
    Zhengzhou.add_child(Beijing)
    InternationalLink4.add_child(HongKong)
    InternationalLink3.add_child(Guangzhou)
    Haikou.add_child(Wuhan)
    Haikou.add_child(Guangzhou)
    HongKong.add_child(Guangzhou)
    HongKong.add_child(Beijing)
    Wuhan.add_child(Beijing)
    Wuhan.add_child(Nanjing)
    Nanjing.add_child(Beijing)
    Nanjing.add_child(Fuzhou)
    Guangzhou.add_child(Tianjin)
    Guangzhou.add_child(Beijing)
    Guangzhou.add_child(Xiamen)
    Xining.add_child(Beijing)
    Urumqi.add_child(Beijing)
    Harbin.add_child(Beijing)
    Changchun.add_child(Beijing)
    Shenyang.add_child(Beijing)
    Dalian.add_child(Tianjin)
    Tianjin.add_child(Beijing)
    Beijing.add_child(Hohhot)
    Beijing.add_child(Yinchuan)
    draw_tree(Lhasa).render('./GV/tree.gv', view=True)




if __name__ == '__main__':
    brite_read()