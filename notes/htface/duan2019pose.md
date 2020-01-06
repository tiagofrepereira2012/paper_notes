# Pose Agnostic Cross-spectral Hallucination via Disentangling Independent Factors

This paper proposes two cascaded convolutional neural networks (CNN) to solve the NIR (Near Infrared) to VIS (Visual light images) task.
The authors hypothesize that NIR-VIS comparisons is a difficult task not only due to spectral differences, but also due to another factors, such as, pose and expression.
To approach that the authors propose two different CNN.
The **first** one take as input a NIR image, a VIS image and 3d image.
The goal of this network is to align the NIR image to the VIS image in order to have the same pose and expression.
The **second** network is responsible synthesize a VIS image give the aligned generated NIR image.
Comparisons are made between the synthesized VIS image and original VIS image using regular face recognition methods.


## Key points

 - There are basically two Encoder/Decoder mechanisms to handle the different tasks
 - It's not clear that at test time you need the 3D image to learn the rotations. If so, this is a drawback
 - Handle NIR-VIS databases only
 - One of their losses (Identity Preserving Loss) **needs to have a pair of images** sensed in different image modalities.
 
