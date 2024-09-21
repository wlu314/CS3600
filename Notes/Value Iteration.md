This is an algorithm to calculate the optimal policy. The idea is to calculate the utility of each state and then use the state utilities to select an optimal action in each state. 

## Bellman Equation
___
Instead of defining the utility of being in a state as the expected sum of discounted rewards from that point onwards in [[Sequential Decision Problems]] talking. **Bellman Equation** says that the utility of a state is the immediate reward for that state plus the expected discounted utility of the next state assuming the agent chooses the optimal action. 
$$U(s) = R(s)+\gamma \space max \space \sum_{s'} P(s'|s,a)U(s')$$
![[Figure 17.1.png]]
For example, the equation for the state $(1,1)$ is 
![[Figure 17.1 Bellman Eqation.png]]
![[Figure 17.4.png]]If there are $n$ possible states, then there are $n$ Bellman equations, one for each state. The $n$ equations contain $n$ unknowns - the utilities of the states. The equations are not linear. Value iteration algorithm propagates information through the state space by local updates. 
### Convergence
____
The value iteration converges to a unique set of solutions of the Bellman Equation. Value iteration converges is the notion of **contraction**. A contraction is a function of one argument that when applied to two different inputs, produces two outputs that are closer together. 


### Manual Calculation of Value Iteration
_____
https://www.youtube.com/watch?v=wIloocUqL-E&list=PL5gYI166VpDY6n0BGxNBkB-t1O0z4RmrJ&index=8 at video 1:20:00