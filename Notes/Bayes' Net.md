![[Bayes Nets.png]]
## Ghostbuster State
___
Two distributions:
- Prior distribution over ghost location: $P(G)$
	- Lets say this is uniform 
- Sensor reading model: $P(R|G)$
	- Given: we know what our sensors do
	- R = reading color measured

## Independence
_____
Two variables are independent if: $\forall x,y:P(x,y)=P(x)P(y)$
- This says that their joint distribution factors into a product two simpler distribution.
- Another form: $\forall x,y :P(x|y) = P(x)$
- $P(x|y)=\frac{P(x,y)}{P(y)}=\frac{P(x)\cancel{P(y)}}{\cancel{P(y)}}=P(x)$
- $X\perp \!\!\! \perp Y$

![[Independent.png]]
$W$ and $T$ are not independent. Coin flips are independent.
![[Conditional Independent.png]]
- X is conditionally independent of Y given Z ($X\perp \!\!\! \perp Y|Z$) if and only if $$\forall x,y,z:P(x,y|z)=P(x|z)P(y|z)$$ or equivalently, if and only if $$\forall x,y,z:P(x|z,y)=P(x|z)$$

## Bayes' Nets
____
Two problems using full joint distribution tables as our probabilisitic models:
- Joint is way too big to represent explicitly
- Hard to learn (estimate) anything empirically about more than a few variables at a time.

Bayes' Nets: describes complex joint distributions (models) using simple, local distribution (conditional probabilities)
- More properly called graphical models
- Describe how variables locally interact
- Local interactions chain together to give global, indirect interactions.

![[Bayes' Nets Insurance Example.png]]*This is the Bayes' Net of an insurance graph*

## Bayes' Net Semantics
____
- A set of nodes, one per variables X
- A direct, acyclic graph 
- A conditional distribution for each node
	- A collection of distribution over X, one for each combination of parents' values $$P(X|a_1...a_n)$$
	- conditional probability table
	- description of a noisy process
![[Bayes' Net Semantics.png | 200]]
### Probabilities in Bayes' Nets 
_____
BNs' implicitly encodes joint distributions. As a product of local conditional distributions. To get probability a BN gives a full assignment, multiply all the relevant conditionals together:
$$P(x_1,x_2,...x_n)=\Pi_{i=1}^{n}P(x_i|parents(X_i))$$![[Probability in BNs Example.png | 200]]
$P(Cavity, Toothache, Catch)=P(Cavity) * P(Toothache|Cavity)* P(Cavity|Catch)$
![[Bayes Net - Alarm Network.png]]![[Alarm Network Query.png]]

### Probabilistic Inference
____
- [[Inference By Enumeration]] (exact, exponential complexity)
- Variable elimination (exact , worse-case exponential complexity, often better)
- Inference is NP-complete
- Sampling (approximate)

#### Inference
____
Inference means to calculate some useful quantity from a join probability distribution. The more hidden variables that need to be summed out will increase the the complexity. 

**Examples**: 
Posterior probability: $P(Q|E_1=e_1,...E_k=e_k$
Most likely explanation: $argmax_q P(Q=q|E_1=e_1...)$

![[Inference by Enumeration 1.png| 200]]
$P(B|+j,+m)\space  \alpha_B P(B,+j,+m)$  This statement with $\alpha _B$ represents they are proportional by some multiplication constant. 

To get this query, I will get the joint distribution and sum out alarm and earthquake. 
$$\sum_{e,a}P(B,e,a,+j,+m)=\sum_{e,a}P(B) \space P(e)\space P(a|B,e) \space P(+j|a) \space P(+m|a)$$
At the end, you would need to normalize ($1/Z$). 
![[Inference By Enumeration 2.png]]
$$P(B|+j,+m)\space = \frac{1}{Z}P(B,+j,+m)=\frac{1}{P(+j,+m)}P(B,+j,+m)$$

### Variable Elimination

#### Preliminary Information
____
**Joint distribution**: $P(X,Y)$
- Entries $P(x,y)$ for all $x,y$
- Sums to 1

**Selected Joint**: $P(x,Y)$
- A slice of a joint distribution
- Entries $P(x,y)$ for fixed x, all y
- Sums to $P(x)$
![[Variable Elimination.png| 200]]
**Single Conditional**: $P(Y|x)$
- Entries $P(y|x)$ for fixed x, all y
- sums to 1
- Under the conditions cold, what are the possibilities. 
![[Single Conditionals.png| 200]]
**Family of Conditionals**: $P(X|Y)$
- Multiple conditioanls
- Entries $P(x|y)$ for all $x,y$
- Sums to $|Y|$
![[Family of Conditionals.png | 300]]
**Specified Family**: $P(y | X)$
- Entries $P(y|x)$ for fixed y but for all x
![[Specified Family.png| 200]]
##### Example
![[Traffic Domain Example.png]]
- Track objects called factors
- Initial factors are local CPTs (one per node)
- Any known values are selected $L=+l$
- ![[Example Variable Elimination.png | 300]] You can see that the last table is change where $-l$ entries are eliminated. 

### Operation 1: Join Factors
____
- Get all factors over the joining variable
- Build a new factor over the union of the variables involved

![[Join Factors.png]]

**Example of Multiple Joins**
___
![[Example of Multiple Joins.png]]

### Operation 2: Eliminate
____
Marginalization: Take a factor and sum out a variable. Shrink a factor to a smaller one. A projection operation. 
![[Example Marginalization.png | 300]]
**Multiple Elimination**
____
![[Example of Multiple Elimination.png]]

### Difference
____
![[Example Difference.png]]
The difference lies in the order the sum is taken

**Variable Elimination Procedure** 
______
![[Example Marginalizing.png]]

**Evidence - Initial Factors**
____
![[Example - Evidence.png]]![[Example VE.png]]


### General Variable Elimination
______
Query: $P(Q|E_1=e_1,...E_k=e_k)$
Start with initial factors: Local CPTs
Hidden Variables:
- Pick a hidden variable H
- Join all factors mentioning H
- Eliminate H
Join all remaining factors and normalize

**Example of VE**
______
![[Example of VE.png]]

**In Math Equations**
_____
![[Example VE in Math.png]]

**Variable Elimination Ordering**
____
Eliminating ordering affects the time complexity. The computational and space complexity of variable elimination is determined by the largest factor. 
![[Variable Elimination Ordering.png | 300]]

