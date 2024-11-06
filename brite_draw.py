import networkx as nx
import matplotlib.pyplot as plt
import topo_json

# 创建一个空的图形对象
G = nx.Graph()

nodes = []
edges = []
topo_json.brite_read(nodes,edges)
nodes_data = [
    # (0, {'pos': (9, 6)})
]
for node in nodes:
    nodes_data.append((int(node.split()[0]),{'pos':(int(node.split()[1]),int(node.split()[2]))}))

# 添加节点到图形中
G.add_nodes_from(nodes_data)

# 边数据
edges_data = [
    # (0, 2, {'weight': 3.1622776601683795})
]
for edge in edges:
    edges_data.append((int(edge.split()[1]),int(edge.split()[2]),{'weight':int((edge.split()[3]).split('.')[0])}))

# 添加边到图形中
G.add_edges_from(edges_data)

# 提取节点位置信息
node_positions = {node: data['pos'] for node, data in G.nodes(data=True)}

# 绘制图形
plt.figure(figsize=(8, 8))
nx.draw(G, pos=node_positions, with_labels=True, node_size=100, node_color='lightblue', font_size=10, font_color='black')
edge_labels = {(u, v): data['weight'] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels, font_size=8)
plt.title('Network Topology')
plt.axis('off')
plt.show()
