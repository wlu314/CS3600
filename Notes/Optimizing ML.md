# Loss Functions
_____
Loss functions provide how well a model's prediction matches the data. During the training process, the goal is to minimize the loss function. [[Gradient Descent]] uses the loss function to adjust the models parameters (weight) to reduce the loss and improve accuracy. 

## 0-1 Loss Function
____
$$1-sgn(y^* \cdot (w\cdot x))$$
### Hinge Loss
____
A classification loss function. Used for training classifiers like Support Vector Machines (SVMs). When wrong there is a degree of "wrongness". 
 
## Gradient Descent
____
The **gradient** gives the direction of steepest descent $\nabla f(x)$. 

-----
**Procedure**:
1. initialize $w$
2. loop
	- $w \leftarrow w - \alpha \cdot \nabla g(w)$
----

$\alpha$: learning rate is the tweaking parameter that needs to be chosen carefully. The weight vector should only change about $0.1-1\%$ per update. 

# Three Types of Gradient Descent
## Batch
____
$$w=w-a\sum_i \nabla LOSS(PREDICT(x_i,\theta), y_i^*)$$
- The gradient of the loss function is calculated using the entire dataset. 
- weight is updated by subtracting the product of the learning rate $\alpha$ and the sum of gradients of the loss with respect to the training example
- Computationally expensive 

## Stochastic
_____
$$w=w-a\nabla LOSS(PREDICT(x_i,\theta), y_i^*)$$
- Stochastic gradient descent is calculating a single randomly chosen training example
- The weights $w$ are updated by subtracting the product of the learning rate $\alpha$ and the gradient of the loss with respect to that single example.
- More noisy convergence

## Mini-Batch
____
$$w=w-a\sum_r \nabla LOSS(PREDICT(x_i,\theta), y_r^*)$$
- calculated using random small subset
- weights $w$ are updated by subtracting the product of the learning rate $\alpha$ and the sum of the gradient of the loss with respect to the mini-batch
- balance between the other two.


# Momentum
-----
**Procedure**:
1. initialize $w$
2. loop
	- $w \leftarrow \mu * v - \alpha \cdot \nabla g(w)$
	- $w\leftarrow w+v$
----
The $v$ increase in proportion to the slope. Over time momentum will build continuously. **With momentum**, the ball gains speed over time. **Without momentum**, the ball moves in response to the slope at each point which might lead to stopping and starting as slope changes. 


## Newton's method
_____
- use 2nd derivative
____
**Procedure**:
1. initialize $w$
2. loop
	- $w \leftarrow w - \alpha \cdot (\nabla ^2 g(w))^{-1} \nabla g(w)$
____
- Newton's method converges in one step for quadratic functions