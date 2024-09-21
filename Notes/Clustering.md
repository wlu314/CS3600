Clustering is a **unsupervised machine learning** technique used to group similar data points together based on characteristics. The goal is to detect patterns in unlabeled data. It doesn't require labels but does require data. 

## [[K-Means]]
_____
An iterative clustering algorithm. Picks K random points as cluster (means). It assigns data instances to closest means and assign each mean to the average of its assigned points. Stop when no points' assignments change. 

K-mean will **always converge** but not to a global optimum. It won't always find the true pattern. 

## [[Agglomerative Clustering ]]
____
 A hierarchical methods builds a hierarchy of clusters either by *merging small clusters* into larger ones such as agglomerative clustering. It incrementally build larger clusters out of smaller clusters.
 