## Inference - Forward Algorithm
_____
![[Particle Filter - Inference.png]]
The complexity is $O(n^2)$ and continuous state are hard to instantiate. 

## Approximate Inference
____
- Tracks samples not all values
- Samples are called particles
- Time per step is linear in the number of samples
- The representation of $P(X)$ is now a list of N particles (samples)
- $P(X)$ approximates by number of particles with value $x$

#### Particle Filtering: Elapse Time 
___
Each particle is moved by sampling its next position from the transition model $$x'=sample(P(X'|x))$$
This is like prior sampling - samples' frequencies reflect the transition probabilities.

#### Particle Filtering: Observe
____
Similar to likelihood weighting, down-weight samples based on the evidence. 
$$w(x)=P(e|w)$$
$$B(X)\propto P(e|X)B'(X) $$
The probabilities don't sum to one since all have been down-weighted. They sum to N times an approximation of $P(e)$![[Particle Filters - Algorithm.png| 150]]
#### Particle Filtering: Resample
____
- Resample
- N times we choose from our weighted sample distribution
- Equivalent to renormalizing the distribution 
- Update is complete for this time step
- Resample particles based on their weights. Draw particles with replacement, where the probability of selecting a particle is proportional to its weight.
- Replace the current set of particles with the resampled set, resetting weights to uniform (or equal) values for the next iteration.
![[Particle Filtering Resa ple.png | 250]]