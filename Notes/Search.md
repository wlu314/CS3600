One kind of goal-based agent is called a **problem-solving agent**. These agent use **atomic** representations described in [[Intelligent Agents]]. Goal-based agents that use more advanced **factored** or **structured** representation are called **planning agents**. 

**Uninformed vs Informed:** We will see several **uninformed** search algorithms—algorithms that are given no information about the problem other than its definition. Although some of these algorithms can solve any solvable problem, none of them can do so efficiently. **Informed** search algorithms, on the other hand, can do quite well given some guidance on where to look for solutions.

The process of looking for a sequence of actions that reaches the goal is called **search**. A search algorithm takes a problem as input and returns a solution in the form of an action sequence. Once a solution is found, the actions it recommends can be carried out. This is called the **execution phase**.

![[Figure 3.1 Simple Problem Solving agent.png| 400]]

## 5 Components of a Problem
___
1. **Initial State** that the agent starts in. 
2. A description of the possible **actions** available to the agent. Given a particular state *s*, $ACTIONS(s)$ returns the set of actions that can be executed in the state *s*. Each of these actions is **applicable** in *s*. 
3. A description of what each action does. The formal name for this is the **transition model**, specified by a function $RESULT(s,a)$ that returns the state that results from doing action *a* in state *s*. We also use the term **successor** to refer to any state reachable from a given state by a single action. The initial state, actions, and transition model implicitly define the **state space** of the problem. This is the set of all states reachable from the initial state by any sequence of actions. The state space forms a directed network or **graph** where nodes are states and links between nodes are actions. A **path** in the state space is a sequence of the states connected by a sequence of actions.
4. The **goal test**, which determines whether a given state is a goal state. Sometimes there is an explicit set of possible goal states and the test simply checks whether the give state is one of them.
 
![[Figure 3.2 Road Map of Romonia.png]]
Sometimes the goal is specified by an abstract property rather than an explicitly enumerated set of states. For example, in chess, the goal is to reach a state called "checkmate".
5. The **path cost** function assign a numeric cost of each path. The problem-solving agent chooses a cost function that reflects its own performance measure. We assume the cost of a path can be described as the sum of the costs of the individual actions along the path. The **step cost** of taking action *a* in state *s* to reach state *s'* is denoted by *c(s,a,s')*. 

A **solution** to a problem is an action sequence that leads from the initial state to a goal state. Solution quality is measured by path cost function and an **optimal solution** has the lowest path cost among all the solutions. 

**Abstraction** is the process of removing detail from a representation. In addition to abstracting the state description, we must abstract the actions themselves. 

## Toy Problem Examples
____
![[Figure 3.4.png]]
**States:** A state description specifies the location of each of the eight tiles and the blank in one of the nine squares.
**Initial State:** Any state can be designated as the initial state.
**Actions:** Left, Right, Up, or Down are the actions. 
**Transition Model:** Given a state and action, this returns the resulting state
**Goal Test:** This checks whether the state machines the goal configured in the photo.
**Path Cost**: Each step costs 1, so the path cost is the number of steps in the path. 

This 8-puzzle belongs to the family of **sliding block puzzles** which are often used as test problems for new search algorithms in AI. This family is known to be [[NP-complete]], so one does not except to find methods significantly better in the worst case than the search algo. The 8-puzzle has 9!/2 = 181,440 reachable states and is easily solved. 

![[Figure 3.5 - 8 Queens Problem.png | 400]]
**8 Queens Problem:** The goal is to place eight queens on a chessboard such that no queens attack one another. An incremental formulation involves operators that augment the state description, starting with an empty state; for the 8-queens problem, this means that each action adds a queen to the state. A complete-state formulation starts with all 8 queens on the board and moves them around. In either case, the path cost is of no interest because only the final state counts. The first incremental formulation one might try is the following:

**States:** Any arrangement of 0 to 8 queens on the board is a state.  
**Initial state:** No queens on the board.  
**Actions:** Add a queen to any empty square.  
**Transition model:** Returns the board with a queen added to the specified square.
**Goal test:** 8 queens are on the board, none attacked.

## Real World Problems Examples
____
**Routing Finding Problem**
**States**: Each state includes a location and the current time. Cost of an action may depend on previous segments, their fare bases, and their status as domestic or international (flights), state must record extra information about these aspects.
**Initial State**: Specified by the user's query
**Actions**: Take my flight from the current location, in any seat class, leaving after the current time, leaving enough time, for transfers
**Transition model:** The state resulting from taking a flight will have the flight’s destination as the current location and the flight’s arrival time as the current time.
**Goal test:** Are we at the final destination specified by the user?
**Path cost:** This depends on monetary cost, waiting time, flight time, customs and immigration procedures, seat quality, time of day, type of airplane, frequent-flyer mileage awards, and so on.


**Touring problems** are closely related to route-finding problems, but with an impot tant difference. Consider, for example, the problem “Visit every city in Figure 3.2 at least once, starting and ending in Bucharest.” As with route finding, the actions correspond to trips between adjacent cities. The state space, however, is quite different. Each state must include not just the current location but also the set of cities the agent has visited. So the initial state would be In(Bucharest),Visited({Bucharest}), a typical intermediate state would be In(Vaslui),Visited({Bucharest,Urziceni,Vaslui}), and the goal test would check whether the agent is in Bucharest and all 20 cities have been visited.

