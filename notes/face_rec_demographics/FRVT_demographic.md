# Face Recognition Vendor Test - Part 3: Demographic effects

Do some intro

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

The set of analysis for face verification (from p. 28) is split in to 2 parts.
The first one focus on Impostors (False Positives evaluation - p.28) and the second one focus on Genuines (False negatives evaluation - p. 53).
For the sake of simplicity, I will enumerate each finding and point to the particular page in the report.


### False positives evaluation.

 1. In p. 30 it's described (for all systems)the impact of matching the impostors and genuines score distributions based on the covariate

 2. 



## Identification findings



