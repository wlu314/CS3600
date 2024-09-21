### BFS - Breadth-First Search
____
[[Breadth-First Search]] is a simple strategy where the root node is expanded first, then all successors of the root node are expanded next, then their successors. All the nodes are expanded at a given depth in the search tree before any nodes at the next level are expanded. 

BFS Is optimal when all step costs are equal and the path cost is a nondecreasing function of the depth of the node.
### Uniform-Cost Search
___
Instead of expanding in the shallowest node, [[Uniform-Cost Search]] expands on the node *n* with the lowest path cost $g(n)$. This is done by storing the frontier as a priority queue ordered by the cost *g*. 

### Depth-First Search
____
[[Depth-First Search]] expands the *deepest* node in the current frontier of the search tree. The search proceeds immediately to the deepest level of the search tree where the node has no successors. As those nodes are expanded, they are dropped from the frontier.

### Bidirectional Search
____
[[Bidirectional Search]] runs two searches. One forward from the initial state and the other backward from the goal. It does this to find a middle ground. The motivation is that $b^{d/2} + b^{d/2}$ is much less than $bd$, or in the figure, the area of the two small circles is less than the area of one big circle centered on the start and reaching to the goal.


![[Figure 3.21 Complexity of All Search Algo.png]]