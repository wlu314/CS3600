In [[Solving Problems using Search]], it's designed to explore search spaces by finding the path to the goal that constitutes a solution to the problem. However, in other problems, like the 8-queens problem, the final configuration of queens matter and not the order they are added. Same can be said about network optimization, portfolio management, automatic programming, and etc. 

If the path is not relevant to the goal, a different set of algorithms are needed. **Local Search** algorithms operate using a single **current node** and move only to the neighbors of that node. Paths are not retained. The *advantages* of local search is that: they use very little memory, and they find reasonable solution in large state spaces.  

## Continuous Space
____
Because continuous spaces can have infinite branching factors algorithms like hill climbing and [[Simulated Annealing]] can handle continuous state and action spaces.  I'll use an example of placing three new airports to minimize the sum of squared distance from each city. The **objective function** $f(x_1,y_1,x_2,y_2,x_3,y_3)$ minimizes the sum of squared distance from each city. Let $C_i$ be the set of cities whose closest airport is airport $i$. 
![[Local Search.png]]
This expression gets the set of cities closest to the airport. **Gradient** of the landscape is used to find the maximum. The gradient of the object function is a vector $\nabla f$ that gives the magnitude and direction of the steepest slope. $∇f=[∂f/​∂x_1​,∂f​∂/y_1​,∂f/​∂x_2​,∂f​∂/y_2​​,∂f/​∂x_3,∂f​∂/y_3​]$. You can find them maximum by solving $\nabla f=0$. 
$x \leftarrow x + \alpha \nabla f(x)$

where $\alpha$ is a small constant often called the step size. In other cases, the objective function might not be available in a differentiable form at all—for example, the value of a particular set of airport locations might be determined by running some large-scale economic simulation package. In those cases, we can calculate a so-called empirical gradient by evaluating the response to small increments and decrements in each coordinate. Empirical gradient search is the same as steepest-ascent hill climbing in a discretized version of the state space.

Hidden beneath the phrase “$\alpha$ is a small constant” lies a huge variety of methods for adjusting $\alpha$. The basic problem is that, if \(\alpha\) is too small, too many steps are needed; if $\alpha$ is too large, the search could overshoot the maximum. The technique of line search tries to overcome this dilemma by extending the current gradient direction—usually by repeatedly doubling $\alpha$—until $f$ starts to decrease again. The point at which this occurs becomes the new current state. There are several schools of thought about how the new direction should be chosen at this point.

For many problems, the most effective algorithm is the venerable Newton-Raphson method. This is a general technique for finding roots of functions—that is, solving equations of the form \(g(x) = 0\). It works by computing a new estimate for the root \(x\) according to Newton’s formula

