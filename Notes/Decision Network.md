![[Courses/CS-3600/Notes/Decision Network.png]]![[Decision Network 1.png]]

![[Decision Network 2.png]]![[VPI.png]]
## Value of Information
____
For evidence e: $$MEU(e)=max_a\sum_s P(s|e)U(s,a)$$
Assuming we see new evidence E'= e': $$MEU(e,e')=max_a\sum_s P(s|e,e') U(s,a)$$

E' is a random value which value is unknown. The expect value of E' is revealed and then we act: $$MEU(e,E')=\sum_{e'}P(e'|e)MEU(e,e')$$
VPI is the difference between the expectation of observing new variable to if we don't.
$$VPI(E'|e)=MEU(e,E')-MEU(e)$$


![[Nonegative.png]]


## VPI Properties
____
Non-negative: $\forall E', e: VPI(E'|e) \ge 0$
Non-additive: $VPI(E_j,E_k|e) \cancel = VPI(E_j|e)+VPI(E_k|e)$ 
Order-independent: $VPI(E_j,E_k|e) = VPI(E_j|e)+VPI(E_k|e, E_j)$
and $VPI(E_j,E_k|e) = VPI(E_k|e, E_j) + VPI(E_j|e)$

