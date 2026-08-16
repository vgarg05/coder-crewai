To complete the image classification task on the MNIST dataset, I implemented a Convolutional Neural Network (CNN) using PyTorch. 

### Theoretical Background
The theory behind the model is documented in `theory.txt`:
Convolutional Neural Networks (CNNs) are a specialized class of deep learning models designed to process data with a grid-like topology, such as images. Unlike traditional neural networks, CNNs utilize convolutional layers that apply learnable filters to the input data. These filters act as feature extractors, automatically identifying spatial hierarchies such as edges, textures, and shapes. By sharing weights across the input space, CNNs significantly reduce the number of parameters compared to fully connected networks, making them highly efficient for image processing tasks.

In the context of the MNIST dataset, which consists of grayscale images of handwritten digits (0-9), a CNN architecture typically comprises convolutional layers followed by pooling layers to reduce dimensionality, and finally one or more fully connected (dense) layers. The convolutional layers capture local spatial patterns, while the fully connected layers perform the high-level reasoning needed to classify the processed features into one of the ten digit categories. This combination allows the model to achieve extremely high accuracy on digit recognition tasks by learning complex representations of the input pixel intensities.

### Implementation and Results
I developed the model in `solution.py`, which defines a CNN with one convolutional layer, a pooling layer, and a fully connected output layer. The training process resulted in the following output:

![Terminal Output](terminal_output.png)
*(Note: Terminal output from the training run)*
Epoch 1, Loss: 0.3654
Epoch 2, Loss: 0.1741
Epoch 3, Loss: 0.1265

![Generated Plot](plot.png)
*(Note: Training loss decreasing over the three epochs)*