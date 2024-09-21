MDPs from [[Making Complex Decisions]] is called offline learning. Online learning is referred to as reinforcement learning. Model Based idea is such that you learn from an approximate model based on experiences. Solve for values as if the learned model were correct. 

## Passive RL
____
Task is to learn policy evaluation $V^{\pi}(s)$. 
- Input: a fixed policy $\pi(s)$
- $T(s,a,s')$ - not known
- $R(s,a,s')$ - not known
- learn state values

Direction Evaluation can be used to learn the state values. The actions are not offline.
### Direct Evaluation
____
**Goal** is to compute values for each state under the *fixed policy*. The **idea** is to to average together observed sample values. A sample is where you enter into the state/environment until termination acting under the fixed policy. Each time you visit a state, write down what the sum of discounted rewards turned out out to be. 

![[RL.png]]
In episode 4, starting from state E failed such that the state value is less than that of B. However, the two share a symmetric policy of moving to C. This is because there are not enough samples and the values didn't converge yet. 

**Good vs Bad**
- Direct Evaluation eventually computes the correct average values using just sample transitions. Easy to understand without knowing the transition model and reward. 
- It wastes information about state connection. Each state must be learned separately so it takes a long time to learn.
## Temporal Difference Learning 
_____
**Idea** is to update $V(s)$ each time we experience a transition $(s, a, s', r)$. Likely outcomes $s'$ will contribute updates often. The temporal difference learning of values. Policy is still fixed and moves value towards value of whatever successor occurs. 

$Sample \space of \space V(s): \space sample = R(s,\pi(s),s')+\gamma V^{\pi}(s')$
$Update \space to \space V(s): V^{\pi}(s)\leftarrow (1-a)V^{\pi}(s)+(a)sample$
$Same \space update:V^{\pi}(s) \leftarrow V^{\pi}(s) +a(sample -V^{\pi}(s) )$

The **exponential moving average** discounts later experiences. The running interpolation update is $\overline{x}_n=(1-\alpha) \cdot \overline{x}_{n-1}+\alpha \cdot x_n$. It makes recent samples more important.
$$\overline{x}_n=\frac{x_n+(1-a)\cdot x_{n-1} +(1-a)^2\cdot x_{n-2}+...}{1+(1-\alpha)+(1-a)^2+...}$$
The decreasing learning rate (alpha) can give more converging averages. $\alpha =\frac{1}{n}$ where $n$ is the number of samples. 

![[Temporal Difference Learning.png]]
## Active RL
____
Agent is making choices instead of a fixed policy. The **goal** is the learn the optimal policy / values. You don't know the **transitional** **model** or **rewards**. Compared to passive RL, you have to choose an **action instead of a fixed policy**. 

### Q-Value Iteration
____
Value Iteration: find successive (depth-limited) values.

With value iteration: Start with $V_0(s)=0$ you calculate $V_k$ with the depth $k+1$ values for all states. 
$$V_{k+1}(s) \leftarrow max_a\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V_k(s')]$$

But Q-values are **more useful**, so compute them instead. Start with $Q_0(s,a)=0$. Given $Q_k$, calculate the depth $k+1$ q-values for all q-states. 
$$Q_{k+1}(s) \leftarrow \sum_{s'}T(s,a,s')[R(s,a,s')+\gamma max_{a'}Q_k(s',a')]$$
Q-Learning goes as follows: 
- Take an action/sample $(s,a,s',r)$
- Consider your old estimate $Q(s,a)$
- Consider your new sample estimate  $$sample = R(s,a,s')+\gamma max_{a'}Q(s',a')$$
- Incorporate the new estimate into a running average$$Q(s,a) \leftarrow (1-a)Q(s,a,)+(a)[sample]$$
#### Properties of Q-Learning
____
Q-learning converges to optimal policy - even if you're acting sub-optimally. This is called **off-policy learning**. The weaknesses are: 
- You have to explore enough
- The learning rate small enough but not decrease it too quickly. Generally, $\alpha = \frac{1}{n}$. 


## Exploration
____
Several scheme for forcing exploration:
- Simplest: random action ($\epsilon$-greedy)
	- Every time step, flip a coin
	- With (small probability $\epsilon$, act randomly
	- With (large) probability $1-\epsilon$, act on current policy
- Problems
	- You keep acting randomly until learning is done
	- One solution is to lower epsilon over time
	- Also, exploration function can help   


#### Exploration Function
____
Takes a value estimate u and a visit count n and returns an optimistic utility $f(u,n)=u+k/n$ 

Regular Q-Update: $Q(s,a) \leftarrow R(s,a,s') + \gamma max_{a'}Q(s',a')$
Modified Q-Update: $Q(s,a) \leftarrow R(s,a,s') + \gamma max_{a'} f(Q(s',a'),N(s',a'))$
