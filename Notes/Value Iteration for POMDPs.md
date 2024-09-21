[[Value Iteration]] algorithm computes one utility value for each state in regular MDPs. Because the belief state is continuous, there are infinitely many belief states. Instead of normal value iterations, POMDPs require conditional plans and how the expected utility of executing a fixed conditional plan varies with the initial belief state. 

Consider an optimal policy $\pi^*$ and its application in specific belief state $b$. The policy generates an action then for each subsequent percept, the belief state is updated and a new action is generated. For this specific belief state, the policy is exactly equivalent to a **conditional plan**. A conditional plan and expected utility executes a fixed conditional plan varying on the initial belief state.  

## Observations
____
1. The utility of executing a fixed conditional plan $p$ starts in a physical state $s$ be $a_p(s)$. Expected utility of executing $p$ in the belief state $b$ is $\sum_{s}b(s)a_p(s)$ or $b\cdot a_p$. They are both vectors. The expected utility of a fixed conditional plan varies linearly with $b$.
2. For any given belief state $b$, the optimal policy will choose to execute the conditional plan with the highest expected utility. The expected utility of $b$ under the optimal policy is just the utility of that conditional plan:
   $$U(b)=U^{\pi*}(b)=max_pb\cdot a_p$$
   If the optimal policy $\pi^*$ chooses to execute $p$ starting $b$, then it's reasonable to expect that it might choose to execute $p$ (fixed conditional plan) in belief states that are very close to $b$.

Conclusion: These observations led us to see that the utility function $U(b)$ on belief states being the maximum of a collection of hyperplanes will be *piecewise linear* and *convex*. 

## Example 
_____
![[Figure 17.8.png]]Using a simple two-state world. The state are labeled 0 and 1, $R(0)=0$ and $R(1)=1$. There are two actions. Stay with a probability 0.9 and Go to switch to another state with probability of 0.9. The discount factor is $\gamma = 1$ and the sensor reports the correct state with a probability of 0.6. The agent should Stay when it thinks it's in state 1 and Go when it thinks it's in state 0. 

$$a_{[Stay]}(0)= R(0)+\gamma (0.9R(0))+0.1R(1)) =0.1$$
$$a_{[Stay]}(1)= R(1)+\gamma (0.9R(1))+0.1R(0)) =1.9$$
$$a_{[Go]}(0)= R(0)+\gamma (0.9R(1))+0.1R(0)) =0.9$$
$$a_{[Go]}(1)= R(1)+\gamma (0.9R(0))+0.1R(1)) =1.1$$
The bold line represents the utility function for the finite horizon problem that allows one action. The optimal action is the first action of the corresponding conditional plan. The optimal **one step policy** is Stay when b(1) > 0.5 and Go otherwise. 

After calculating the utilities for all the conditional plans $p$ at depth 1 in each physical state $s$ we can compute utilities for all conditional plans of depth 2 by considering each possible first action, each possible subsequent percept and then each way of choosing a depth 1 plan to execute for each percept. 

## Dominated Plan
____
There are 8 distinct depth 2 plans and their utilities are show in Figure 17.8(b). Dashed lines are suboptimal - these plans are **dominated** and are not considered. The four undominated plans each of which is optimal in a specific region in (c) partition the belief-state space. 

For **depth 3**, and so on, there is a general formula. In genera , let $p$ be a depth $d$ conditional plan whose initial action is $a$ and whose depth-$d - 1$  subplan for percept $e$ is $p.e$; then $$a_p(s)=R(s)+\gamma (\sum_{s'}P(s'|s,a)\sum_eP(e|s')a_{p.e}(s'))$$This recursion gives the value iteration algorithm.
![[Figure 17.9 VValue Iteration Fromula for POMDP.png]]
## Complexity
___
The algorithm depends on how many plans get generated. Given |A| actions and |E| observations, there are $|A|^{O(|E|^{d-1})}$ distinct depth-$d$ paths. The algorithm is inefficient for larger problems. Given $n$ conditional plans at level $d$, the algorithm constructs $|A|\cdot n^{|E|}$ conditional plans at level $d+1$ before eliminating the dominated ones. Because the complexity is so bad, look ahead search is an approximate method for solving POMDPs.
### Online Agents for POMDP
____
The transition and sensor models are represented by a dynamic Bayesian network (DBN). The DBN is extended with decision and utility nodes in decision network. The resulting model is called a **dynamic decision network** or DDN. A filtering algorithm is used to incorporate each new percept and action and to update the belief state representation. Decision are made by projecting forward possible action sequences and choosing the best one. 

The single state $S_t$ becomes a set of state variables $X_t$, and there may be multiple evidence variable $E_t$. We will use $A_t$ to refer to the action at time $t$, so the transition model becomes $P(X_{t+1}|X_t,A_t)$ and the sensor model becomes $P(E_t|X_t)$. The reward is $R_t$ to refers to the reward received at time $t$ and $U_t$ to refer to the utility of the state at time $t$. ![[Figure 17.10 Dynamic Desicison Network..png]]

![[Figure 17.11.png]]
- This shows the search tree of the three-step look ahead DDN in Figure 17.10.
- **Triangular Node** is a belief state the agent makes a decision
- **Round Node** corresponds to the choices by the environment. 
- Belief state in triangular node can be computed by applying **filtering algorithm** to the sequence of percepts and actions leading to it.
- A decision is extracted from the search tree by backing up the utility values from the leaves. It takes the average at the chance node and the taking the maximum at the decision nodes.
- The time complexity of an exhaustive search to depth $d$ is $O(|A|^d · |E|^d)$ . $|A|$ is the number of available actions and $|E|$ is the number of possible percepts. 