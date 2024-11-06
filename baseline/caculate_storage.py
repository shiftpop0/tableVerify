import sys
from tqdm import tqdm
from graphviz import Digraph
import random
import ip_black_list
from datetime import datetime
import multiTree


class Node:
    def __init__(self):
        self.value = ""
        self.parent_road_value = None
        self.parent = None
        self.lchild = None
        self.rchild = None
        self.level_index = -1
        self.is_end = False
        self.alloc_filter = None
        self.alloc_rule_flag = False  # 分配的规则读到此处为止
        self.is_alloc = False  # 当前结点是否被分配
        self.leaf_num = -1  # self为根的子树的叶子数量
        self.leaf_num_proto = -1
        self.is_full_node = -1  # self为根的子树是否是满二叉树，满树可聚合规则数量,-1表示未判断，0表示否，1表示是
        self.have_alloc = False  # 子树是否有被分配
        self.node_num = 0  # 子树总结点数量
        self.high = 0  # 从上往下的高度
        self.spec_high_node_num = 0  # 指定高度的结点数量

    def add_lchild(self, str, node):
        node.parent_road_value = str
        node.parent = self
        self.lchild = node

    def add_rchild(self, str, node):
        node.parent_road_value = str
        node.parent = self
        self.rchild = node

    def judge_is_full(self):
        if not self:
            return True
        elif self.is_end:
            self.is_full_node = 1
            return True
        if self.is_full_node != -1:
            return True if self.is_full_node == 1 else False
        elif self.lchild and self.rchild:
            if all([self.lchild.judge_is_full(), self.rchild.judge_is_full(), self.lchild.leaf_num == self.rchild.leaf_num, len(self.lchild.parent_road_value) == 1, len(self.rchild.parent_road_value) == 1]):
                self.is_full_node = 1
                return True
            else:
                self.is_full_node = 0
                return False
        else:
            if self.lchild:
                self.lchild.judge_is_full()
            if self.rchild:
                self.rchild.judge_is_full()
            self.is_full_node = 0
            return False

    # 先序遍历
    def preorder_traversal(self, queue=[]):
        queue.append(self)
        self.value = 'N' + str(len(queue))
        if self.lchild:
            self.lchild.preorder_traversal(queue)
        if self.rchild:
            self.rchild.preorder_traversal(queue)
        self.node_num = len(queue)

    # 后序遍历
    def postorder_traversal(self, queue=[]):
        if self.lchild:
            self.lchild.preorder_traversal(queue)
        if self.rchild:
            self.rchild.preorder_traversal(queue)
        queue.append(self)

    def level_traverse(self, spe_high=32, disable=True, desc="Level Traverse"):
        queue = [self]
        k = 0
        array = []
        total_process = self.node_num
        self_root = self
        self_root.spec_high_node_num = 0
        with tqdm(total=total_process, desc=desc, unit="nodes", disable=True) as pbar:
            while len(queue):
                node = queue.pop(0)
                if node.high < spe_high:
                    self_root.spec_high_node_num += 1
                array.append(node)
                node.level_index = k  # 层序
                k = k + 1
                if node.lchild:
                    queue.append(node.lchild)
                    node.lchild.high = node.high + 1
                if node.rchild:
                    queue.append(node.rchild)
                    node.rchild.high = node.high + 1
                pbar.update(1)
        return array

    def leaf_count(self):
        if not self:
            return 0
        elif self.is_end:
            self.leaf_num = 1
            self.leaf_num_proto = self.leaf_num
            return 1
        elif self.leaf_num != -1:
            return self.leaf_num
        else:
            self.leaf_num = (self.lchild.leaf_count() if self.lchild else 0) + (self.rchild.leaf_count() if self.rchild else 0)
            self.leaf_num_proto = self.leaf_num
            return self.leaf_num

    # 分配结点后修改leaf_num
    def modify_alloc(self, num, filter):
        filter_name = filter.name

        def modify_parent(node):
            current_node = node
            while current_node:
                current_node.leaf_num -= num
                if current_node.leaf_num == 0:
                    current_node.is_alloc = True
                current_node.have_alloc = True
                current_node = current_node.parent

        modify_parent(self)
        self.is_alloc = True

        def modify_kids(node):
            if node.lchild and not node.lchild.is_alloc:
                node.lchild.is_alloc = True
                node.lchild.leaf_num = 0
                modify_kids(node.lchild)
            if node.rchild and not node.rchild.is_alloc:
                node.rchild.is_alloc = True
                node.rchild.leaf_num = 0
                modify_kids(node.rchild)

        modify_kids(self)

        # 到满树就截止的深度优先遍历
        def depth_full_traversal(node):
            if node.is_full_node:  # 如果是满树结点
                return [node]
            else:
                l_list = []
                r_list = []
                if node.lchild:
                    l_list = depth_full_traversal(node.lchild)
                if node.rchild:
                    r_list = depth_full_traversal(node.rchild)
                return l_list + r_list

        def filter_rule_add(node, filter):
            rule = ''
            current_node = node
            while current_node.parent_road_value:
                rule = current_node.parent_road_value + rule
                current_node = current_node.parent
            filter.rule.append(rule + '/' + str(len(rule)))

        # 规则添加，且规则已被聚合过
        if self.is_full_node:
            self.alloc_filter = filter_name
            filter_rule_add(self, filter)
        else:
            full_node_list = depth_full_traversal(self)
            # depth_full_traversal(self, full_node_list)
            for item_node in full_node_list:
                item_node.alloc_filter = filter_name
                filter_rule_add(item_node, filter)


