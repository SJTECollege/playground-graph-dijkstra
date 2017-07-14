# Dijkstra's Algorithm

Dijkstra's Algorithm allows you to calculate the shortest path between one node (you pick which one) and _every other node in the graph_. Let's study the algorithm with an explained example! Let's calculate the shortest path between node A and the other nodes in our graph:

![Graph example](dj-ini.png "")

(It's the same graph than before; I've just moved the numbers so everything is more readable during the explanation.)

We'll mark every node with its minimum distance to node A (our selected node). For node A, this distance is 0. For the rest of nodes, as we still don't know that minimum distance, it's infinity (∞).

![Graph example](dj-mark.png "")

Now, we set our _current node_ to A (our selected node). In the image, we mark the current node with a red dot.

Now, we check the neighbours of our current node (G, F, E and B) in no specific order. Let's begin with G. We add the minimum distance of the current node (in this case, 0) with the weight of the edge that connects our current node with G (in this case, 5), and we obtain 0+5 = 5. We compare that value with the minimum distance of G (infinity); the lowest value is the one that remains as the minimum distance of G (in this case, 5 is less than infinity):

![Graph example](dj-1.png "")

So far, so good. Now, let's check neighbour F. We add 0 (the minimum distance of A, our current node) with 3 (the weight of the edge connecting our current node with F) to obtain 3. We compare that 3 with the minimum distance of F (infinity), and leave the smallest value:

![Graph example](dj-2.png "")

OK. Repeat the same for E and B:

![Graph example](dj-3.png "")

Great. We have checked all the neighbours of A. Because of that, we mark it as _visited_. Let's represent visited nodes with a green check mark:

![Graph example](dj-adone.png "")

We now need to pick a new _current node_. That node must be the unvisited node with the smallest minimum distance (so, the node with the smallest number and no check mark). That's F. Let's mark it with the red dot:

![Graph example](dj-f.png "")

And now we repeat the algorithm. We check the neighbours of our current node, ignoring the visited nodes. This means we check G and E.

For G, we add 3 (the minimum distance of F, our current node) with 3 (the weight of the edge connecting F and G) to obtain 6. We compare that 6 with the minimum distance of G (5) and leave the smallest value; therefore, the 5 remains untouched.

For E, we add 3+2 = 5 and compare that value with 4; we leave the 4.

Afterwards, we mark F as visited and pick a new current node: E, which is the non-visited node with the smallest current distance.

![Graph example](dj-f.png "")

We repeat the algorithm again. This time, we only check B. We obtain 4+1 = 5; we compare that value with B's minimum distance (5) and leave the minimum one (5). We mark E as visited and pick a new current node. Both G and B have a minimum distance of 5, so we may pick any of them as current node.

Let's skip to the future. After we've marked every node as visited, we'll have this:

![Graph example](dj-end.png "")

We're done! The minimum distance of each node now actually represents the minimum distance from that node to node A (the node we picked as our initial node)!

Here's a description of the algorithm:
1. Mark your selected node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node C.
3. For each neighbour N of your current node: add the current distance of C with the weight of the edge connecting C-N. If it's smaller than the current distance of N, set it as the new current distance of N.
4. Mark the current node as visited.
5. If there are unvisited nodes, go to step 2.

@[The shown function should obtain the current node for Dijkstra's Algorithm.]({"stubs": ["nodes.py"], "command": "python3 test_nodes.py"})


# Next step
To obtain the paths that correspond to those minimum values, we simply need to keep track of the nodes every time we change the minimum distance of a node.