[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tiagofrepereira2012/MINE/master?filepath=MINE.ipynb)

# MINE - Mutual Information Neura Estimation - TF 2

Tensorflow 2 implementation of MINE - Mutual Information Neural Estimation (https://arxiv.org/pdf/1801.04062.pdf)


## How to use?


```python
from mine import MineModel
model = MineModel()
model.compile(optimizer="adam")
model.fit(x=[X, Z])
```

![](MINE.png)