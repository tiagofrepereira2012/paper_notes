# Face Recognition Vendor Test - Part 3: Demographic effects

Do some intro

This summary should be "digested" with the NIST report on the side.

It's very clear that they target some populations.

## About the dataset

The NIST report quantified the accuracy of face recognition for the following demographic groups: **gender, age, ethnicity/country of birth** (here they assumed that country of birth is a good proxy for ethnicity).
The tests were carried out with systems from 106 vendors/universities (p. 25) and with four large datasets of photographs collection in the U.S governamental applications that are currently in operation and they are the following:  

 - **Domestic mugshots** collected in the United States.
 - **Application photographs** from a global population of applicants for immigration benefits.
 - **Visa photographs** submitted in support of visa applicants.
 - **Border crossing photographs** of travelers entering the United States.

The first 3 datasets have good compliance with image capture standards (ICAO).
The last one, does not have since images were captured in during the border crossing procedure.
Together this dataset contains:

  - 8.49M subjects
  - People from 24 countries (7 distinct regions)
  - Age from 6 distinct cohorts
  - 18.27M comparisons 


## Verification findings

The set of analysis for face verification (from p. 28) are split in to 2 parts.
The first one focus on **Impostors (False Positives evaluation - p.28)** and the second one focus on **Genuines (False negatives evaluation - p. 53)**.
For the sake of simplicity, I will enumerate each finding and point to the particular page in the report.


### False positives evaluation.

False positives (or false alarms) occurs when samples from two individuals, when compared, present a score higher than a decision threshold `T` (such threshold is a fixed value for most biometric systems).
The risk of a false alarm in a biometric system depends of the application, of course, but it is pretty obvious (i'll not discuss this here and just go direct to the point).
In the topics below it is summarized the findings about the impact of different demographics in the impostors score distribution.


#### False match rates under demographic pairing.

**Experiment**: In p. 30 it's described (for all systems) the impact (in terms of FMR) of matching the impostors and genuines score distributions based on the covariate.
For this, **they pick `T` that corresponds to 0.00003** of a impostor score distribution from **random people** (not looking to the covariates).
Then, using this `T` as a reference they start to pair the impostors and the genuines score distribution based on different covariates and measure the FMR as it can be observed in the figure below and in Figute 4 of the report (p .33).
  

![](frvt_images/figure3.png)


**Finding 1**: FMR is higher once the covariates from genuines and impostor distributions match.
From a random pair of distributions FMR is lower than when pairs are matched based on age, gender and ethnicity.


#### False match rates within and across countries

**Experiment**: Using high quality images, it was 442019 images from 24 countries were compared with 441517 images of different individuals from the same countries and `FMR(T)` was measured.
This analysis also was carried by **gender** and the target **age was (35-50]** years old (they call this age zone as "real world impostors").
The threshold `T` was set in another dataset (law enforcement mugshots) containing 93.070.400 imposters (I'm assuming mostly americans) and it corresponds to FMR at 0.00003 in this distribution.
The figure below (p. 35) shows a FMR hit map (in `log10` with the lower bound clip in -6) containing all the country combinations.
This analysis was carried out with the system imperial\_002 (more systems in the Annex 7).
**IMPORTANT** All the trends observed here, was observed for other systems too.

![](frvt_images/figure5.png)


**Finding 2**: Reinforcing finding 1, mixing the comparisons from different cohorts leads to lower FMR (obviously).

**Finding 3**: Nominal FMR observed in Eastern Europe population.

**Finding 4**: Higher FMR observed in East/West African countries, East Asia and Caribean countries (including Mexico). For some subpopulations, this values are two orders of magnitude higher than the nominal FMR. For some cases the level of security of this FMR corresponds to a PIN password with 2 digits only.

**Finding 5**: More accurate systems present biases, but more attenuated (look Figure 7 p.37).

**Finding 6**: Systems are less accurate with female cohort (look Figure 6 p. 36).

The reason for those shifts are unknown and "no attempts to explain these effects" were provided (p. 40).

Another view of those findings can be seem in the figure below (Figures 8, 9, 10 and 11 from p. 42).
In these figures all the 126 were put into perspective with two sub-populations (East Europe vs West Africa and East Europe vs East Asia).
It's possible to observe that the majority of the systems works in the nominal FMR zone for **East European male cohort** and way above the nominal FMR for **females, West african and East Asia** cohorts.

![](frvt_images/figure8.png)



## Identification findings



