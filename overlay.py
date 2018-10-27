import random
import math

try:
	import networkx as nx
	import matplotlib.pyplot as plt
except:
	print 'This program requires networkx and matplotlib packages.'
	exit()

NUM_NODES = 100


def redraw(func):
	def wrapper(*args, **kwargs):
		plt.close()
		func(*args, **kwargs)
		color_map = [G.node[i].get('color', 5) for i in list(G.nodes)]
		size_map = [600 if G.node[i].get('value', None) == 'superpeer' else 200 for i in list(G.nodes)]
		superpeers = [x for x in list(G.nodes) if G.node[x]['value'] == 'superpeer']
		nx.draw(G, pos, node_color=color_map, node_size=size_map, with_labels=True, edge_color='gray', width=0.2, cmap=plt.cm.Blues)
	return wrapper


def check_valid(func):
	def wrapper(*args, **kwargs):
		range_value = kwargs.get('range_value', None)
		while True:
			try:
				num = func(*args, **kwargs)
				if range_value and int(num) in range(1, range_value):
					return int(num)
				elif int(num) in list(G.nodes):
					return int(num)
				else:
					raise
			except Exception as e:
				pass
	return wrapper


def reset_graph(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		print 'Updating super peer assignments...'
		for i in list(G.nodes):
			G.node[i]['value'] = None
			G.node[i]['color'] = 5
			G.node[i]['peers'] = []
			G.node[i]['superpeer'] = None
		add_super_peers(G, num_super_peers)
	return wrapper


@redraw
def prepare_graph(G, pos):
	plt.ion()
	nx.set_node_attributes(G, {i: None for i in list(G.nodes)}, 'value')
	for i in list(G.nodes):
		node_list = list(G.nodes)
		node_list.remove(i)
		for _ in range(len(G.nodes) // 4):
			random_node = random.choice(node_list)
			G.add_edge(i, random_node)
			node_list.remove(random_node)


@reset_graph
def add_node(G, pos, num_super_peers):
	node_num = list(G.nodes)[-1] + 1
	G.add_node(node_num)
	pos[node_num] = (random.random(), random.random())
	node_list = list(G.nodes)
	for _ in range(len(G.nodes) // 4):
		random_node = random.choice(node_list)
		G.add_edge(node_num, random_node)
		node_list.remove(random_node)
	print 'Added node {}.'.format(node_num)


@reset_graph
def remove_node(G, node, num_super_peers):
	G.remove_node(node)
	print 'Removed node {}.'.format(node)


@check_valid
def get_input(msg, *args, **kwargs):
	return raw_input(msg)


@redraw
def add_super_peers(G, num_super_peers):
	superpeers = random.sample(list(G.nodes), num_super_peers)
	peers = superpeers[:]
	for s in superpeers:
		G.node[s]['value'] = 'superpeer'
		G.node[s]['color'] = 10
		G.node[s]['peers'] = []
		color = random.randint(10, 30)
		for n in G.neighbors(s):
			if n not in peers:
				G.node[s]['peers'].append(n)
				G.node[n]['color'] = color
				G.node[n]['superpeer'] = s
				peers.append(n)
	nodes_without_superpeers = list(set(list(G.nodes)) - set(peers))
	def find_peer():
		for s in superpeers:
				for p in G.node[s]['peers']:
					if n in G.neighbors(p):
						G.node[s]['peers'].append(n)
						G.node[n]['superpeer'] = s
						G.node[n]['color'] = G.node[p]['color']
						peers.append(n)
						return
	for n in nodes_without_superpeers:
		find_peer()
	nodes_without_superpeers = list(set(list(G.nodes)) - set(peers))
	if nodes_without_superpeers:
		print 'Nodes without direct access to a super peer: ' + ', '.join([str(x) for x in nodes_without_superpeers])


def find_route(G, node1, node2):
	route = []
	node1_superpeer = G.node[node1].get('superpeer', node1)
	if node1_superpeer != node1:
		route += nx.shortest_path(G, node1, node1_superpeer)
		route.remove(node1_superpeer)
	node2_superpeer = G.node[node2].get('superpeer', node2)
	sp_route = nx.shortest_path(G, node1_superpeer, node2_superpeer)
	sp_route[0] = str(sp_route[0]) + ' (super peer)'
	sp_route[-1] = str(sp_route[-1]) + ' (super peer)'
	route += sp_route
	if node2_superpeer != node2:
		route += nx.shortest_path(G, node2_superpeer, node2)
		route.remove(node2_superpeer)
	print 'Route: ' + ' -> '.join(str(item) for item in route)


def view_super_peer_tables(G):
	for i in list(G.nodes):
		if G.node[i].get('value', None) == 'superpeer':
			print 'Peers belonging to super peer {}: {}'.format(i, G.node[i]['peers']) 




title = '''

Overlay Network
===============
This program models an overlay network in simulation.  The simulation displays visually
both the "real" network and the overlay.  The simulation generates at least 100 nodes for
the "real" network.  Each node of the "real" network is connected randomly to at least
25% of the other "real" nodes.  The overlay network connects every node in a structured
manner using super peers.  The super peers divide the real network into regions such that
there would be one super peer per region.

'''

instructions = '''

 User choices:
  1. Add node
  2. Delete node
  3. Request route between real nodes
  4. View super peer tables
  5. Exit
'''


if __name__ == '__main__':
	print title
	G = nx.empty_graph(NUM_NODES)
	pos = nx.random_layout(G)
	prepare_graph(G, pos)
	num_super_peers = get_input('Enter number of super peers: ')
	add_super_peers(G, num_super_peers)
	while True:
		print instructions
		choice = get_input('Enter your choice: ', range_value=5)
		if choice == 1:
			add_node(G, pos, num_super_peers)
		if choice == 2:
			node = get_input('Which node id to delete: ')
			remove_node(G, node, num_super_peers)
		if choice == 3:
			node1 = get_input('Enter starting node id: ')
			node2 = get_input('Enter ending node id: ')
			find_route(G, node1, node2)
		if choice == 4:
			view_super_peer_tables(G)
		if choice == 5:
			print '\nHave a nice day!\n'
			exit()
