from graphviz import Digraph
import topo_json
import networkx as nx
import pandas as pd
import numpy as np
import random

S = "生成树节点数量"


class Node:
    def __init__(self, value, cap=None, traffic_ratio=None):
        self.value = value
        self.children = []
        self.cap = cap if cap is not None else random.randint(100, 200)
        self.level_index = 0
        self.brv = 0
        self.load = 0
        self.traffic_ratio = traffic_ratio if traffic_ratio is not None else 1
        self.traffic_tmp_count = 0  # 临时存储流量数量，用来计算traffic_ratio

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
        print(S + ":" + str(k), end=", ")
        return k

    def search_node(self, value):
        list = []
        self.postorder_traversal(list)
        for item in list:
            if item.value == value:
                return item
        return


def traffic_set(node: Node):
    queue = []
    node.postorder_traversal(queue)
    for node_item in queue:
        if not node_item.children:
            node_item.traffic_tmp_count = random.randint(1, 100)
            # node_item.traffic_tmp_count = 1
        else:
            for child in node_item.children:
                node_item.traffic_tmp_count += child.traffic_tmp_count
    total_traffic = node.traffic_tmp_count
    for node_item in queue:
        node_item.traffic_ratio = node_item.traffic_tmp_count / total_traffic


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
    while len(queue):
        node = queue.pop(0)
        dot.node(str(id(node)), str(node.value) + ', ' + '{:.2f}%'.format(node.load * 100) + ', ' + str(node.brv) + '/' + str(node.cap) + ',' + '{:.2f}%'.format(node.traffic_ratio * 100))
        # dot.node(str(id(node)), str(node.value) + ', ' + 'load {:.2f}%'.format(node.load * 100) + ', ' + 'traffic {:.2f}%'.format(node.traffic_ratio*100))
        for child in node.children:
            queue.append(child)
    queue = [root]
    while len(queue):
        node = queue.pop(0)
        for child in node.children:
            dot.edge(str(id(node)), str(id(child)))
            queue.append(child)
    return dot


def draw_multi_ingress(root_list):
    dot = Digraph()
    queue = root_list.copy()
    visit = set()
    for item in queue:
        visit.add(item.value)
    while len(queue):
        node = queue.pop(0)
        # dot.node(str(id(node)), str(node.value) + ', ' + '{:.2f}%'.format(node.load * 100) + ', ' + str(node.brv) + '/' + str(node.cap) + ',' + '{:.2f}%'.format(node.traffic_ratio * 100))
        dot.node(str(id(node)), str(node.value))
        for child in node.children:
            if child.value not in visit:
                visit.add(child.value)
                queue.append(child)
    queue = root_list.copy()
    visit = set()
    for item in queue:
        visit.add(item.value)
    while len(queue):
        node = queue.pop(0)
        for child in node.children:
            dot.edge(str(id(node)), str(id(child)))
            if child.value not in visit:
                visit.add(child.value)
                queue.append(child)
    return dot


