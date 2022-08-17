# Treasure-Hunt

This is a reinforcement learning game.
We have a 5x5 grid with some walls, and a prize in a hidden location. 
One Player is the receiver and the other player is the sender.
Once every episode starts, the sender sends a message to receiver (the message is just an integer) so a priori the message has no meaning.
The Receiver receives the message and moves around the grid, until it
finds where the prize is. Its goal is to find the prize as soon as possible.

The main point of this exercise is for the agents to create a communication between them. They need create a meaning for each message that both of them can understand. The models used were $\epsilon-greedy$ Q Learning.

How to use: at the file experimentGenerator.py you specify the desired experiment, and if you run that file it will run the whole program.
Below is a sample experiment, where the x axis is the log of the number of episodes trained, and the y axis is the discounted average reward.

![](images/question%2520d.png)