class Filter:
    def __init__(self, alph, name=''):
        self.name = name
        self.alph = alph
        self.alph_proto = alph
        self.rule = []


def alloc_node(node, Filter_list):
    def find_index(arr: list[Node], num):
        for index, item in enumerate(arr):
            if item.leaf_num <= num:
                return index
        return -1

    Filter_list = sorted(Filter_list, key=lambda x: x.alph, reverse=True)  # 降序
    array = node.level_traverse()  # 有序数组
    array = sorted(array, key=lambda x: (x.leaf_num, x.level_index), reverse=True)  # 降序

    total_process = node.leaf_num_proto
    # finish_process = 0
    # process_count = 0
    with tqdm(total=total_process, desc="分配进度 ", unit="leaf nodes") as pbar:
        while len(array):
            try:
                current_filter = Filter_list[0]
            except Exception as e:
                k = 1
                break
            alloc_index = find_index(array, current_filter.alph)
            current_filter.alph -= array[alloc_index].leaf_num
            pbar.update(array[alloc_index].leaf_num)  # 进度更新
            array[alloc_index].modify_alloc(array[alloc_index].leaf_num, current_filter)
            # draw_tree(node).render('wang.gv', view=True)
            if current_filter.alph == 0:
                Filter_list.pop(0)
            else:
                Filter_list = sorted(Filter_list, key=lambda x: x.alph, reverse=True)
            pop_list = []
            for index, item in enumerate(array):
                if item.is_alloc or item.have_alloc:
                    pop_list.append(index)
            for index, item in enumerate(pop_list):
                array.pop(item - index)
            array = sorted(array, key=lambda x: (x.leaf_num, x.level_index), reverse=True)

            k = 1


def draw_tree(root):
    dot = Digraph()
    queue = [root]
    while (len(queue)):
        node = queue.pop(0)
        # dot.node(str(id(node)), node.value + ", " + (node.alloc_filter if node.alloc_filter else ""))
        dot.node(str(id(node)), str(node.value))
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
    queue = [root]
    while (len(queue)):
        node = queue.pop(0)
        if node.lchild:
            dot.edge(str(id(node)), str(id(node.lchild)), node.lchild.parent_road_value)
            queue.append(node.lchild)
        if node.rchild:
            dot.edge(str(id(node)), str(id(node.rchild)), node.rchild.parent_road_value)
            queue.append(node.rchild)
    return dot