def Opt_Cover(tree):
    T_r = 128
    W_a = 1
    W_b = 9
    W_c = 10
    total = T_r * 2 + 3
    stack = []
    tree.level_traverse()
    tree.preorder_traversal(stack)
    OM = [[0 for i in range(total + 1)] for i in range(len(stack))]
    OJM = [[[0 for i in range(total + 1)] for i in range(total + 1)] for i in range(len(stack))]
    NM = [[0 for i in range(total + 1)] for i in range(len(stack))]
    while stack:
        v = stack.pop()
        for i in range(total + 1):  # 3代表两次端口号 一次协议号
            lam1 = 0  # 是否check 端口号
            lam2 = 0  # 是否check 协议号
            if len(v.children) == 0:
                if i >= 1:
                    lam2 = 1
                if i > 2:
                    lam1 = 2
                elif i == 2:
                    lam1 = 1
                OM[v.level_index][i] = ((((i - 3) if i > 3 else 0) * W_a + W_b * lam1 + W_c * lam2) / v.cap) * v.traffic_ratio
                NM[v.level_index][i] = i
            else:
                for j in range(0, i + 1):
                    lam2 = 1 if j == total else 0
                    lam1 = min(j - i + 3 if j - i + 3 > 0 else 0, 2)  # min用来限制最大为2
                    OJM[v.level_index][i][j] = (((j - lam1 - lam2) * W_a + W_b * lam1 + W_c * lam2) / v.cap) * v.traffic_ratio
                    for u in v.children:
                        if u is not None:
                            OJM[v.level_index][i][j] = max(OJM[v.level_index][i][j], OM[u.level_index][i - j])
                OJM_min_index = 0
                for j in range(0, i + 1):
                    if OJM[v.level_index][i][j] < OJM[v.level_index][i][OJM_min_index]:
                        OJM_min_index = j
                OM[v.level_index][i] = OJM[v.level_index][i][OJM_min_index]
                NM[v.level_index][i] = OJM_min_index
                # print(i)
    # stack = []
    tree.postorder_traversal(stack)
    len_brv = [0 for i in range(len(stack))]
    if OM[0][total] <= 1:
        while stack:
            v = stack.pop()
            tmp_node = get_parent_node(tree, v)
            if tmp_node is None:
                v.brv = NM[v.level_index][total]
                len_brv[v.level_index] = v.brv
                if len_brv[v.level_index] <= total - 3:
                    v.load = v.brv / v.cap
                elif len_brv[v.level_index] <= total - 1:
                    port_bit = (len_brv[v.level_index] - T_r * 2)
                    v.load = (v.brv - port_bit + port_bit * W_b) / v.cap
                else:
                    v.load = (v.brv - 3 + 2 * W_b + W_c) / v.cap
                v.load = v.load * v.traffic_ratio
            else:
                v.brv = NM[v.level_index][total - len_brv[tmp_node.level_index]]
                len_brv[v.level_index] = v.brv + len_brv[tmp_node.level_index]
                if len_brv[v.level_index] <= total - 3:
                    v.load = v.brv / v.cap
                elif len_brv[v.level_index] <= total - 1:
                    port_bit = len_brv[v.level_index] - T_r * 2
                    ip_bit = 0 if v.brv - port_bit < 0 else v.brv - port_bit
                    v.load = (ip_bit + port_bit * W_b) / v.cap
                else:
                    ip_bit = 0 if v.brv - 3 < 0 else v.brv - 3
                    port_bit = 0 if v.brv - ip_bit - 1 < 0 else v.brv - ip_bit - 1
                    v.load = (ip_bit + port_bit * W_b + W_c) / v.cap
                v.load = v.load * v.traffic_ratio

    # max_load = 0

    tree.preorder_traversal(stack)
    # while stack:
    #     v = stack.pop()
    #     # if len_brv[v.level_index] <= T_r * 2:
    #     #     v_load = v.brv / v.cap
    #     # else:
    #     #     over_bit=len_brv[v.level_index]-T_r * 2
    #     #     # v_load=
    #     parent=get_parent_node(tree, v)
    #     if parent is None:
    #         v_load=OM[0][total]
    #     else:
    #         v_load=OM[parent][total-len_brv[v.level_index]]
    #     max_load = v_load if v_load > max_load else max_load

    # print("minimax负载:" + str(OM[0][total]), end=", ")
    return OM[0][total]


def find_leaf_depths(tree, node, leaf_depths, depth=0):
    # 如果当前节点是叶子节点，则记录其深度
    if len(node.children) == 0:
        leaf_depths[node] = max(depth, leaf_depths[node] if node in leaf_depths else 0)
    else:
        # 否则，继续深度优先搜索
        for child in node.children:
            find_leaf_depths(tree, child, leaf_depths, depth + 1)


