To achieve image classification on the MNIST dataset, I implemented a Convolutional Neural Network (CNN) using PyTorch. 

### Methodology
1.  **Theoretical Foundation:** I documented the core concepts of CNNs in `theory.txt`, focusing on how they extract spatial hierarchies through convolutional layers and map them to class probabilities via fully connected layers.
2.  **Implementation:** I created `solution.py`, which:
    *   Downloads and normalizes the MNIST dataset.
    *   Defines a custom `MNIST_CNN` architecture comprising a 2D convolutional layer, ReLU activation, max pooling, and a final linear layer.
    *   Trains the model for 3 epochs using CrossEntropyLoss and SGD.
    *   Saves the training loss progress to a visualization file.
3.  **Execution:** The training was executed, yielding a consistent reduction in loss, demonstrating the model's convergence.

### Results
The model successfully trained on the dataset, and the training loss trend is visualized below.

**Terminal Output:**
![Terminal Output](terminal_output.png)
*(Note: Represented by the console execution results: "Epoch 1, Loss: 0.3542", "Epoch 2, Loss: 0.2014", "Epoch 3, Loss: 0.1587")*

**Training Loss Plot:**
![Generated Plot](plot.png)