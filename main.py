from graph import Graph

our_graph = Graph()



ex_dict = {'A' : ['B', 'C'],
'B' : ['A', 'D'],
'C' : ['A', 'D', 'E'],
'D' : ['B', 'C'],
'E' : ['C', 'F'],
'F' : ['E']}

our_graph.graph_dict = ex_dict
our_graph.print_connections()
our_graph.add_connections(int(input('How many connections do you wanna add? ')))

our_graph.print_connections()

our_graph.start = 'A'
our_graph.look_for = 'D'

print("DFS: ")
print(our_graph.dfs())

#print("BFS: ")
#print(our_graph.bfs())