def main_brite():
    leaf_depths = {}
    nodes, links = topo_json.brite_read()
    ingress = 's' + str(random.randint(0, 100))
    # print("ingress:"+ingress)
    root = Node(ingress)

    visited = set()
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        visited.add(current_node.value)
        # 广度优先遍历

        for link in links:
            if link[0] == current_node.value and link[1] not in visited:
                visited.add(link[1])
                child_node = Node(link[1])
                current_node.add_child(child_node)
                queue.append(child_node)

    # 随机选取分支路径
    find_leaf_depths(root, root, leaf_depths)
    depth_sort_list = sorted(leaf_depths.items(), key=lambda x: x[1], reverse=True)

    time = 0
    tree = Node(ingress)
    roads = []
    random_out = []
    max_depth = 0
    border_num = 2
    if border_num - 1 > len(leaf_depths):
        return False
    while len(random_out) < border_num - 1:
        a = random.randint(0, len(leaf_depths) - 1)
        if list(leaf_depths.items())[a][0].value not in random_out:
            random_out.append(list(leaf_depths.items())[a][0].value)
            max_depth = max(list(leaf_depths.items())[a][1], max_depth)
    print("最大树深：" + str(max_depth), end=", ")
    print("出口路由数量:" + str(len(random_out)), end=", ")
    for item in depth_sort_list:
        time += 1
        if item[0].value not in random_out:
            continue
        node = item[0]
        node2 = get_parent_node(root, node)
        road = [node.value]
        while node2 != root and node2 is not None:
            node = node2
            road.append(node.value)
            node2 = get_parent_node(root, node2)
        road.reverse()
        roads.append(road)
    sets = []
    for sub_tree in roads:
        tmp_root = tree
        for node_value in sub_tree:
            node = Node(node_value)
            if node.value not in sets:
                tmp_root.children.append(node)
                sets.append(node.value)
                tmp_root = tmp_root.children[len(tmp_root.children) - 1]
            else:
                j = 0
                for child in tmp_root.children:
                    if child.value == node.value:
                        break
                    j += 1
                tmp_root = tmp_root.children[j]

    # node1 = Node('A')
    # node2 = Node('B')
    # node1.add_child(node2)
    # node3 = Node('C')
    # node2.add_child(node3)
    # node5.add_child(node6)
    # node6.add_child(Node('I'))
    # node3.add_child(node7)
    # node4.add_child(node8)
    # root.postorder_traversal()
    # print(get_parent_node(root,node2.children[1]).value)

    # G = nx.DiGraph()
    # for link in links:
    #     G.add_edge(link[0], link[1])
    # entry_route = "s94"  # 入口路由
    # roads = []
    # for  exit_route in exit_routes:
    #     exit_route = set_value[len(set_value)-1]  # 出口路由
    #     try:
    #         shortest_path = nx.shortest_path(G, source=entry_route, target=exit_route)
    #         roads.append(shortest_path)
    #         print("最短路径:", shortest_path)
    #     except nx.NetworkXNoPath:
    #         print("无法找到从入口到出口的路径")
    Opt_Cover(tree)
    draw_tree(tree).render('./GV/ree.gv', view=True)
    return True


def main_topo_zoo():
    with open('Data/topozoo.txt', 'r') as file:
        content = file.readlines()
    tag = 1  # 是否在读取结点/链接
    nodes = []
    node_entity_list = []
    links = []
    delay = 0
    for line in content:
        if 'delay' in line:
            tag = 0
            delay = line.split("delay':'")[1].split("ms")[0]
            continue
        if tag:
            nodes.append(line.split(" = net.addSwitch")[0])
            node_entity_list.append(Node(line.split(" = net.addSwitch")[0]))
        else:
            city1 = line.split('addLink(')[1].split(', ')[0]
            city2 = line.split('addLink(')[1].split(', ')[1]
            cost = delay
            # node_dict[city1].add_child(node_dict[city2])
            links.append([city1, city2, cost])
            k = 1
    INFINITY = 1000000  # 无穷大

    # 距离矩阵
    D_matrix = [[INFINITY] * len(nodes) for _ in range(len(nodes))]
    for link in links:
        D_matrix[nodes.index(link[0])][nodes.index(link[1])] = int(float(link[2]) * 100)
        D_matrix[nodes.index(link[1])][nodes.index(link[0])] = int(float(link[2]) * 100)
    Path_matrix = [[0] * len(nodes) for _ in range(len(nodes))]  # 路径矩阵

    # 初始化路径矩阵，即P[u][v] 记录直达路径uv的终点v前面的顶点u
    for u in range(0, len(nodes)):
        for v in range(0, len(nodes)):
            Path_matrix[u][v] = u

    for w in range(0, len(nodes)):
        for u in range(0, len(nodes)):
            for v in range(0, len(nodes)):
                if w != u and w != v and D_matrix[u][w] + D_matrix[w][v] < D_matrix[u][v]:
                    D_matrix[u][v] = D_matrix[u][w] + D_matrix[w][v]
                    Path_matrix[u][v] = Path_matrix[w][v]

    Path = []  # 完整路径矩阵
    for i in range(0, len(nodes)):
        Path.append([])
        for j in range(0, len(nodes)):
            Path[i].append([])

    for u in range(0, len(nodes)):
        for v in range(0, len(nodes)):
            if u == v:
                continue
            print("{}到{}的逆向路径是:".format(u, v), end=' ')
            print(v, end=',')  # 先输出终点
            Path[u][v].append(v)
            w = Path_matrix[u][v]  # 推到上一个节点
            while w != u:
                print(w, end=',')
                Path[u][v].append(w)
                w = Path_matrix[u][w]  # 推到u-->w的上一个节点
            Path[u][v].append(u)
            print(u)
            Path[u][v].reverse()  # 逆序

    switch_list = range(0, len(nodes))
    ingress_list = sorted(random.sample(switch_list, 1))
    switch_list = list(set(switch_list) - set(ingress_list))
    egress_list = sorted(random.sample(switch_list, 3))
    name_index_list = []
    for i in range(0, len(nodes)):
        name_index_list.append(node_entity_list[i].value)
    for i in range(0, len(nodes)):
        name_index_list.append(node_entity_list[i].value)
    print("入口路由: ", end=" ")
    for ingress in ingress_list:
        print('{}, '.format(name_index_list[ingress]), end=" ")
    print("出口路由: ", end=" ")
    for egress in egress_list:
        print('{}, '.format(name_index_list[egress]), end=" ")
    print()
    for ingress in ingress_list:
        for egress in egress_list:
            last_node = ingress
            for path_node_item in Path[ingress][egress]:
                if path_node_item == ingress:
                    continue
                if node_entity_list[path_node_item] not in node_entity_list[last_node].children:
                    node_entity_list[last_node].add_child(node_entity_list[path_node_item])
                last_node = path_node_item

    # traffic_set(ingress_list)
    tree_list = []
    for ingress in ingress_list:
        tree_list.append(node_entity_list[ingress])
        # draw_tree(node_entity_list[ingress]).render('./GV/tree.gv', view=True)
    for tree in tree_list:
        traffic_set(tree)
        Opt_Cover(tree)
    draw_tree(tree_list[0]).render('./GV/tree.gv', view=True)
    k = 1


