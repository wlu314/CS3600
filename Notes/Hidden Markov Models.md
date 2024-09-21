 ![[HMM.png | 300]]
 Instead of observing them through states, they are observed through noisy evidence variables.

## Aspects
____
**Initial Distribution**: $P(X_1)$
**Transitions**: $P(X_t|X_{t-1})$ 
**Emissions**: $P(E_t|X_t)$ 
*both transitions and emissions have tables corresponding to the variables.*

## Markov Assumption
____
The current state $X_t$ depends on a few finite fixed number of previous states. $P(X_t|X_{0:t-1})=P(X_t|X_{t-1})$

The sensor model gives evidence variable $E_t$ which could depend on previous variables as well as current state variables. The sensor Markov Assumption is $P(E_t|X_{0:t},E_{1:t-1})=P(E_t|X_t)$. $P(E_t|X_t)$ is the sensor model or observation model

Given the prior probability at time 0, $P(X_0)$ we hae specification of the complete joint distribution over all variables. $$P(X_{0:t},E_{1:t})=P(X_0) \Pi_{i=1}^t P(X_i|X_{i-1})P(E_i|X_i)$$
### Joint Distribution 
____
$$P(X_1,E_1,X_2,E_2,X_3,E_3)=P(X_1)P(E_1|X_1)P(X_2|X_1)P(E_2|X_2)P(X_3|X_2)P(E_3|X_3)$$
In General: 
$$P(X_1,E_1,...,X_T,E_T)=P(X_1)P(E_1|X_1)\Pi_{t=2}^{T}P(X_t|X_{t-1})P(E_t|X_t)$$

### Conditional Independencies
____
![[HMM.png | 300]]
$E_1\perp\!\!\!\perp \ X_2,E_2,X_3,E_3,...|X_1$ 

$P(X_1|e_1)$
	$=P(x_1|e_1)=P(x_1,e_1)/P(e_1)$
	$= \propto x_1 \space P(x_1,e_1)$
	$=P(x_1)P(e_1|x_1)$
$P(X_2)$
	$P(x_2)=\sum_{x_1}P(x_1,x_2)$
	$=\sum_{x_1}P(x_1)P(x_2|x_1)$
## Inference
____
Current belief P(X| evidence to date)
$$B(X_t)=P(X_t|e_{1:t})$$
After one time step passes
$$P(X_{t+1}|e_{1:t})=\sum_{x_t}P(X_{t+1},x_t|e_{1:t})$$
$$=\sum_{x_t}P(X_{t+1}|x_t,e_{1:t})P(x_t|e_{1:t})$$
$$=\sum_{x_t}P(X_{t+1}|x_t) P(x_t|e_{1:t})$$
Compactly
$$B'(X_{t+1})=\sum_{x_t}P(X'|x_t)B(x_t)$$
B is the post observation (after observing evidence) and B' is you're pre-observation. 
![[HMMs.png]]![[HMMs Example.png]]
By using this algorithm, it updates at each state based on the belief from B' to B and then from B to B' 

## Forward Algorithm
![[HMMs Forward Algorithm.png]]



### Example - Forward Algorithm
____
![[Figure 14.2.png]]
$P(R_0)=<0.5,0.5>$, On day 1, the umbrella is true so $U_1=true$. The prediction from $t=0$ to $t=1$ is $P(R_1)=\sum_{r_0}P(R_1|r_0)P(r_0)=<0.7,0.3>\times 0.5+<0.3,0.7> \times 0.5 = <0.5,0.5>$
$P(R_1|u_1)=\alpha P(u_1|R_1)P(R_1)=\alpha <0.9,0.2><0.5,0.5>=\alpha <0.45,0.1>=<0.818,0.182>$

### Likelihood
_____
The forward recursion can compute the likelihood of the evidence sequence $P(e_{1:t})$. $l_{1:t}(X_t)=P(X_t,e_{1:t})$. The calculation is identical to that for filtering $$l_{1:t+1}=FORWARD(l_{1:t},e_{t+1})$$ Having computed $l_{1:t}$ we obtain the actual likelihood by summing out $X_t$
$$L_{1:t}=P(e_{1:t})=\sum_{x_t}l_{1:t}(x_t)$$


[[Viterbi Algorithm]]
