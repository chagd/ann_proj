import numpy as np


class NeuralNet:
    def __init__(self, shape):
        self.weights = []
        self.biases = []
        for i in range(len(shape)):
            if i != 0:
                self.weights.append(np.random.random_sample(
                    size=[shape[i], shape[i-1]]))
                self.biases.append(np.random.random_sample(size=shape[i]))


a = NeuralNet(shape=[2, 3, 2, 1])
