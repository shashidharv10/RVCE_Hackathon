# RVCE_Hackathon

This project is ML based and it is designed for providing techinical support to paralused patients by monitoring their facial emotions and eye movements.
A pretrained model for emotion detection was taken and was again trained with a certain additional photographs and the same was done for the detection of the blink of an eye.
The blink of an eye detection involved basic construction of neural networks using tensor flow.
The movement of the eye was coded in C++ and was not very effective but detected large movements in the pupil of the eyes but it failed to pick up the minute movements.
The pupil of the eye was the main factor to detect the direction of the movement and was done based on the color intensity difference between the eye ball and the pupil.

The entire project is based on OpenCV and lot of information was gathered about how to construct this idea into what the project is from the blog PyImageSearch.
The interface for interaction was built using Tkinter module on python. Initially we tried to build it on a single system using the microprocessor of the computer but the we failed to achieve the concurrency.
To achieve concurrency we had to move to a microcontroller platform such as raspberry pi.

This project is still being developed with contributions from other team members as well.

The respective haar cascasde files to be used along with the face and eye detection have not been uploaded due to file size constraints please download them to use the application.
