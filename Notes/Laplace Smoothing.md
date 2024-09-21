Laplace smoothing is a technique to handle zero probabilities in probabilities models. It is commonly used to estimate probabilities for unseen events in a dataset. 

# Problem
____
For [[Naive Bayes']] where multiplying probabilities are used to find a query,  a single zero probability can nullify the entire product. This leads to incorrect results. 

# Laplace Smoothing
____
To address this issue, add small non-zero probabilities to all possible events to ensure no event has a zero probability.
$$P_{LAP}(x)=\frac{c(x)+1}{\sum_x[c(x)+1]}=\frac{c(x)+1}{N+|X|}$$
- c(x) is the number of times $x$ appears
- N is the total number of parameters 
- |X| is the total number of unique appearances, this normalizes the probabilities
- adding one ensures that there $P_{LAP} =0$
  
## Example 
____
Suppose the sample is $(red,red,blue)$
$P_{ML}(X):$
	$Red:2/3$
	$Blue:1/3$
$P_{LAP}(X)$:
	$Red: 3/5$
	$Blue: 2/5$
	The denom. is 5 because there are two unique appearance (blue and red). Therefore, |X| is 2. 

# Extended Laplace Smoothing
____
$$P_{LAP}(x)=\frac{c(x)+k}{N+k|X|}$$
Given that the $N=(red,red,blue)$, e.g.$<Red,Blue>$
$P_{LAP,0}(X)=<\frac{2}{3},\frac{1}{3}>$
$P_{LAP,1}(X)=<\frac{3}{5},\frac{2}{5}>$
$P_{LAP,100}(X)=<\frac{2+100}{3+100(2)},\frac{1+100}{3+100(2)}>=<\frac{102}{203},\frac{101}{203}>$

## Conditionals
_____
Smooth each condition independently
$$P_{LAP}(x|y)=\frac{c(x,y)+k}{c(y)+k|X|}$$
