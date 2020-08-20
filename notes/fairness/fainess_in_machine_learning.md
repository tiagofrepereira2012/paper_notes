# Fairness in Machine Learning

 
## Mental notes

Given tree random variables $R$, $Y$, and $A$ being the prediction variable, target variable, and sensible attributes respectively, let's discuss the fairness criterias presented in the book.
Here $R=\{0,1\}$, $Y=\{0,1\}$ and $A=\{a,b\}$

### Independence

The independence criteria $R \perp A$ is equivalent to the condition:

$P\{R=1 | A=a\} = P\{R=1 | A=b\}$

**Interpretation:** The decision score $R$ should be the same regardless of the sensible attribute $A$.


### Separation


The separation criteria $R \perp A | Y$ is equivalent to the conditions:


$P\{R=1 | Y=1, A=a\} =  P\{R=1 | Y=1, A=b\} $ --> True Positive Rate

$P\{R=0 | Y=0, A=a\} =  P\{R=0 | Y=0, A=b\} $ --> True Negative Rate

$P\{R=1 | Y=0, A=a\} =  P\{R=1 | Y=0, A=b\} $ --> False Positive Rate

$P\{R=0 | Y=1, A=a\} =  P\{R=0 | Y=1, A=b\} $ --> False Negative Rate


**Interpretation:** Figures of metric should be the same regardless of the sensible attribute $A$.


### Sufficiency

The separation criteria $Y \perp A | R$ is equivalent to the condition:

$P\{Y=1 | R=r, A=a\} =  P\{Y=1 | R=r, A=b\}$


**Interpretation:**
