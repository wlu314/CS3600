![[Rejection Sampling.png]]
**Algorithm**:
IN: evidence instantiation
$for \space i=1,2,...,n$
	Sample $x_i$ from $P(X_i|Parents(X_i))$
	if $x_i$ not consistent with evidence
		reject: return, and no sample is generated in this cycle
$return \space (x_1,x_2,...,x_n)$


### Questions
___
1. What queries can we answer with rejection samples (evidence: +c)?
   A. $P(+a,-b,+c)$ - This calculates $(+a,-b,+c)$ but rejection sampling ignores all $(-c)$ samples. Therefore, it's not possible to count the number of total samples.
   B. $P(+a,-b|+c)$ (correct) - This is correct because under the condition of $(+c)$ how many is $(+a,-b)$. This is possible as all $(-c)$ is removed. 
   C. $Both$ (this would be correct if you knew the number of rejections)
   D. $Neither$