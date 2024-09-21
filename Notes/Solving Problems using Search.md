#### Search
___
Agents can construct sequence of actions that achieve its goals; this process is called [[Search]]. 
- a **goal** must be defined and well-defined **problem** must be formulated. 
- There is 5 parts: **initial state**, **a set of actions**, **transitional models** - describing result of actions, **goal test function**, and a **path cost function**. The environment is called a **state** **space**. A **path** through the state space from initial state to a goal state is a **solution**. 
- Search algorithms treat states and actions as **atomic** - they don't consider any internal structure. 
- **Tree Graph Algorithms** - consider all possible paths to find a solution. There is no need for an explored set because a Tree is directional. 
- **Graph Search Algorithms** - avoid considerations of redundant paths. This means that there is an **explored set** when considering expanding. 

#### Uniformed Search
____
[[Breadth-First Search]] - expands the shallowest nodes first, complete, optima for unit steps costs. It has exponential space complexity. 

[[Uniform-Cost Search]] - expands the node with lowest path cost, $g(n)$ and it's optimal for general step costs, NOT heuristics. 

[[Depth-First Search]] - expands on the deepest unexpanded node first. It's neither complete nor optimal, but has a linear space complexity.

Iterative Deepening Search - uses DFS with increasing depth limits until a goal is found, optimal for unit steps costs, has time complexity comparable to BFS, but has a linear time complexity

[[Bidirectional Search]] - reduces time complexity by half, but not always applicable and may require too much space expanded from the goal and the start state. 

#### Informed Search
___
[[Heuristic Search Strategies]] has access to **heuristic functions** $h(n)$ that estimates the cost of a solution from $n$. Information can be found in [[Heuristic Search Strategies]].

[[Best-First Search]] - selects a node for expansion by the evaluation function.

**Greedy Best First Search**, in [[Best-First Search]], expands nodes with the minimized heuristic function $h(n)$. This is not optimal but is often efficient. 

[[A* Search]] expands with minimal $f(n)=g(n)+h(n)$. $A^*$ is complete and optimal provided that $h(n)$ is admissible (for tree search) or consistent (for graph search). 