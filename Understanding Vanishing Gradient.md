# Understanding Vanishing Gradients in Neural Networks

![Vanishing Gradient](https://i.stack.imgur.com/YUlyb.jpg)

### Introduction

We all know that neural networks perform learning through the process of forward pass and backward pass.<br> 
This cycle goes on until we find a optimal value for the cost function that we are trying to minimize. <br>
The optmization happens with the help of gradient descent.<br>

Graidents are computed in each of the layers of the neural network. When the number of layers are increased, the value of the cost function starts approaching towards zero, since we are trying to minimize the cost.
This impacts the training of the neural network and it takes longer for the network to converge.

The good news is that this is the case when only certain activation functions are used in the neural networks.

### Why does it happen ?

A very commonly used activation function is the sigmoid function.

![Sigmoid Function and its Derivative](https://miro.medium.com/max/1000/1*6A3A_rt4YmumHusvTvVTxw.png)
