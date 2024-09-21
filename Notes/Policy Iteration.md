The **policy iteration** algorithm follows two steps, from beginning with an initial policy $\pi _0$. 
- **Policy Evaluation**: Given a policy $\pi _i$ calculate $U_i=U^{\pi _i}$, the utility of each state if $\pi_i$ were to be executed
- **Policy Improvement**: Calculate the new MEU policy $\pi_{i+1}$ using one step look-ahed based on $U_i$
The algorithm terminates when the policy improvement step yields no change in the utilities. The utility function $U_i$ is a fixed point of the Bellman update, so it's a solution to the Bellman equation, and $\pi_i$ must be an optimal policy. Because there are only finitely many policies for a finite state space, and each iteration can be shown to yield a better policy, policy iteration must terminate.
![[Figure 17.6.png]]
The action in each state is fixed by the policy. At the $i$th iteration, the policy $\pi_i$ specifies the action $\pi_i(s)$ in state $s$. This means that this is a simplified version of the Bellman equation relating the utility of $s$ (under $\pi_i$) to the utilities of its neighbor. $$U_i(s)=R(s)+\gamma \sum_{s'} P(s'|s,\pi_s(s))U_i(s')$$
For example, if $\pi_i$ is the policy in Figure 17.2(a) shown below![[Figure 17.2.png]]Then $\pi_i(1,1)=Up,\pi_i(1,2)=Up,...$ The Bellman equations are:
$$U_i(1,1)=-0.04+0.8U_i(1,2)+0.1U_i(1,1)+0.1U_i(2,1)$$
$$U_i(1,2)=-0.04+0.8U_i(1,3)+0.2U_i(1,2)$$
$$...$$
These equations are linear because the max operator is removed. For $n$ states, we have $n$ linear equations with $n$ unknowns which can be solved in $O(n^3)$ by linear algebra methods. For small state space, policy evaluation using exact solution is the most **efficient** approach. For large state spaces, the time complexity could be an issue. 

Policy evaluation can also perform simplified value iteration steps (simplified because the policy is fixed) to give a reasonably good approximation of the utilities. The simplified Bellman update for this process is $$U_{i+1}(s) \leftarrow R(s) +\gamma \sum_{s'}P(s'|s,\pi_i(s))U_i(s')$$
This is repeated $k$ times to produce the next utility estimate. This algo is called **modified policy iteration**. It's more efficient than standard policy iteration or value iteration.
![[Figure 17.7 Policy Iteration.png]]

The algorithms we have described so far require updating the utility or policy for all states at once. It turns out that this is not strictly necessary. In fact, on each iteration, we can pick any subset of states and apply either kind of updating (policy improvement or simplified value iteration) to that subset. This very general algorithm is called **asynchronous policy iteration**. Given certain conditions on the initial policy and initial utility function, asynchronous policy iteration is guaranteed to converge to an optimal policy. The freedom to choose any states to work on means that we can design much more efficient heuristic algorithms—for example, algorithms that concentrate on updating the values of states that are likely to be reached by a good policy. This makes a lot of sense in real life: if one has no intention of throwing oneself off a cliff, one should not spend time worrying about the exact value of the resulting states.