def custom_topo():
    node1 = Node('A', cap=100, traffic_ratio=1)
    node2 = Node('B', cap=80, traffic_ratio=0.5)
    node1.add_child(node2)
    node3 = Node('C', cap=60, traffic_ratio=0.5)
    node2.add_child(node3)
    node4 = Node('D', cap=80, traffic_ratio=0.5)
    node1.add_child(node4)
    Opt_Cover(node1)
    draw_tree(node1).render('./GV/tree.gv', view=True)



def main_ingress_bit(high=2):
    root = Node('n1', cap=100)
    leaf_list = [root]
    count = 1
    while count < 2 ** high-1:
        pop_node = leaf_list.pop(0)
        node1 = Node('n' + str(count + 1))
        node2 = Node('n' + str(count + 2))
        pop_node.add_child(node1)
        pop_node.add_child(node2)
        count += 2
        leaf_list.append(node1)
        leaf_list.append(node2)
    traffic_set(root)
    minmax_load = Opt_Cover(root)
    draw_tree(root).render('./GV/DC/tree.gv', view=False)
    return minmax_load

def main_ingress_rule(high=2):
    root = Node('n1')
    leaf_list = [root]
    count = 1
    while count < 2 ** high-1:
        pop_node = leaf_list.pop(0)
        node1 = Node('n' + str(count + 1))
        node2 = Node('n' + str(count + 2))
        pop_node.add_child(node1)
        pop_node.add_child(node2)
        count += 2
        leaf_list.append(node1)
        leaf_list.append(node2)
    traffic_set(root)
    node_list = [root]
    minmax_load = 0
    while node_list:
        node = node_list.pop(0)
        if node.children:
            for child in node.children:
                node_list.append(child)
        minmax_load = max(minmax_load, node.traffic_ratio * (128*2+9*2+10)/node.cap)
    return minmax_load

def main_ingress_single(high=2):
    return (128*2+9*2+10)/random.randint(100, 200)

if __name__ == '__main__':
    mean_list = []
    std_dev_list = []
    for i in range(2, 11):
        tmp_i = 0
        ans_list = []
        while tmp_i < 50:
            ans = main_ingress_bit(i)
            print("树高{}, 第{}次结果 |{}".format(i, tmp_i + 1, ans))
            ans_list.append(ans)
            tmp_i += 1
        mean = np.mean(ans_list)
        std_dev = np.std(ans_list, ddof=1)  # 设置 ddof=1 用于样本标准差
        print("均值:{}".format(mean))
        print("标准差:{}".format(std_dev))
        mean_list.append(mean)
        std_dev_list.append(std_dev)
    print()
    print(mean_list)
    print(std_dev_list)
