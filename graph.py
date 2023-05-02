from node import Node


class Graph:
    def __init__(self):
        self.graph_dict = {}
        self.start = None
        self.look_for = None

    def set_start(self, start_letter):
        # two ways to set the start (1st with instance_graph.start = 'A' the other one
        # instance_graph.set_start('A)
        self.start = start_letter

    def set_look_for(self, look_for_letter):
        self.look_for = look_for_letter

    def add_connections(self, number_of_connections=1):
        for i in range(number_of_connections):
            node1 = input("Node1: ")
            node2 = input("Node2: ")
            if node1 in self.graph_dict.keys():
                self.graph_dict[node1].append(node2)
            else:
                self.graph_dict[node1] = [node2]

            if node2 in self.graph_dict.keys():
                self.graph_dict[node2].append(node1)
            else:
                self.graph_dict[node2] = [node1]

    def print_connections(self):
        for key in self.graph_dict.keys():
            print(key, ':', self.graph_dict[key])

    def dfs(self):
        count = -1  # I added for counting how many edges (keep in mind nodes = edges - 1)
        visited = []  # if smth is in this list we dont want to go there anymore
        journey = []
        stack = [(self.start, None)]  # pair (node, parent)
        while len(stack) > 0:
            popped = stack.pop()
            current_node = popped[0]

            count += 1
            print("we are in: ", current_node)

            if current_node != self.look_for:
                visited.append(current_node)
                journey.append(popped)
                neighbours = self.graph_dict[current_node]
                for next_node in neighbours:
                    if next_node not in visited:
                        stack.append((next_node, current_node))
            else:
                journey.append(popped)
                print('count:', count)
                return journey
#ex. 3
    def dfs_modified(self):
            count = -1  # I added for counting how many edges (keep in mind nodes = edges - 1)
            visited = []  # if smth is in this list we dont want to go there anymore
            journey = []
            stack = [(self.start, None, 0)]  # pair (node, parent, distance)
            while len(stack) > 0:
                popped = stack.pop()
                current_node = popped[0]
                parent_distance = popped[2]

                count += 1
                print("we are in: ", current_node)

                if current_node != self.look_for:
                    visited.append(current_node)
                    journey.append(popped)
                    neighbours = self.graph_dict[current_node]
                    for next_node in neighbours:
                        if next_node not in visited:
                            next_distance = parent_distance + 1
                            stack.append((next_node, current_node, next_distance))
                else:
                    journey.append(popped)
                    print('count:', count)
                    return journey
#ex. 1
    def bfs(self): #bfs - breadth first search
        visited = [] #we make a list of visited nodes
        journey = [] #we make a list of the journey
        count = -1 #nodes = edges-1

        queue = [(self.start, None)]  # instead of stack u get queue -> pair (node, parent)

        while len(queue) > 0: #while the length of the graph is larger than 0, we can execute the search
            popped = queue.pop(0)  # now you pop 0th element instead of the last one
            current_node = popped[0] #current node is the 0th element of popped
            count += 1 #add a value to an existing variable and assign the new value back to the same variable
            if current_node != self.look_for: #if the current node is not equal to what we are looking for
                if current_node != visited: #and if current node is not in the visited list
                    visited.append(current_node) #we add current node to the visited list
                    journey.append(popped) #we add the popped element to the jounrey list
                    neighbours = self.graph_dict[current_node] #we are getting all the neighbor nodes of the current node
                    for next_node in neighbours: #iterating through the neighbours nodes
                        if next_node not in visited: #if the next node not in visited
                            queue.append((next_node, current_node)) #add the next node to the queue in front of the current node - FIFO
            else: #if the current node is what we are looking for
                journey.append(popped) #add the popped element to the journey list
                print('count:', count) #print the count
                return journey #return journey list
        return -1 #if the length of the queue is equal to 0, return -1
#ex. 2
    def trace_back(self):
        #journey = self.dfs() #question - how do i know if i have to use dfs or bfs here? isnt the shortest path looking method dependent on where the target is?
        # TODO: @katrina
        shortest_path = []
        current_node = self.look_for #look from end to start?
        while current_node != self.start:
            shortest_path.append(current_node) #in each iteration of the loop, the method appends current_node to the shortest_path list
            for node, parent in self.graph_dict.items():
                if current_node in parent and node not in shortest_path:
                    current_node=node #if current_node is a child of a node which is not already in the shortest_path list, the node becomes the new current_node
                    break
        shortest_path.append(self.start)
        print(shortest_path[::-1]) #::-1 means reverse

#ex 3*
    def graph_file(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines() #reads lines in the file
        for line in lines: #iterates through lines to find nodes and neighbors
            node, neighbors = line.strip().split(':') #strip removes unwanted characters (spaces)
            neighbors = neighbors.strip().split(',')
            self.graph_dict[node] = neighbors #node is used as a key, neighbors as corresponding values

ex_dict = {'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D', 'E'],
    'D' : ['B', 'C'],
    'E' : ['C', 'F'],
    'F' : ['E']}

graph = Graph()
graph.graph_dict = ex_dict
graph.start = "A"
graph.look_for = "E"

#print(graph.bfs())
#print(graph.dfs())
#print(graph.dfs_modified())
#print(graph.trace_back())

ex2_dict = {'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D', 'E', 'M'],
    'D' : ['B', 'C'],
    'E' : ['C', 'F', 'M'],
    'F' : ['E']}

graph2 = Graph()
graph2.graph_dict = ex2_dict
graph2.start = "A"
graph2.look_for = "M"

print(graph2.trace_back())

reading_file = Graph()
reading_file.graph_file('text.txt')
print(reading_file.graph_dict)