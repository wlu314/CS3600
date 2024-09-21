- Inputs are **feature values**
- Each features has a **weight** 
- Sum is the **activation** 
$$activation_w(x)=\sum_iw_i\cdot f_i(x)=w\cdot f(x)$$
- Activation is positive, output +1
- Activation is negative, output -1

## Weights
____
Binary Case: compare features to a weight vector
Learning: Figure out the weight vectors from examples![[Linear Models Weights.png]]
*For a spam detector, each feature is given a weight. Given a weight vector and feature vector, if the dot product will give either a positive or negative result. $f(x_1)\cdot w$* 

### Binary Decision Rule
____
In the space of feature vectors, if the weight vector and the feature vector is greater than $90 \degree$ than it will be given a negative value. There's a line that runs perpendicular called a **decision boundary**. Any weight vector is a hyperplane. In a 2 dimensional plane, it's a line. In a 3 dimensional plane, it's a plane. Any $n-th$ dimensional plane, the weight vector is $n-1$ hyperplane.

#### Weight Updates: Binary Perceptrons
_____
Start with weights = 0
for each training instance
	-Classify current weights $$y=+1\space\space if \space\space w\cdot f(x) \ge0$$ $$y=-1\space \space if \space \space w\cdot f(x)<0$$
	-if correct, no change -> compare with y=y*
	-if wrong, adjust the weight vector -> by adding or subtracting feature vector. Subtract if y* is -1. 

**Adjusting Feature Vector**:
$$w=w+y^*\cdot f$$Before & After 
![[Courses/CS-3600/Notes/Adjusting Feature Vector.png | 200]]![[Adjusting Feature Vector 1.png | 200]]
### Multi-class Decision Rule
_____
![[Courses/CS-3600/Notes/Multiclass Decision Rule.png]]
- A weight vector for each class $w_y$\
- Score (activation) of a class $y$ $w_y\cdot f(x)$
- Prediction highest score wins $y=arg_ymax \space w_y\cdot f(x)$
![[Multiclass Decision Rule 1.png| 250]]

#### Learning - Multi-class Perceptron
_____
- Start with all weights = 0
- Pickup training example one by one
- Predict with current weights $$y=argmax_yw_y\cdot f(x)$$
- if correct no change
- if wrong: lower score of wrong answer, raise score of right answer $$w_y=w_y-f(x)$$$$w_{y^*}=w_{y^*}+f(x)$$

![[Multiclass Decision Rule 2.png | 200]]
![[Multiclass Decision Rule 3.png | 250]]
##### Example - Multiclass Perceptron
_____
![[Multiclass Perceptron Example.png]]


### Properties of Perceptrons
____
- Separability: true if some parameters get the training set perfectly correct
- Convergence: if the training is separable, perceptron will eventually converge - [[Perceptron Convergence Theorem]]. This theorem tells us how fast we will converge, because convergence is guaranteed. 
- Mistake bound: maximum number of mistakes related of the margin or degree of separability. $$Mistakes <\frac{k}{\delta^2}$$ *The number of mistakes is the number of features divided by squared of the size of the margin that separates positive from negative classes*
  
 ![[Properties of Perceptrons.png| 250]]
###  Problems & Improvement with the Perceptron
____
**Problem**: If the data isn't separable, weight might thrash causing **noise**. **Solution**: Average weight vectors overtime can help (averaged perceptron). 

**Problem**: Mediocre Generalization finds a barely separating solution. 

**Problem**: Overtraining test/hold-out accuracy usually rises then falls. Overtraining is like overfitting.

#### MIRA* 
____
Idea is to adjust the weight update to mitigate these effects. MIRA* choose an update size that fixes the current mistake.
Guessed $y$ instead of $y^*$ on example $x$ with features $f(x)$. 
$$w_y=w'_y-\tau f(x)$$ $$w_{y^*} = w'_{y^*}+\tau f(x)$$
![[Minimum Correcting Update.png]]

**Maximum Step Size**
___
- Bad to make updates that are too large
	- Not enough features
	- Solution is to cap the maximum possible value of $\tau$ with some constant
$$\tau^* = min(\frac{(w'_y-w'_{y^*}) \cdot f+1}{2f\cdot f})$$
- 


Converges faster than perceptron and better on noisy data 

#### Support Vector Machines
___
- Maximizing the margin between the closest + and - in the training data. 
- SVMs find the separator with max margin
- SVMs are MIRA where you optimize over all examples at once
![[MIRA vs SVM.png| 300]]
