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
		pos = nx.random_layout(G)
		color_map = ['blue' if not G.node[i]['value'] else 'red' for i in list(G.nodes)]
		size_map = [200 if not G.node[i]['value'] else 600 for i in list(G.nodes)]
		nx.draw(G, pos, node_color=color_map, node_size=size_map, with_labels=True)
	return wrapper


def check_valid(func):
	def wrapper(*args, **kwargs):
		range_value = kwargs.pop('range_value', NUM_NODES) + 1
		while True:
			try:
				num = func(*args, **kwargs)
				if int(num) in range(1, range_value):
					return int(num)
			except Exception as e:
				pass
	return wrapper


@redraw
def prepare_graph(G):
	plt.ion()
	nx.set_node_attributes(G, {i: None for i in list(G.nodes)}, 'value')
	# add(G)


@check_valid
def get_input(msg, *args, **kwargs):
	return raw_input(msg)


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
  3. Request Route Between Real Nodes
  4. Exit
'''


if __name__ == '__main__':
	print title
	G = nx.gnp_random_graph(100, .10)
	prepare_graph(G)
	num_super_peers = get_input('Enter number of super peers: ')
	while True:
		print instructions
		choice = get_input('Enter your choice: ', range_value=4)
		# if choice == 1:
		# 	add(G)
		# if choice == 2:
		# 	key = int(raw_input('Which node id to delete: '))
		# 	delete(G, key)
		# if choice == 3:
		# 	node = int(raw_input('Enter node id to lookup from: '))
		# 	lookup(G, node)
		if choice == 4:
			print '\nHave a nice day!\n'
			exit()
