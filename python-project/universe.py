
def set_current_node(visited, currentDistances):
    # visited is a set that contains the name of the nodes marked as visited. E.g. {'A', 'C'}.
    # currentDistances is a dictionary that contains the current distance of each node. E.g. {'A':0, 'B':3, 'C':5}
    edges = []

    #To add an edge, use edges.append(node1, node2, weight).
    #For example, edges.append(1,2,10) connects nodes 1 and 2 with an edge of weight 10.
    edges.append(1,2,10)
    edges.append(1,3,15)
    edges.append(2,3,6)

    return edges