Suppose that $[true,true,false,true,true]$ is the observed umbrella sequence. What is the sequence $x_{1:t}$ that must be true. This is a linear time algorithm for finding the **most likely sequence** given evidence. It relies of the Markov property that yielded a more efficient algorithm.
![[Figure 14.5.png]]
$m_{1:t}=max_{x_{1:t-1}}P(x_{1:t-1},X_t,e_{1:t})$ 
$m_{1:t+1}=P(e_{t+1}|X_{t+1})max_{x_t}P(X_{t+1}|x_t)max_{x_{1:t-1}}P(x_{1:t-1},x_t,e_{1:t})$
There is no normalizing constant $a$ like the filtering equation. The algorithm for computing starts at time 0 with the prior $P(X_0)$ and runs forward along the sequence. 