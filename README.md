# PP6

## 1
Analyse the BFS program make commments and workout elements of the code.
Try adding prints in places and test out whether they are what you expected.

## 2

Complete the traceback method in `graph.py` and print out the shortest path
from start to end. For our example it would be:
A, C, D
Notice that you just need to add line:
`print(our_graph.traceback())`
to `main.py` in order to test it.
Provide some test cases to test your algorithm.

## 3

Modify (copy and make a new function) of DFS or BFS
that instead of keeping track of tuples (current_node, parent) would
keep track of tuples (next_node, minimum_distance).
Hint: distance to next node is parents distance + 1

Where can you find a minimum distance to the target node?
## 3*
Make a method in class Graph where 
dictionary for the graph could be read from a 
file (like in the last lesson). Develop a few test cases.


