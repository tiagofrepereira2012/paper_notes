# Investigating Bias in Deep Face Analysis: The KANFace Dataset and Empirical Study


## In a nutshell

This paper introduces a new Face Database (KANFace) focusing on possible biases in three different tasks related to faces (face recognition, age estimation, and gender recognition).
Such dataset contains 40K images + 44k videos (14M available images in total) of 1045 identities (586 male, 459 female, and 544 kin pairs) distributed in around 39 images and 13,870 frames per subject.
The following metadata information is available: Age, Gender, Kinship.
The dataset is also divesed with respect to some cranio-facial ratios, face region contrast and skin-tone.

A method to mitigate biases was also presented, but not well evaluated in my opinion.


## More details

**About the dataset;** it was basically scrapped from the web using IMDb and wikipedia pages from celebrities with a simple pipeline of selecting images.

**About biases in FR;** An assessment on how FR systems are w.r.t demographics of the KANFace was carried out using the Light CNN, VGG16 and restnet 50.
However, only rank 1 recognition rate in a closed-set scenario is used as metric, which is very raw as a metric.

**About biases mitigation;** The regularization mechanism presented to mitigate such biases is not clear at all, but the overall hypothesis is that **there is some orthogonality between identity and sensitivity attributes (age, gender, ....)**, and CNNs are regulirized with that.

## Findings

**Finding 1**. Nice dataset they gathered, but so far not freely available.


