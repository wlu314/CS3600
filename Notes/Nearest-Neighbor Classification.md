- 1 Nearest Neighbor (1-NN): copies the label of the most similar data points
- K Nearest Neighbor (K-NN): vote the k nearest neighbors (needs a weighting scheme)
- The issue is to define similarity
- Trade-offs: small k gives relevant neighbors, large k give smoother functions

# Parametric/Non-Parametric
____
 **Parametric**: 
 - Fixed set of parameters
 - More data means better settings 
 **Non-parametric models**: 
 - Complexity of classifiers increase with data
 - Better in the limit often worse in the non limit 
 - KNN is non parametric

### Example - Digit Classification
____
Nearest Neighbor for digits
- Take new image 
- Compare to all training images 
- Assign based on closest example 
- Encodes image is vector of intensities $$1\rightarrow <0.0,0.0,0.3,0.8,0.7,0.1,...,0.0>$$ this could be a vector of pixel intensities or features
- Find the similarity function. $$sim(x,x')=x\cdot x'=\sum_i x_ix_i'$$ *if features are just pixels*
## Basic Similarity
____
$$sim(x,x')=f(x)\cdot f(x')=\sum_if_i(x)f_I(x')$$
*many similarities based on **features dot products***

## Invariant Metrics
_____
- Better similarity functions use knowledge about vision
- Invariant metrics have similarities under certain transformation: Rotation, scaling, translation, stroke-thickness 

