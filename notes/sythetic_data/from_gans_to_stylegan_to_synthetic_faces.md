# From GANS to Style GANS to Sythetic Faces


In this piece of text, I will explain how to go from base GANs (Generative adversarial networks) [1] passing by StyleGANS 1 and 2 [2] [3] and how to reach our recent publication [4], where we leverage from style gan 2 to generate faces controlling some semantic factors.

## Generative models and GAN basics

Generative models using deep learning is a topic heavily researched nowadays by both Machine Learning and Computer Vision communities.
Strategies can be roughly divided in two categories: Conditional and Unconditional Generative models.

In short, **Unconditional Generative Models** synthesize data from noise and the two strategies that dominate the literature are Generative Adversarial Networks and Variational Auto-Encoders (VAEs).

Basically, VAEs consist of an encoder $$`q_{\phi}(z|x_i)`$$  that encodes from real samples $`x_i \in \mathbb{R}^m`$ to an **latent space** $`z \in \mathbb{R}^n`$ and a decoder network $`p_{\theta}(x_i|z)`$ that tries to reconstruct the original sample from samples of the latent space as "precisely" as possible.







## References 
- [1] Goodfellow, Ian; Pouget-Abadie, Jean; Mirza, Mehdi; Xu, Bing; Warde-Farley, David; Ozair, Sherjil; Courville, Aaron; Bengio, Yoshua (2014). Generative Adversarial Networks (PDF). Proceedings of the International Conference on Neural Information Processing Systems (NIPS 2014). pp. 2672–2680.

- [2] Karras, Tero, Samuli Laine, and Timo Aila. "A style-based generator architecture for generative adversarial networks." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.

- [3] Karras, Tero, et al. "Analyzing and improving the image quality of stylegan." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

- [4] Colbois, Laurent, Tiago de Freitas Pereira, and Sébastien Marcel. "On the use of automatically generated synthetic image datasets for benchmarking face recognition." arXiv preprint arXiv:2106.04215 (2021).