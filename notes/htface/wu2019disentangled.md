# Disentangled Variational Representation for Heterogeneous Face Recognition

This paper hypothesizes that facial appearance can be decomposed (disentangled) in to two independent latent variables.
One represents the identity distribution and one the variation distributions, where the identity variable can be marginalized.
The last variable one takes into account all possible variations with respect to image modality, pose, expression, etc...
The authors proposed a framework to disantangle those variables for the case of VIS-NIR face recognition.

## Key points

This disentanglement framework is composed of many parts and its training is full of tricks, I will try to summarize its key points as follow:

  - It is assumed that spectrum differences lies in a linear manifold. This is important for future assumptions
  - Given ![\{x^{i} \in \mathbb{R}^d \}](https://render.githubusercontent.com/render/math?math=%5C%7Bx%5E%7Bi%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed%20%5C%7D)  and 