$x \leftarrow x - \frac{g(x)}{g'(x)}$

To find a maximum or minimum of $f$, we need to find $x$ such that the gradient is zero (i.e., $(\nabla f(x) = 0$ Thus, $g(x)$ in Newton’s formula becomes $\nabla f(x)$, and the update equation can be written in matrix–vector form as

$x \leftarrow x - H_f^{-1}(x) \nabla f(x)$

where $H_f(x)$ is the Hessian matrix of second derivatives, whose elements $H_{ij}$ are given by $\frac{\partial^2 f}{\partial x_i \partial x_j}$. For our airport example, we can see from Equation (4.2) that $H_f(x)$ is particularly simple: the off-diagonal elements are zero and the diagonal elements for airport $i$ are just twice the number of cities in $C_i$. A moment's calculation shows that one step of the update moves airport $i$ directly to the centroid of $C_i$, which is the minimum of the local expression for $f$ from Equation (4.1). For high-dimensional problems, however, computing the $n^2$ entries of the Hessian and inverting it may be expensive, so many approximate versions of the Newton-Raphson method have been developed.

Local search methods suffer from local maxima, ridges, and plateaux in continuous state spaces just as much as in discrete spaces. Random restarts and simulated annealing can be used and are often helpful. High-dimensional continuous spaces are, however, big places in which it is easy to get lost.

A final topic with which a passing acquaintance is useful is constrained optimization. An optimization problem is constrained if solutions must satisfy some hard constraints on the values of the variables. For example, in our airport-siting problem, we might constrain sites
to be inside Romania and on dry land (rather than in the middle of lakes). The difficulty of constrained optimization problems depends on the nature of the constraints and the objective function. The best-known category is that of linear programming problems, in which con- straints must be linear inequalities forming a convex set 8 and the objective function is also linear. The time complexity of linear programming is polynomial in the number of variables.

Linear programming is probably the most widely studied and broadly useful class of optimization problems. It is a special case of the more general problem of convex optimization, which allows the constraint region to be any convex region and the objective to be any function that is convex within the constraint region. Under certain conditions, convex optimization problems are also polynomially solvable and may be feasible in practice with thousands of variables. Several important problems in machine learning and control theory can be formulated as convex optimization problems (see Chapter 20).

#### Objective Function 
____
![[Figure 4.1 Objective Function.png | 600]]
To understand local search, we find it useful to consider the state-space landscape (as in Figure 4.1). A landscape has both “location” (defined by the state) and “elevation” (defined by the value of the heuristic cost function or objective function). If elevation corresponds to cost, then the aim is to find the lowest valley—a global minimum; if elevation corresponds to an objective function, then the aim is to find the highest peak—a global maximum. (You can convert from one to the other just by inserting a minus sign.) Local search algorithms explore this landscape. A complete local search algorithm always finds a goal if one exists; an optimal algorithm always finds a global minimum/maximum.

#### [[Hill-Climbing Search]]
____
![[Figure 4.2 Hill Climbing.png]]
This algorithm moves in the direction of increasing value - uphill. It terminates when it reaches a peak where no neighbor has a higher value. This is sometimes called **greedy local search** as it grabs a good neighbor state without looking further. 

Many variants of hill climbing have been invented. **Stochastic hill climbing** chooses at random from among the uphill moves; the probability of selection can vary with the steepness of the uphill move. This usually converges more slowly than steepest ascent, but in some state landscapes, it finds better solutions. **First-choice hill climbing** implements stochastic hill climbing by generating successors randomly until one is generated that is better than the current state. This is a good strategy when a state has many (e.g., thousands) of successors.

The hill-climbing algorithms described so far are incomplete—they often fail to find a goal when one exists because they can get stuck on local maxima. **Random-restart hill climbing** adopts the well-known adage, “If at first you don’t succeed, try, try again.” It con- ducts a series of hill-climbing searches from randomly generated initial states,1 until a goal is found. It is trivially complete with probability approaching 1, because it will eventually generate a goal state as the initial state. If each hill-climbing search has a probability p of success, then the expected number of restarts required is 1/p. For 8-queens instances with no sideways moves allowed, p ≈ 0.14, so we need roughly 7 iterations to find a goal (6 fail- ures and 1 success). The expected number of steps is the cost of one successful iteration plus (1−p)/p times the cost of failure, or roughly 22 steps in all. When we allow sideways moves, 1/0.94 ≈ 1.06 iterations are needed on average and (1 × 21) + (0.06/0.94) × 64 ≈ 25 steps. For 8-queens, then, random-restart hill climbing is very effective indeed. Even for three mil- lion queens, the approach can find solutions in under a minute.2

The success of hill climbing depends on the shape of the state-space landscape. If there is few local maxima and plateaux, random restart hill climbing will find a solution quickly. NP-hard problems typically have an exponential number of local maxima to get stuck on. Despite this, a reasonably good local maximum can often be found after a small number of restarts. [[Simulated Annealing]] could potentially help with the local maxima problem by increasing greediness overtime. 

Instead of keeping one node in memory, [[Local Beam Search]] keeps track of $k$ states rather than just one. 
#### Definition
___
**Local Maxima**: Local Maximum is a peak that is higher than each of its neighboring states but lower than the global maximum. Hill-climbing algorithm that reach the vicinity of a local max will be upwards but will be stuck. 
**Ridges**: A sequence of local maxima that is very difficult for greedy algorithms to navigate. 
**Plateaux**: A flat area of state space landscape. No uphill exist. 