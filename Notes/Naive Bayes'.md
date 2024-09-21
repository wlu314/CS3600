Naive Bayes assumes all features are independent effects of the label. 

## Example - Simple Digit Recognition
_____
- One feature (variable) $F_{ij}$ for each grid position $<i,j>$
- Feature values are on/off, based on whether intensity is more or less than 0.5 in underlying image
- Each input maps to a feature vector $$1 \rightarrow <F_{0,0}=0 \space F_{0,1}=0\space F_{0,2}=0 ...  F_{15,15}=0$$
- Each feature is binary valued
- Naive Bayes Model $P(Y|F_{0,0}...F_{15,15})\propto P(Y)\Pi_{i,j}P(F_{i,j}|Y)$
![[Naive Bayes.png | 300]]

## General Naive Bayes
____
$$P(Y,F_1,...,F_n)=P(Y)\Pi_i P(F_i|Y)$$
*Building a joint distribution that Y takes on. There are $|Y| \times |F^n|$ values.*  

### Inference for Naive Bayes
____
Compute posterior distribution over label variable Y.
1. Get joint probability of label and evidence for each label
2. Sum to get probability of evidence
3. Normalize by dividing step 1 by step 2
$$P(Y,f_1,..,f_n)=\begin{bmatrix} P(y_1,f_1...f_n) \\ P(y_2,f_1...f_n) \\ ... \\P(y_k, f_1...f_n) \end{bmatrix} \rightarrow \frac{\begin{bmatrix} P(y_1) \Pi_i P(f_1|y_1) \\ P(y_2)\Pi_iP(f_1|y_2) \\ ... \\P(y_k)\Pi_iP(f_i|y_k) \end{bmatrix}}{p(f_1...f_n)}=P(Y|f_1...f_n)$$


#### Parameter Estimation
_____
- Estimate the distribution of a random variable
- Use training data through learning
	- For each outcome $x$, look at the empirical rate of that value $$P_{ML}(x)=\frac{count(x)}{total\space samples}$$
	- If there are three samples, two are red and one are red. Then $P_{ML}(r)=2/3$

 - Relative frequencies are the maximum likelihood estimates
#### Example - Number Recognition Conditional Probabilities
_____
![[Naive Bayes Number Recognition.png]]
$P(Y)$ is the initial probability distribution. $P(F_{3,1}​=on|Y)$ indicates the probability that the element at position $(3,1)$ in the matrix is "on" given the value of $Y$. 

### Generalizing and Overfitting
_____
Relative frequency parameters will overfit the training data. If unseen events are given a zero probability, the chance that it appear such that the probability will always be zero regardless of how correct the sensory model gives. To generalize better, we need to **smooth** and **regularize** the estimates. 

#### [[Laplace Smoothing]]
___
Laplace's estimate pretends you saw every outcome once more than you actually did. This handles problem of zero probabilities in these models. It is used to estimate the probabilities for unseen events in a data set.  
$$P_{LAP}(x)=\frac{c(x)+1}{\sum_x[c(x)+1]}=\frac{c(x)+1}{N+|X|}$$
#### Estimate: Linear Interpolation
____
Laplace perform poorly for $P(X|Y)$ when both $|X|$ and $|Y|$ is large.
Get the empirical  from the data Make sure the estimates of  isn't too different from the empirical $P(X)$
$$P_{LIN}(x|y)=\alpha \hat{P}(x|y)+(1.0-a)\hat{P}(x)$$
