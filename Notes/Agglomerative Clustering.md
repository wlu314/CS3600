 A hierarchical methods builds a hierarchy of clusters either by *merging small clusters* into larger ones such as agglomerative [[Clustering]]. It incrementally build larger clusters out of smaller clusters.

# Algorithm
____
- Maintain a set of clusters
- Initially, each instance in its own cluster
- Repeat: 
	- Pick the two closest clusters
	- Merge them into a new cluster
	- Stop when theres only one cluster left 

Produces not one clustering, but a family of clustering represented by a dendrogram. 
![[Agglomerative Clustering Dendrogram.png | 400]]

## Various Clustering
____
- Single-link clustering  (Closest Pair)
- Complete-link clustering (Farthest Pair) 
- Average of all pairs
- Ward's method (min-variance, like [[K-Means]])
- 