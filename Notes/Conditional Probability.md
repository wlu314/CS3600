A relation between joint and conditional probabilities. 

$P(a|b)=\frac{P(a,b)}{P(b)}$

![[Conditional Probability.png | 400]]

Given that we know when $b$ happens, what is the probability that $a$ happened. 


![[Conditional Probability Table.png]]

## Summing out of Conditionals
____
Summing over all values of a conditional distribution is equal to 1. 
$$P(-a|+b)+P(+a|+b)=\frac{P(+b)}{P(+b)}=1$$

## Normalizing Trick
____
Changing from a joint distribution to a conditional distribution
![[Courses/CS-3600/Notes/Normalizing Trick.png]]
![[Normalizing Trick 1.png]]![[Normalizing Trick 2.png]]



### Questions
_____
![[Conditional ProbabilityQuestions.png]]
- $P(+a,+b,+c)=P(+a)\cdot P(+b|+a) \cdot P(+c|+b)= 1/2 * 1/10 * 4/5=1/4$ 