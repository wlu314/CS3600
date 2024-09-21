**Algorithm**
_____
For $i=1,2,..,n$ 
	Sample $x_i$ from $P(X_i | Parents(X_i)$\
Return $(x_1,x_2,...,x_n)$

![[Courses/CS-3600/Notes/Prior Sampling.png]]
*Answer: A* 

![[Prior Sampling 1.png]]*Answer*: $N \cdot P(A) \cdot P(B|A) \cdot P(C|B)= N  \cdot P(-a) \cdot P(+b|-a) \cdot P(-c|+b)=1000 \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{5}=50$ 