def random_filter(number=1000, n=2):
    if n == 0:
        raise ValueError("n不能为零")
    if n == 1:
        return [Filter(number, 'R0')]
    # 生成n-1个随机数，表示分割点
    load = sorted(random.sample(range(64, 128), n))
    sum_load = sum(load)
    split_points = []
    for index, item in enumerate(load[:-1]):
        tmp = int(number / sum_load * item)
        split_points.append(tmp)

    # 计算每个部分的大小
    split_sizes = [split_points[0]] + [split_points[i] - split_points[i - 1] for i in range(1, n - 1)] + [number - split_points[-1]]
    Filter_list = []
    for index, item in enumerate(split_sizes):
        Filter_list.append(Filter(item, 'R' + str(index)))
    return Filter_list


def avg_filter(number=1000, n=2):
    # 计算平均值和余数
    quotient = number // n
    remainder = number % n
    result = [quotient] * n
    for i in range(remainder):
        result[i] += 1
    Filter_list = []
    for index, item in enumerate(result):
        Filter_list.append(Filter(item, 'R' + str(index)))
    return Filter_list


def merge_node(node):  # 单孩子结点的合并
    grandson = None
    if not node:
        return
    if node.lchild and node.rchild:
        merge_node(node.lchild)
        merge_node(node.rchild)
    elif node.lchild:
        son_node = node.lchild
        if son_node.is_end:
            node.parent_road_value += node.lchild.parent_road_value
            node.is_end = True
            node.lchild = None
            del son_node
            return None
        if son_node.lchild and not son_node.rchild:
            grandson = node.lchild.lchild
        elif not son_node.lchild and son_node.rchild:
            grandson = node.lchild.lchild
        if grandson:
            grandson.parent_road_value = son_node.parent_road_value + grandson.parent_road_value
            grandson.parent = node
            del son_node
            node.lchild = grandson
            merge_node(node)
        else:
            merge_node(node.lchild)
            merge_node(node.rchild)
    elif node.rchild:
        son_node = node.rchild
        if son_node.is_end:
            node.parent_road_value += node.rchild.parent_road_value
            node.is_end = True
            node.rchild = None
            del son_node
            return None
        if son_node.lchild and not son_node.rchild:
            grandson = node.rchild.lchild
        elif not son_node.lchild and son_node.rchild:
            grandson = node.rchild.rchild
        if grandson:
            grandson.parent_road_value = son_node.parent_road_value + grandson.parent_road_value
            grandson.parent = node
            del son_node
            node.rchild = grandson
            merge_node(node)
        else:
            merge_node(node.lchild)
            merge_node(node.rchild)
    else:
        return


def create_tree(rule_list):
    root = Node()
    for index1, rule in enumerate(rule_list):
        current_node = root
        for index2, char in enumerate(rule):
            if char == '0':
                if not current_node.lchild:
                    current_node.add_lchild('0', Node())
                    current_node.lchild.is_end = True if index2 == len(rule) - 1 else False
                current_node = current_node.lchild
            else:
                if not current_node.rchild:
                    current_node.add_rchild('1', Node())
                    current_node.rchild.is_end = True if index2 == len(rule) - 1 else False
                current_node = current_node.rchild
    return root


def read_acl(ipsum=2):
    # with open('./TCPFilters10k', 'r') as file:
    #     lines = file.readlines()

    # i=0
    # lines=[]
    # while i<100000:
    #     line = "@"+str(random.randint(1,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'/'+str(random.randint(8,32))
    #     lines.append(line)
    #     i+=1

    lines = ip_black_list.read_github_ipsum(ipsum)

    rule_set = set()
    for index, line in enumerate(lines):
        columns = line.strip().split('\t')
        source_ip = columns[0].split('@')[1].split('/')
        bit_local = 0
        binary_rule = ""
        while bit_local * 8 < int(source_ip[1]):
            binary = bin(int(source_ip[0].split('.')[bit_local]))[2:]
            padding_zeros = 8 - len(binary)  # 高位补0
            binary = '0' * padding_zeros + binary
            if (bit_local + 1) * 8 > int(source_ip[1]):
                binary = binary[0:int(source_ip[1]) - bit_local * 8]
            binary_rule += binary
            bit_local += 1
        if len(binary_rule) < 8:
            continue
        rule_set.add(binary_rule)
    k = 1
    return list(rule_set)