The traveling salesperson problem (**TSP**) is a touring problem in which each city must be visited exactly once. The aim is to find the shortest tour. The problem is known to be NP-hard, but an enormous amount of effort has been expended to improve the capabilities of TSP algorithms. In addition to planning trips for traveling salespersons, these algorithms have been used for tasks such as planning movements of automatic circuit-board drills and of stocking machines on shop floors.

A **VLSI** layout problem requires positioning millions of components and connections on a chip to minimize area, minimize circuit delays, minimize stray capacitances, and max- imize manufacturing yield. The layout problem comes after the logical design phase and is usually split into two parts: cell layout and channel routing. In cell layout, the primitive components of the circuit are grouped into cells, each of which performs some recognized function. Each cell has a fixed footprint (size and shape) and requires a certain number of connections to each of the other cells. The aim is to place the cells on the chip so that they do not overlap and so that there is room for the connecting wires to be placed between the cells. Channel routing finds a specific route for each wire through the gaps between the cells. These search problems are extremely complex, but definitely worth solving. Later in this chapter, we present some algorithms capable of solving them.

**Robot navigation** is a generalization of the route-finding problem described earlier. Rather than following a discrete set of routes, a robot can move in a continuous space with (in principle) an infinite set of possible actions and states. For a circular robot moving on a flat surface, the space is essentially two-dimensional. When the robot has arms and legs or wheels that must also be controlled, the search space becomes many-dimensional. Advanced techniques are required just to make the search space finite. We examine some of these methods in Chapter 25. In addition to the complexity of the problem, real robots must also deal with errors in their sensor readings and motor controls.

**Automatic assembly sequencing** of complex objects by a robot was first demonstrated by FREDDY (Michie, 1972). Progress since then has been slow but sure, to the point where the assembly of intricate objects such as electric motors is economically feasible. In assembly problems, the aim is to find an order in which to assemble the parts of some object. If the wrong order is chosen, there will be no way to add some part later in the sequence without undoing some of the work already done. Checking a step in the sequence for feasibility is a difficult geometrical search problem closely related to robot navigation. Thus, the generation of legal actions is the expensive part of assembly sequencing. Any practical algorithm must avoid exploring all but a tiny fraction of the state space. Another important assembly problem is **protein design**, in which the goal is to find a sequence of amino acids that will fold into a three-dimensional protein with the right properties to cure some disease.
# Searching For Solution
___
A solution is an action sequence, so search algorithms work by considering various possible action sequences. The possible action sequences starting at the initial state form a **search tree**. Branches are actions and the **nodes** are the states in the state space of the problem. The set of all leaf nodes available for expansion at any given point is called the **frontier**. (Many authors call it the **open list**, which is both geographically less evocative and less accurate, because other data structures are better suited than a list.) In Figure 3.6, the frontier of each tree consists of those nodes with bold outlines.

To expand nodes on the frontier continues until a solution is found or there is no more states to expand. **Search strategy** depends on which state to expand next to. Loopy paths are a special case of the more general concept of **redundant paths**. This exist whenever there is more than one way to get from one state to another. In other cases, redundant paths are unavoidable. This includes all problems where the actions are reversible, such as route-finding problems and sliding-block puzzles. Route- finding on a **rectangular grid**.

![[Figure 3.6 - Search Tree.png | 600]]

s the saying goes, algorithms that forget their history are doomed to repeat it. The way to avoid exploring redundant paths is to remember where one has been. To do this, we augment the TREE-SEARCH algorithm with a data structure called the explored set (also known as the closed list), which remembers every expanded node. Newly generated nodes that match previously generated nodes—ones in the explored set or the frontier—can be dis- carded instead of being added to the frontier. The new algorithm, called GRAPH-SEARCH, is shown informally in Figure 3.7. The specific algorithms in this chapter draw on this general design.

![[Figure 3.8.png]]![[Figure 3.9.png]]

## Infrastructure for [[Search Algorithm]]
## Node
____
In the node $n$ of the tree, there is four components:
**State**: The state in the state space to which the node corresponds
**Parent**: The node in the search tree that generated this node
**Action**: The action that was applied to the parent to generate the node
**Path-Cost**: The cost traditionally denoted by $g(n)$, of the path form the initial state to the node, as indicated by the parent pointer

![[Figure 3.10 Nodes.png]]

## Frontier
___
Now there is nodes, we need somewhere to put them. The frontier needs to be stored in such a way that the search algorithm can easily choose the next node to epxand accoridng to its preferred strategy. The appropriate data structure is a [[Queue]]. 

**Different Actions:**
1. return true only if there are no more elements in the queue
2. remove the first element of the queue and return it
3. insert an element and return the resulting queue

The explored set can be implemented with a **hash table** to allow efficient checking for repeated states. With a good implementation, insertion and lookup can be done in roughly constant time no matter how many states are stored.