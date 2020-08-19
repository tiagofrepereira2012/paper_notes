# Face Recognition: Too Bias, or not Too Bias


## In a nutshell

In this paper, the authors present a new database (called BFW) to study bias effects in Face Recognition.
This database is basically an extra layer on top of VGG2 where gender and race were semi-automatically annotated.
Furthermore, the authors discuss that score distributions from different ethnicities/gender and from both genuines/impostors varies no matter the demographic cut you look at AND suggests a one threshold per demographic cut is more suitable for the problem.
Finally, a Face verification human assessment is carried out in order to see if our "brain face recognition machine" is also biased.

## More details

As mentioned before, the paper presents the impact of having a single threshold that works well for all demographic cuts and advocates that having one threshold for the task is more suitable.
This approach has some problems IMO and they are the following:

 1. Another classification problem needs to be solved in order to pick the right threshold. The authors never discuss this aspect. Furthermore, this operation is no longer blind, which can be legally problematic.
 2. The selection of a threshold per demographic cut might be critical and can suffer from underrepresentation. We can observe this in MORPH and MEDS that have very little data from Hispanic and Asiatic women.


## Findings

**Finding 1**. Good dataset

**Finding 2**. Human assessement in this dataset to verify is we present a biased behaviour