# 最终分配好的规则集
def final_rule(ipsum=2, filter_num=2):
    # rule_list = ['0000', '001', '010', '011', '100', '101', '110', '111']
    rule_list = read_acl(ipsum)
    print("规则总数量：{}".format(len(rule_list)))
    root = create_tree(rule_list)
    merge_node(root)
    root.preorder_traversal([])
    root.leaf_count()
    print("叶子规则总数量：{}".format(root.leaf_num))
    root.judge_is_full()
    # filter_list = [Filter(35, 'R1'), Filter(4, 'R2')]
    filter_list = avg_filter(number=root.leaf_num, n=filter_num)
    # filter_list = random_filter(number=root.leaf_num, n=filter_num)
    alloc_node(root, filter_list)
    # draw_tree(root).render('wang.gv', view=True)
    for item in filter_list:
        print(item.name, end=', ')
        print("负载：{}，规则数量：{}".format(item.alph_proto, len(item.rule)), end=': ')
        # for index, item2 in enumerate(item.rule):
        #     if int(item2.split('/')[1])<32:
        #         print(item2, end=' ')
        print()
    return filter_list, root, create_tree(rule_list), len(rule_list)


def random_bit_filter(n=3):
    # load = sorted(random.sample(range(64, 128), n))
    load = [104] * n
    node_list = []
    for i in range(n):
        node_list.append(multiTree.Node(' ', cap=load[i]))
    for i in range(n-1):
        node_list[i].add_child(node_list[i+1])
    multiTree.Opt_Cover(node_list[0])
    # print("bit-based随机cap：{}, {}, 分配的brv: {}, {}".format(load[0], load[1], node1.brv, node2.brv))
    # multiTree.draw_tree(node_list[0]).render('wang.gv', view=True)
    brv_list = []
    for item in node_list:
        brv_list.append(item.brv)
    return brv_list


