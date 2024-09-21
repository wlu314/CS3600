This [[Search Algorithm]] runs two searches. One forward from the initial state and the other backward from the goal. It does this to find a middle ground. The motivation is that $b^{d/2} + b^{d/2}$ is much less than $bd$, or in the figure, the area of the two small circles is less than the area of one big circle centered on the start and reaching to the goal.

Instead of a goal test, it check to see whether the frontiers of the two searches intersect. If they do, a solution is found. The check can be done when each node is generated or selected for expansion and, with a hash table, will take constant time.

For example, if a problem has solution depth d = 6, and each direction runs breadth-first search one node at a time, then in the worst case the two searches meet when they have generated all of the nodes at depth 3. For b = 10, this means a total of 2,220 node generations, compared with 1,111,110 for a standard breadth-first search. Thus, the time complexity of bidirectional search using breadth-first searches in both directions is $O(b^{d/2})$. The space complexity is also $O(b^{d/2})$.

