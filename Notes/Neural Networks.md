# Perceptron
_____
![[Neural Network - Perceptron.png | 350]]
![[Figure 18.19.png]]

The dot product of weights and features are passed in an activation $\Sigma$. If it's negative (output: -) and if it's positive (output: +). The basic building block of the neural network is the [[Perceptron]]. A neural network is build from stacked perceptrons. 

A neural network is just a collection units connected together. The properties of the network are determined by its topology and the properties of the neurons.
![[Neural Network - N-Layer Perceptron Network.png]]
## Neural Network Structure
____
Neural networks are composed of nodes or units connected directly by **links**. A link from unit $i$ and $j$ serve to propagate the **activation** $a_i$. Each link has a **weight** $w_{i,j}$ associated with it. Each unit has a dummy input $a_0=1$ with an associated weight $w_{0,j}$. Each unit $j$ first computes a weighted sum of its inputs. $$in_j=\sum_{i=0}^nw_{i,j} a_i$$
Then it applies an activation function $g$ to this sum to derive the output. $$a_j=g(in_j)=g(\sum_{i=0}^nw_{i,j} a_i)$$The activation function $g$ is typically either a hard threshold in which case the unit is called a perceptron or a logistic function. Sometimes sigmoid perceptron is used. A nonlinear activation function ensure the important property that the entire network of units can represent a nonlinear function.

**Feed-Forward** network has connections only in one direction. Every node receives input from upstream or parent nodes. This network represents a function of its current input. A **recurrent network** feeds its outputs back into its own inputs. Feed-Forward network are arranged in layers such that each unit receives input only from units in the immediately preceding layer. **Hidden Units** are not connected to the outputs of the network.

### Single Layer Feed-Forward Network (perceptrons)
____
A network with all inputs connected directly to the outputs are called single layer neural network or perceptron networks. 
![[Perceptron Network Training Data.png | 300]]


## Soft-Max
____
The soft-max algorithm is a function used for multi-class classification problems. It converts a vector of values into a probability distribution. 