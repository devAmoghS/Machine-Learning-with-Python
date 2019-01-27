import random

from neural_network.data import raw_digits
from neural_network.utils import backpropagate, feed_forward

if __name__ == "__main__":

    def make_digit(raw_digit):
        return [1 if c == '1' else 0
                for row in raw_digit.split("\n")
                for c in row.strip()]


    inputs = list(map(make_digit, raw_digits))

    targets = [[1 if i == j else 0 for i in range(10)]
               for j in range(10)]

    random.seed(0)  # to get repeatable results
    input_size = 25  # each input is a vector of length 25
    num_hidden = 5  # we'll have 5 neurons in the hidden layer
    output_size = 10  # we need 10 outputs for each input

    # each hidden neuron has one weight per input, plus a bias weight
    hidden_layer = [[random.random() for __ in range(input_size + 1)]
                    for __ in range(num_hidden)]

    # each output neuron has one weight per hidden neuron, plus a bias weight
    output_layer = [[random.random() for __ in range(num_hidden + 1)]
                    for __ in range(output_size)]

    # the network starts out with random weights
    network = [hidden_layer, output_layer]

    # 10,000 iterations seems enough to converge
    for __ in range(10000):
        for input_vector, target_vector in zip(inputs, targets):
            backpropagate(network, input_vector, target_vector)


    def predict(input):
        return feed_forward(network, input)[-1]


    for i, input in enumerate(inputs):
        outputs = predict(input)
        print(i, [round(p, 2) for p in outputs])

    print(""".@@@.
             ...@@
             ..@@.
             ...@@
             .@@@.""")

    print([round(x, 2) for x in
           predict([0, 1, 1, 1, 0,      # .@@@.
                    0, 0, 0, 1, 1,      # ...@@
                    0, 0, 1, 1, 0,      # ..@@.
                    0, 0, 0, 1, 1,      # ...@@
                    0, 1, 1, 1, 0])])   # .@@@.
    print()

    print(""".@@@.
             @..@@
             .@@@.
             @..@@
             .@@@.""")

    print([round(x, 2) for x in
           predict([0, 1, 1, 1, 0,      # .@@@.
                    1, 0, 0, 1, 1,      # @..@@
                    0, 1, 1, 1, 0,      # .@@@.
                    1, 0, 0, 1, 1,      # @..@@
                    0, 1, 1, 1, 0])])   # .@@@.
    print()
