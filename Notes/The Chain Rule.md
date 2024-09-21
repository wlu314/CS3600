Joint distribution can be written as an incremental product of conditional distributions.
$$P(x_1,x_2,x_3)=P(x_1)P(x_2|x_1)P(x_3|x_1,x_2)$$
$$P(x_1,x_2,...,x_n)=\Pi_iP(x_i|x_1...x_{i-1})$$
## Explain
____
$P(x_1)P(x_2|x_1)P(x_3|x_1,x_2) = P(x_1)\frac{P(x_2,x_1)}{P(x_1)}\frac{P(x_3,x_2,x_1)}{P(x_2,x_1)}=P(x_1,x_2,x_3)$ 

$P(x_2|x_1)= \frac{P(x_2,x_1)}{P(x_1)}$ by [[The Product Rule]]. 
