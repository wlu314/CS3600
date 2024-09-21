from NeuralNet import *

## XOR Training data, easier than to get from xor.txt file
examples = [
    ([0, 0], [0]),
    ([0, 1], [1]),
    ([1, 0], [1]),
    ([1, 1], [0])
]

train_ex = examples
test_ex = examples
example_data = (train_ex, test_ex)
maxIterations = 1000


## 0 Hidden Layers -> perceptron 
nnet, accuracy = buildNeuralNet(example_data, hiddenLayerList=[], maxItr=maxIterations)
print(f"The accuracy of a simple perceptron is: {accuracy * 100:.2f}%")


## Training with more hidden layers
# hidden_layer_sizes = [5,10,15]
# for size in hidden_layer_sizes:
#     print(f"\nTraining with {size} hidden perceptrons:")
#     nnet, accuracy = buildNeuralNet(example_data, hiddenLayerList=[size], maxItr=maxIterations)
#     print(f"Training with {size} hidden perceptrons resulted in {accuracy * 100:.2f}% accuracy.")
