# Accuracy comparison across face recognition algorithms: Where are we on measuring race bias?


## In a nutshell

This paper presents some underlying factors and methodological approach to assess biases (racial biases for instance) in face recognition databases.
Such factors are split in two categories: Data-driven and Scenario-modeling.
The Data-driven factors, can be, image quality, model (NN architecture), statistics of some sub-population.
Scenario modelling consider some demographic constraints or/and decision thresholds per sub-population.
Experiments were carried our in the GBU database where there's an equal distribution of Asia and Caucasian men.
The concludes with a check-list for measure racial bias.



## More details


The paper starts paraprasing the bias of face recognition algorithmm with the ORE (other-race effect) that's being observed for more than 50 years in humans in different races and in different groups.
We tend to better recognize better people from our own race rather than others and we have been observing this on FR algorithms.
This ORE has been observed in face recognition systems for more than 30 years (Lessons 1 and 2 in the paper)
Some good references on ORE are: 

[1] R. S. Malpass and J. Kravitz, "Recognition for faces of own and other
race." Journal of personality and social psychology, vol. 13, no. 4,
p. 330, 1969.

[2] A. J. O’Toole, K. Deffenbacher, H. Abdi, and J. C. Bartlett, "Simulating the ’other-race effect’ as a problem in perceptual learning,"
Connection Science, vol. 3, no. 2, pp. 163–178, 1991.


Some factors that might introduce such ORE effect in FR systems were split in two major categories.

Data-driven factors:
    – sub-population distributions: the population statistics for demographic groups
    – algorithm: the quality of the algorithm’s representations across demographic groups
    – representative images: the subgroup’s representation of the population of interest
    – imaging conditions: the imaging conditions directly affect the difficulty of comparing images

Scenario-modeling
    – threshold: appropriate selection of threshold for a desired FAR for each racial group, independently
    – demographic-pairing: modeling the homogeneity of the different-identity distribution


To analyse those factors the authors designed an experiment using 4 FR systems.
One before DCNN era and (a score fusion of the best systems from FRVT 2006.
The other three are VGG16, [3] and [4]  (the last 2 there are no code available)


[3] R. Ranjan, A. Bansal, J. Zheng, H. Xu, J. Gleason, B. Lu, A. Nanduri, J.-C. Chen, C. D. Castillo, and R. Chellappa, “A fast and accurate system for face detection, identification, and verification,” IEEE Transactions on Biometrics, Behavior, and Identity Science, vol. 1, no. 2, pp. 82–96, 2019.

[4] R. Ranjan, C. D. Castillo, and R. Chellappa, “L2-constrained softmax loss for discriminative face verification,” arXiv preprint arXiv:1703.09507, 2017.


For the database, they resuscitated GBU database (Good, Bad and Ugly).
For the record, this dataset contains 1,085 images of 437 identities in each partition.
The dataset includes frontal images that vary in environment (e.g., indoors and outdoors) and demographics (race, age, gender).
All images were collected within a single academic year.
GBU dataset was selected for this study because "(1) race in the GBU dataset is self-reported, (2) the conditions under which the images were taken are identical across and within race groups, and (3) age range is narrow which limits other confounding demographics".


For this experiment, a subset samples from GBU were selected.
The rules are the following:

 1. Only images taken indoors were selected.
 2. Given that Asian and Caucasian faces represented the majority of images, only these two racial groups were selected for comparison
 3. Gender was NOT split for some unknown reason.

After this prunning, the condensed GBU consisted of:
  - Good: 385 dentities;
  - Bad: 389 identities; 
  - Ugly: 380 identities;


## Fidings

**Finding 1** During the **Experiments**, it was observed that biases (high FNMR) was only observed at very low FMR (0.0001).

**Finding 2** Image quality matters. Biases were more proeminet in UGLY subset.

**Finding 3** These findinds corroborates with the ones from [NIST](../FRVT_demographic.md) report.

