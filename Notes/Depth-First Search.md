This [[Search Algorithm]] expands the *deepest* node in the current frontier of the search tree. The search proceeds immediately to the deepest level of the search tree where the node has no successors. As those nodes are expanded, they are dropped from the frontier.

Depth-First Search uses a LIFO [[Queue]]. This means that the most recently generated node is chosen for expansion. Alternatively, it's common to use a recursive function that calls itself on each of its children.
![[Figure 3.16 DFS Diagram.png | 600]]

## Tree Search vs. Graph Search
___
Graph Search avoids repeated states and redundant paths. It is complete in finite state spaces because it will eventually expand every node. The tree search is not complete. Depth-first tree search can be modified at no extra memory cost so that it checks new states against those on the path from the root to the current node; this avoids infinite loops in finite state spaces but does not avoid the proliferation of redundant paths.

Both Versions are non-optimal. 

## Complexity
____
It may generate all of the $O(b^m)$ nodes in a search tree where *m* is the max depth of any node. *m* can be larger than the depth of the shallowest solution. The reason to use DFS is the space complexity. DFS store only a single path from the root to a leaf node. For a graph search, there is no advantage, but a depth-first tree search needs to store only a single path from the root to a leaf node, along with the remaining unexpanded sibling nodes for each node on the path. Once a node has been expanded, it can be removed from memory as soon as all its descendants have been fully explored. (See Figure 3.16.) For a state space with branching factor *b* and maximum depth *m*, depth-first search requires storage of only $O(bm)$ nodes.

**Backtracking Search** is a variant of DFS. One successor is generated at a time rather than all successors. In this way, only $O(m)$ memory is needed rather than $O(bm)$.