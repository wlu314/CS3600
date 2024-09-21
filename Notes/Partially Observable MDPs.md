Given that the environment was **fully observable** in Markov Decision Processes, the agent always knows which states it is in. This combined wit the assumption for the transition model means that the optimal policy depends only on the current state. If the environment is **partially observable**, then the agent doesn't know the state it's in. It cannot execute the action $\pi(s)$ for the state. POMDP or **partially observable MDPs** are viewed much more difficult than ordinary MDPs.

## Defining POMDPs
____
**Transition Model**: $P(s'|s,a)$
**Actions**: $A(s)$
**Reward**: $R(s)$
**Sensor Model**: $P(e|s)$ 
	The sensor model specifies the probability of perceiving evidence $e$ in state $s$. For example, the 4x3 world in Figure 17.1 can be converted into a POMDP by adding a noisy or partial sensor instead of assuming the agent knows its location exactly. This sensor could measure the $number \space of \space adjacent \space walls$.
**Belief States**: The set of actual states the agent might be in. In POMDP, the belief state $b$ becomes the $probability \space distribution$ over all possible states. $b(s)$ is the probability assigned to the actual state $s$ by the belief state $b$. By using conditional probability distribution over the actual states given the sequence of percepts and action so far. If $b(s)$ was the previous belief state, and the agent does action $a$ and then perceives evidence $e$, then the new belief state is given by $b'(s')= \alpha P(e|s')\sum_s P(s'|s,a)b(s)$. $\alpha$ is the normalizing constant that makes the belief state sum to 1. By analogy with update operator for **filtering**, $b'=FORWARD(b,a,e)$. 

**Filtering**: Filtering is the task of calculating the new belief state from a previous belief state and the new evidence.

## Example 
![[Figure 17.1.png]]
In this $4 \times 3$  POMDP, suppose the agent moves $Left$ and the sensor report 1 adjacent wall, it's likely the agent is in (3,1). **The optimal action depends only on the agent's current belief state.** Optimal policy can be described by mapping $\pi^*(b)$ from belief states to actions. It *doesn't* depends on the actual state the agent is in. This is because the agent doesn't actually know its state; all it knows is the belief state. The decision cycle of an agent:
1. Given the current belief state $b$, execute the action $a=\pi^*(b)$
2. Receive percept $e$
3. Set the current belief state to $FORWARD(b,a,e)$ and repeat

The POMDP belief stat space is *continuous*, because this state is a probability distribution. 

### Calculating Probability $b\rightarrow b'$
___
Calculate the probability that an agent in belief state $b$ reaches belief state $b'$ after the action $a$. The probability of perceiving $e$, given that $a$ was performed starting in the belief state $b$, is given by summing all the states $s'$ that the agent might reach. 
$$P(e|a,b)=\sum_{s'}P(e|a,s',b)P(s'|a,b)$$
$$=\sum_{s'}P(e|s')P(s'|a,b)$$
$$=\sum_{s'}P(e|s')\sum_{s}P(s'|s,a)b(s)$$
*This is saying what is the sum of probability of reaching the state $s'$ given the evidence of the percept multiplied by the sum of probability to reach s' given action a times the belief state of $s$. 

The probability of reaching $b'$ from $b$ given an action $a$ is $P(b'|b,a)$ then $$P(b'|b,a)=P(b'|a,b)=\sum_eP(b'|e,a,b)P(e|a,b)=\sum_eP(b'|e,a,b)\sum_{s'}P(e|s')\sum_{s}P(s'|s,a)b(s)$$
$P(b'|e,a,b)$ is equal to 1 if $b'=FORWARD(b,a,e)$ and 0 otherwise. The reward function for belief states (i.e. the expected reward for the actual states the agent might be in): $$p(b)=\sum_sb(s)R(s)$$
$P(b'|b,a)$ and $p(b)$ define an observable MDP on the space of belief states. It can be shown that an optimal policy for this MDP, $\pi^*(b)$ is also an optimal policy for the original POMDP. Solving a POMDP on a physical state space can be reduce to solving an MDP on the corresponding belief-state space. This is mainly because belief state is always observable to the agent by definition. Therefore, POMDP can be reduced down to a continuous state spaced MDP. None of the previous algorithms applies to this type of MDP. 

## [[Value Iteration for POMDPs]]
____
[[Value Iteration]] algorithm computes one utility value for each state in regular MDPs. Because the belief state is continuous, there are infinitely many belief states. Instead of normal value iterations, POMDPs require conditional plans and how the expected utility of executing a fixed conditional plan varies with the initial belief state. 