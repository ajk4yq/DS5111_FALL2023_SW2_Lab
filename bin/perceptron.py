"""Module for Perceptron"""
class Perceptron:
    """Perceptron Class"""
    def __init__(self):
        """Initialize weights"""
        self._weights = []

    def train(self, inputs, labels):
        """Method to train perceptron"""
        dummied_inputs = [my_x + [-1] for my_x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for my_input, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(my_input)
                for index, my_x in enumerate(my_input):
                    self._weights[index] += .1 * my_x * label_delta
    def predict(self, my_input):
        """Method to make prediction with perceptron"""
        if len(my_input) == 0:
            return None
        my_input = my_input + [-1]
        return int(0 < sum([my_x[0]*my_x[1] for my_x in zip(self._weights, my_input)])) # pylint: disable=consider-using-generator
