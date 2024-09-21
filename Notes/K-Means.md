K-mean will **always converge** but not to a global optimum. It won't always find the true pattern. 

**Steps**: 
1. **Initialize Centroids**: Choose K initial centroids randomly from the dataset. These centroids will serve as the initial centers of the clusters.
2. **Assign points to nearest centroids**. Each data point is assigned to the nearest centroid based on the euclidean distance. 
3. **Update centroids** - calculate the new centroids as the mean of all data points assigned to each clusters. Find the average position of all in each cluster 
4. **Repeat 2 and 3** until centroids no longer change significantly or max iterations is reached. 

### Optimization
_____
Consider the total distance to the means
$\phi (\{ x_i \}, \{ a_i \} , \{ c_k\}) = \sum_i dist(x_i,c_{a_i})$
$x_i$ are the points
$a_i$ are the assignments
$c_k$ are the cluster means
- Each iteration reduces phi
- Two stages each iteration
	- Update assignments: fix means c, change assignment a
	- Update means: fix assignments a, change means c

The goal of the K-means algorithm is to minimize this total distance (phi), which represents the sum of distances between each data point and its assigned cluster centroid.

**Iterative Process**: 
1. Update Assignments
	- Fix the current centroids
	- Assign each data point $x_i$ to the nearest centroid $c_{a_i}$
	- This step changes the assignment $a_i$ based on the fixed centroids $a_i=argmin_k dist(x_i,c_k)$
2. Update Means
	- Fix the current assignments $a_i$ 
	- Calculate the new centroids $c_k$ as the mean of all data points assigned to each cluster $c_k=\frac{1}{|\{ i: a_i = k\}|} \sum_{i:a_i=k}x_i$
	- step changes the centroids based on the fixed assignments

