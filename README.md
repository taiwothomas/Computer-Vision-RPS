This is a rock-paper-scissors game that takes user input using a computer vision model.
The model was developed using teachable machines online at https://teachablemachine.withgoogle.com/train
This helps create a machine learning model that can be downloaded locally.

This model is deployed by running RPS_solution.py within a virtual conda environment with the following dependencies installed via pip:
opencv-python, tensorflow and ipykernel.

The game logic is written in manual_rps.py containing methods for the user and computer input, and the game winner logic. This is contained in a class named Rps.

When the game is run, a  five-second timer starts  and is displayed in the video frame. The CV model predicts the image in each frame and saves the result to a variable. This is how the user input is taken.
The computer select its input randomly. 
The game is run five times and the winner is the player with the most victories.