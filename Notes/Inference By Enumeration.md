## Variables
___
Evidence Variables: $E_1...E_k=e_1...e_k$
Query* Variables: $Q$
Hidden Variables: $H_1...H_r$

The goal is to find $P(Q,e_1...e_k)$.

## Algorithm
___
1. Select the entries consistent with the evidence 
2. Sum out the hidden variables to get joint Query and evidence $$P(Q,e_1...e_k)=\sum_{h_1...h_r}P(Q,h_1...h_r,e_1...e_k)$$This process can be found in [[Conditional Probability]]
3. Normalize $$\frac{1}{Z}$$$$Z=\sum_qP(Q,e_1...e_k)$$ $$P(Q|e_1...e_k)=\frac{1}{Z}P(Q,e_1...e_k)$$
## Example
![[Courses/CS-3600/Notes/Inference by Enumeration.png]]
$P(W|winter,hot)=0.1+0.05=0.15$
$P(Sun|winter, hot)=\frac{0.10}{0.15}$
$P(Rain|winter,hot)=\frac{0.05}{0.15}$

## Problems
_____
Let $n$ be the number of variables in the network. Let $d$ be the maximum number of possible values each variable can take.

Time Complexity: $O(d^n)$
Space Complexity: $O(d^n)$ to store the joint distribution

