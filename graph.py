from node import Node


class Graph:
    def __init__(self):
        self.graph_dict = {}
        self.start = None
        self.look_for = None

    def set_start(self, start_letter):
        self.start = Node(start_letter, parent=None, distance=0)

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
        count = -1
        visited = []
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


    def bfs(self):
        visited = []
        journey = []
        count = -1

        queue = [(self.start, None)]

        while len(queue) > 0:
            popped = queue.pop(0)
            current_node = popped[0]
            count += 1
            if current_node != self.look_for:
                if current_node != visited:
                    visited.append(current_node)
                    journey.append(popped)
                    neighbours = self.graph_dict[current_node]
                    for next_node in neighbours:
                        if next_node not in visited:
                            queue.append((next_node, current_node))
            else:
                journey.append(popped)
                print('count:', count)
                return journey
        return -1




