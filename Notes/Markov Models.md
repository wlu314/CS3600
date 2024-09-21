Graphical Model that models sequence of observation. Value of X at a given time is called the **state**.
![[Markov Model.png]]
Parameters: called transition probabilities or dynamics, specify how the state evoles over time (initial state probabilities) 
Stationary Assumption: Transition probabilities the same over at all times

### Joint Distribution of a Markov Model
____
**Joint Distribution**: $$P(X_1,X_2,X_3,X_4)=P(X_1)P(X_2|X_1)P(X_3|X_2)P(X_4|X_3)$$
**General**: $$P(X_1,X_2,...,X_T)=P(X_1)P(X_2|X_1)P(X_3|X_2)...P(X_T|X_{T-1})$$ 
$$=P(X_1)\Pi_{t=2}^{T}P(X_t|X_{t-1})$$

- Past and future independent of the present
- Each time step only depends on the previous 
- called first order Markov property 

## Mini Forward Algorithm
____
How to find $P(X)$ on some $state = t$.
$P(x_1)=known$
$P(x_t)=\sum_{x_{t-1}} P(x_{t-1},x_t)= \sum_{x_{t-1}}P(x_t|x_{t-1})P(x_{t-1})$

## Stationary Distributions
____
- For most chains, influence of the initial distribution gets less and less over time. The distribution we end up in is independent of the initial distribution.
- The distribution we end up with is called the **stationary distribution**  $P_{\infty}$of the chain. It satisfies $$P_{\infty}(X)=P_{\infty +1}(X)=\sum_{\infty}P(X|x)P_{\infty}(x)$$
**Calculating P(X) when t = infinity**
____
![[Markov Model - Infinity.png| 200]]
$P_{\infty}(sun)=P(sun|sun)P_{\infty}(sun)+P(sun|rain)P_{\infty}(rain)$
$P_{\infty}(rain)=P(rain|sun)P_{\infty}(sun)+P(rain|rain)P_{\infty}(rain)$

$P_{\infty}(sun)=0.9P_{\infty}(sun)+0.3P_{\infty}(rain)$
$P_{\infty}(rain)=0.1P_{\infty}(sun)+0.7P_{\infty}(rain)$

$P_{\infty}(sun)=3P_{\infty}(rain)$
$P_{\infty}(rain)=1/3P_{\infty}(sun)$ 

$P_{\infty}(sun)+P_{\infty}(rain)=1$ 

$P_{\infty}(sun)=3/4$
$P_{\infty}(rain)=1/4$

## Application
____
Early Web: Each web page is a state. Initial distribution uniform over pages. With probability c, uniform jumps to random pages. With probability 1-c, follow a random outlink. 

