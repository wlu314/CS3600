A **decision tree** is a representation of a function that maps a vector of attributes value to a single output value called "a decision". Reaches its decision by performing a sequence of tests. It starts at the root and follow the appropriate branch until a leaf is reached. Each internal node in the tree corresponds to a test of the value of one of the input attributes. The branches from the node are label with possible values of the attribute and the leaf specify what value is return by the function. 

**Boolean classification** are outputs that are either true or false. 
![[Figure 19.3.png]]

Learn Decision Tree algorithm adopts a greedy divide and conquer strateg by testing the most important attributes first. Then it recursively solves the smaller subproblems that are defined by the possible results of the test.