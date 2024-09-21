**Adversarial Search** problems can be represented when there are two or more agents have conflicting goals. Games such as chess, Go, and poker are easily to represent and agents have actions they can take which results are precise. For each state where we choose to stop searching, we ask who is wining. We use a heuristic evaluation function to estimate who is winning based on features of the state.  
# Two Player Games
____
Two players are called $MAX$ and $MIN$. $MAX$ moves first, and then the players take turns moving until the game is over. At the end of the game, points are awarded to the winning player and penalties are given to the loser. A game can be defined by the following elements. 
- $s_0$ is the initial state
- $TO-MOVE(s)$: the players whose turn it is to move in state $s$
- $ACTION(s)$: The set of legal moves in state $s$ 
- $RESULT(s,a)$: The transition model which defines the state resulting from taking action $a$ and in state $s$
- $IS-TERMINAL(s)$: A terminal test which is true when the game is over and false otherwise. States where the game has ended are called terminal states. 
- $UTILITY(s,p)$: A utility/objective/payoff function which defines the final numeric value to player $p$ when the game ends in the terminal state $s$. For example, the outcome is a win, loses or draw with the values 1, 0, or 1/2. 

## Optimal Decision in Games
___
$MAX$ wants to find a sequence of actions leading to a win. $MAX's$ strategy must be a condition plan - a contingent strategy specifying a response to each of $MIN's$ possible moves. Given a game tree, the optimal strategy can be determined by working out the minimax value of each state in the tree. The minimax value is the utility for MAX of being in that state. The minimax value of a terminal state is just its utility. In a non-terminal state, $MAX$ prefers to move to a state of maximum value when it is $MAX's$ turn to move and $MIN$ prefers a state of minimum value. The terminal nodes on the bottom level get their utility value form the game's utility function.

![[Figure 5.3.png]]\
![[MAX-Min tree.png]]
## Alpha-Beta Pruning
____
The number of game state is exponential in the depth of the tree. No algorithm can completely eliminate the exponent, but we can sometimes cut it in half, computing the correct minimax decision without examining every state by **pruning** large parts of the tree that make no difference to the outcome.
![[Figure 5.5.png]]
- (a) The first leaf below $B$ has the value 3. Hence node $B$ which is a $MIN$ node has the value of AT MOST 3. 
- (b) The second leaf below node $B$ has a value of 12. $MIN$ would avoid this move, so the value of $B$ is still AT MOST 3.
- (c)  The second leaf below node $B$ has a value of 8. $MIN$ would avoid this move, so the value of $B$ is still AT MOST 3. After seeing all of B's successor states, the value of B is exactly 3.
- (d) The first leaf below node $C$ has the value 2. Hence node $C$ which is a $MIN$ node has the value of at MOST 2. Since B is worth 3, the MAX will never choose $C$. So you don't to look at the successor states. 
- (e) The first leaf below $D$ has the value of 14, so D is worth AT MOST 14. This is still higher than MAX's best alternative (3), so we keep exploring D's successors. Notice that we now have bounds on all the successors of the roots so the root's value is at MOST 14. 
- (f) The second successor of $D$ is worth 5, keep exploring. The third successor is worth 2, so $D$ is worth exactly 2. MAX's decision at the root is move to $B$ giving it a value of 3.

Alpha-beta pruning can be applied to trees of any depth, and it's often possible to prune entire subtrees rather than just leaves. 