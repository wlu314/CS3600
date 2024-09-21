Two ways to factor a joint distribution over two variables
$$P(x,y)=P(x|y)P(y)=P(y|x)P(x)$$
$$P(x|y)=\frac{P(y|x)}{P(y)} P(x)$$

This rule helps up build one conditional from its reverse. 

![[Bayes Rule Question.png | 300]]
$P(W|dry) = \frac{P(dry|W)P(W)}{P(dry)}$
**W=Sun**:
	$P(sun|dry) = \frac{P(dry|sun) P(sun)}{P(dry)} = \frac{0.9\cdot 0.8}{Z}=0.72/Z$

	$P(rain|dry)=\frac{P(dry|rain)P(rain)}{P(dry)}=\frac{0.3 \cdot 0.2}{Z}=0.24/Z$
	$Z=0.72+0.06$
	