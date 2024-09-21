$score(y,x)=w_y\cdot f(x)$
	$=(\sum_i a_{i,y}f(x_i)) \cdot f(x)$
	$=\sum_i a_{i,y}(f(x_i) \cdot f(x))$
	$=\sum_i a_{i,y} K(x_i,x)$
*The weighted combination of dot product of training example and test example* 

# Learning in Dual Perceptron
_____
- Start with zero counts (alpha) 
- Pick up training instance one by one
- Try to classify $x_n$ $$y=argmax_y \sum_i a_{i,y} K(x_i,x_n)$$
- if correct, no change
  
$a_{x,y}=a_{x,y}-1$
$a_{x,y ^*}=a_{x,y^*}+1$

## Kernelized Perceptron
____
$K(x_i,x)$ tells us the dot product between $x$ and $x'$. There is no need to ever take dot products (kernel trick). IT allows perceptron to classify data that is not linearly separable.

![[Dual Perceptrons.png]]*the original feature space can always be mapped to some higher-dimensional feature space where the training set is separable*

## Connection with Kernels
____
Kernels map original vectors to higher dimensional spaces, take the dot product there, and. hand the result back.

**Linear Kernel**: $K(x,x')=x' \cdot x' =\sum_i x_i x_i'$
**Quadratic Kernel**: $K(x,x')=(x\cdot x' +1)^2$
**RBF**: $K(x,x')=exp(-||x-x'||^2)$
