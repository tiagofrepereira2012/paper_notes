# Disentangled Variational Representation for Heterogeneous Face Recognition

This paper hypothesizes that facial appearance can be decomposed (disentangled) in to two independent latent variables.
One represents the identity distribution and one the variation distributions, where the identity variable can be marginalized.
The last variable one takes into account all possible variations with respect to image modality, pose, expression, etc...
The authors proposed a framework to disantangle those variables for the case of VIS-NIR face recognition.

## Key points

This disentanglement framework is composed of many parts and its training is full of tricks, I will try to summarize its key points as follow:

  - Given ![\{x^{i} \in \mathbb{R}^d \}](https://render.githubusercontent.com/render/math?math=%5C%7Bx%5E%7Bi%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed%20%5C%7D) and ![\{x^{i} \in \mathbb{R}^h \}](https://render.githubusercontent.com/render/math?math=%5C%7Bx%5E%7Bi%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Eh%20%5C%7D) independent variables of one identity `i`, it is hypothesized that ![\z^{i} = \mu^{i} + \epsilon  \odot \sigma^{i}](https://render.githubusercontent.com/render/math?math=%5Cz%5E%7Bi%7D%20%3D%20%5Cmu%5E%7Bi%7D%20%2B%20%5Cepsilon%20%20%5Codot%20%5Csigma%5E%7Bi%7D), where \mu^i denotes identity information and \sigma_i denotes variation information. The marginalization of x (which is intractable) is given by an autoencoder defined in equation 3.
  - It is assumed that spectrum differences lies in a linear manifold. This is important for future assumptions, hence, ![\sigma_{\text{VIS}} = P\sigma_{\text{NIR}} ](https://render.githubusercontent.com/render/math?math=%5Csigma_%7B%5Ctext%7BVIS%7D%7D%20%3D%20P%5Csigma_%7B%5Ctext%7BNIR%7D%7D%20)
  - They assumed that the latent variables ![z_\text{VIS}](https://render.githubusercontent.com/render/math?math=z_%5Ctext%7BVIS%7D) and ![z_\text{NIR}](https://render.githubusercontent.com/render/math?math=z_%5Ctext%7BNIR%7D) are independent, hence, and ortogonality can be imposed in 'P'. Therefore: ![P^\intercal P = 1](https://render.githubusercontent.com/render/math?math=P%5E%5Cintercal%20P%20%3D%201)
  
  - Tests made only with VIS images
  - No source code


