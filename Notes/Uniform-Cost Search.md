This is a [[Search Algorithm]]. Instead of expanding in the shallowest node, [[Uniform-Cost Search]] expands on the node *n* with the lowest path cost $g(n)$. This is done by storing the frontier as a priority queue ordered by the cost *g*. 

UCS doesn't care about the number of step the solution has but the total cost of that path. Therefore, it will get stuck in an infinite loop if there is a path with an infinite sequence of zero-cost actions. 
### Difference from BFS
____
1. The goal test is applied to a node when it is *selected for expansion* .
2. A test is added in case a better path is found to a node currently on the frontier

**Pseudocode**   
___
![[Figure 3.14 UCS Pseudocode.png | 600]]

**Example**
___
![[Figure 3.15 UCS Example.png]]
In this example, we'll explore the difference between UCS and BFS. This is to optimize the solution. The goal state is to reach *Bucharest* from *Sibiu*. The successors of Sibiu are Rimnicu Vilcea (cost: 80) and Fagaras (cost: 99). The least cost node is expanded next adding Pitesti (80+97 = 177). The least cost node is now Fagaras which expands to Bucharest (99+211=310). Now a goal node has been generated but UCS keeps going, choosing Pitesti for expansion (80+97+101 = 278). The algorithm sees that the new path is more optimal so the old one is discarded. The *g-cost* is 278.

## Complexity
____
Because the search is guided by path cost the complexity is not easily characterized in terms of successors *b* or depth *d*. Let $C^*$ be the cost of the optimal solution, assume that every action costs at least $\epsilon$. Then the worst case time and space complexity is $O(b^{1+\lfloor C^* \epsilon \rfloor})$ which could be greater than $b^d$. This is because UCS can explore large trees of small steps before paths involving large and perhaps useful steps. When all step costs are equal the previous complexity is just $b^{d+1}$. When all costs are the same, uniform cost search is similar to [[Breadth-First Search]]. 