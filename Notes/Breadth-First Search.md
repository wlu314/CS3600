This is a general graph-[[Search Algorithm]] where the*shallowest* unexpanded node is chosen for expansion. It uses a FIFO [[Queue]] for the **Frontier**. The new nodes go to the back of the queue and the old nodes get expanded first.

The tweak is that the goal test is applied to each node when it is *generated rather than when it's selected for expansion*. 

**Pseudocode**
____
![[Figure 3.11 BFS Pseudocode.png | 600]]

## Complexity
____
Imagine a uniform tree where every state has *b* successors. The root of the search tree generates *b* nodes at the first level, each of which generates *b* more nodes. Suppose the solution is at depth *d*. In the worst case, the total number of nodes generated is $$b+b^2+b^3+...+b^d=O(b^d)$$
The space complexity is $O(b^d)$ because every node generated remains in memory. 
![[Figure 3.13 BFS Complexity.png | 600]]


(If the algorithm were to apply the goal test to nodes when selected for expansion, rather than when generated, the whole layer of nodes at depth d would be expanded before the goal was detected and the time complexity would be $O(b^{d+1})$. 

## Depth-Limited Search
____
A predetermined depth limit $l$. That is nodes at depth $l$ treated as if they have no successors. This is called depth-limited search. This solves the infinite path problem. Unfortunately, it also introduces an additional source of incompleteness if we choose $l < d$, that is, the shallowest goal is beyond the depth limit. (This is likely when d is unknown.) Depth-limited search will also be non-optimal if we choose $l > d$. Its time complexity is $O(b^l)$ and its space complexity is $O(bl)$. Depth-first search can be viewed as a special case of depth-limited search with $l = ∞$ 
![[Figure 3.17 Depth-limited tree search.png]]

## Iterative Deepening DFS
___
Iterative deepening search (or iterative deepening depth-first search) is a general strategy, often used in combination with depth-first tree search, that finds the best depth limit. It does this by gradually increasing the limit—first 0, then 1, then 2, and so on—until a goal is found. This will occur when the depth limit reaches $d$, the depth of the shallowest goal node.