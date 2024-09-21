This is an instance of the general Tree-Search or Graph-Search algorithm where a node is selected for expansion based on the **evaluation function, $f(n)$**. This function is construed as a cost estimate so the node with the lowest evaluation is expanded first. The implementation is identical to [[Uniform-Cost Search]] except for the use of $f$ instead if $g$ to order the PQ.  

**Heuristic Function, $h(n)$** is the estimated cost of the cheapest path from the state a node n to a gaol state. Basically is the same as UCS but adds the heuristic function (Highest Priority). 

1. **Initialization**:
   - Start with an empty priority queue and insert the start node \( s \) with its heuristic value \( h(s) \).

2. **Expansion Loop**:
   - While the priority queue is not empty:
     - Remove the node \( n \) with the lowest heuristic value \( h(n) \) from the priority queue.
     - If \( n \) is the goal node, return the path to \( n \) as the solution.
     - Otherwise, expand node \( n \) to generate its successors.
     - For each successor, compute its heuristic value and insert it into the priority queue if it has not been visited before.

3. **Termination**:
   - The algorithm terminates when the goal node is reached or the priority queue is empty (indicating that no path to the goal exists).

**Characteristics**
- **Informed Search**: Best-First Search is an informed search algorithm because it uses domain-specific knowledge (heuristics) to guide the search.
- **Efficiency**: The efficiency of Best-First Search depends on the quality of the heuristic function. A good heuristic can significantly reduce the search space and time.
- **Admissibility**: Best-First Search is not guaranteed to be admissible (i.e., it may not always find the least-cost path to the goal). This depends on the heuristic function used.
- **Optimality**: Similarly, Best-First Search is not guaranteed to be optimal unless the heuristic is consistent and admissible.
## Greedy Best-First Search
___
This tries to expand the node that is closest to the goal on the grounds that this is likely to lead to a solution quickly. It evaluates node by using the **heuristic function** $f(n) = h(n)$. It's incomplete in a finite state space much like depth-first search. It can lead to infinite loops. The graph search version is complete in finite spaces but not in infinite ones. The worst case **time**  and **space** complexity for the *tree version* is $O(b^m)$, where $m$ is the maximum depth of the search space. 