def calculate(ip_sum=8, filter_num=5):
    filter_list, root, root_proto, len_rule_list = final_rule(ip_sum, filter_num)
    print()

    tmp_avg_rule_pot_number = 10
    print("ingress-based规则数量：{}".format(len_rule_list))
    ingress_stroage = len_rule_list * (32 * 2 + 16 * tmp_avg_rule_pot_number + 8)
    print("ingress-based：{} bit".format(ingress_stroage))
    print()

    tmp_avg_port_number = 3  # 每个数组内的规则数量
    root_proto.preorder_traversal([])
    # root_proto.leaf_count()
    brv_list = random_bit_filter(n=filter_num)
    if brv_list[0] > 64:
        spe_high = 32
    elif brv_list[0] > 32:
        spe_high = brv_list[0] - 32
    else:
        spe_high = brv_list[0]
    root_proto.level_traverse(spe_high=spe_high, desc="root_proto层序遍历 ")
    # if brv_list[0] <= 32:
    #     bit_storage1 = root_proto.spec_high_node_num * 64 + root_proto.spec_high_node_num - 1
    #     storage_part = 16 * len_rule_list * tmp_avg_port_number * 2 + len_rule_list * 8 * 2
    #     bit_storage2 = root_proto.node_num * 64 + root_proto.node_num - 1 + (root_proto.node_num - root_proto.spec_high_node_num) * 64 + root_proto.node_num - root_proto.spec_high_node_num + storage_part
    # elif brv_list[0] > 32 and brv_list[0] <= 64:
    #     bit_storage1 = root_proto.node_num * 64 + root_proto.node_num - 1 + root_proto.spec_high_node_num * 64 + root_proto.spec_high_node_num - 1
    #     storage_part = 16 * len_rule_list * tmp_avg_port_number * 2 + len_rule_list * 8 * 2
    #     bit_storage2 = (root_proto.node_num - root_proto.spec_high_node_num) * 64 + root_proto.node_num - root_proto.spec_high_node_num + storage_part
    # elif 64 < brv_list[0] <= 66:
    #     bit_storage1 = 2 * (root_proto.node_num * 64 + root_proto.node_num - 1)
    #     storage_part = (66 - brv_list[0]) * 16 * len_rule_list * tmp_avg_port_number + len_rule_list * 8 * 2
    #     bit_storage2 = storage_part
    # else:
    #     storage_part = 16 * len_rule_list * tmp_avg_port_number * 2 + len_rule_list * 8 * 2
    #     bit_storage1 = 2 * (root_proto.node_num * 64 + root_proto.node_num - 1) + storage_part
    #     bit_storage2 = 0
    bit_storage_part1 = root_proto.spec_high_node_num * 64 + root_proto.spec_high_node_num - 1
    bit_storage_part2 = 16 * len_rule_list * tmp_avg_port_number * 2 + len_rule_list * 8 * 2
    print("bit-based结点数量：{}".format(root_proto.node_num))
    my_bit_storage = bit_storage_part1 + bit_storage_part2
    print("bit-based的存储空间：{}bit".format(my_bit_storage))
    print()

    rule_ip_node_num = []
    for filter_index, filter_item in enumerate(filter_list):
        rule_list = []
        for rule_index, rule_item in enumerate(filter_item.rule):
            rule_list.append(rule_item.split('/')[0])
        tmp_root = create_tree(rule_list)
        tmp_root.preorder_traversal([])
        # tmp_root.level_traverse(desc=(filter_item.name+"层序遍历 "))
        # tmp_root.leaf_count()
        rule_ip_node_num.append(tmp_root.node_num)
        print("{}的源ip存储：{}bit".format(filter_item.name, tmp_root.node_num), end=', ')
    print()
    tmp_storage_part = 16 * len_rule_list * tmp_avg_port_number * 2 + len_rule_list * 8 * 2
    print("Wang的ip存储大小{}，哈希方案存储大小{}".format(max(rule_ip_node_num)*2,tmp_storage_part))
    wang_rule_storage = max(rule_ip_node_num)*2 + tmp_storage_part
    print("Wang的存储：{}bit".format(wang_rule_storage))
    del filter_list, root, root_proto, len_rule_list
    return ingress_stroage, my_bit_storage, wang_rule_storage

    # sum_rule_times = [0] * len(filter_list)
    # ans = []
    # for filter_index, filter_item in enumerate(filter_list):
    #     for rule_index, rule_item in enumerate(filter_item.rule):
    #         prefix_len = int(rule_item.split('/')[1])
    #         sum_rule_times[filter_index] += prefix_len
    #     print("过滤器{}平均规则长度：{:.6f}".format(filter_item.name, sum_rule_times[filter_index] / len(filter_item.rule)))
    #     ans.append(sum_rule_times[filter_index] / len(filter_item.rule))
    # return ans


if __name__ == '__main__':
    ans1 = []  # 外循环是数量，内循环是多次实验
    ans2 = []
    ans3 = []
    for i in range(0, 9):
        ingress_storage, bit_storage, rule_storage = calculate(ip_sum=1, filter_num=i+2)
        ans1.append(ingress_storage)
        ans2.append(bit_storage)
        ans3.append(rule_storage)
    print()
    print("ingress-based")
    for index,item in enumerate(ans1):
        print("过滤器数量: {}".format(index+2))
        print(item)
    print()
    print("bit-based")
    for index, item in enumerate(ans2):
        print("过滤器数量: {}".format(index + 2))
        print(item)
    print()
    print("rule-based")
    for index, item in enumerate(ans3):
        print("过滤器数量: {}".format(index + 2))
        print(item)

