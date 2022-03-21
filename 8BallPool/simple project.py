import numpy as np
import copy

np.random.seed(0)


def sigmoid(x):
    o = 1 / (1 + np.exp(-1))
    return o


def sigder(x):
    return x * (1 - x)


# data generation
x1 = np.array([1, 0])
x2 = np.array([0, 1])
y = np.array([1, 0])

# features
input_layers = 2
hidden_layers = 2
out_layers = 1

# weights
wx = 2 * np.random.rand(input_layers, hidden_layers) - 1
wy = 2 * np.random.rand(hidden_layers, out_layers) - 1
wh = 2 * np.random.rand(hidden_layers, hidden_layers) - 1

wx_update = np.zeros_like(wx)
wy_update = np.zeros_like(wy)
wh_update = np.zeros_like(wh)

# other parameters
lr = 0.5
epochs = 500

# generate xandy
for epoch in range(epochs):
    h = np.zeros(hidden_layers)
    layer2_delta = list()
    pred = list()
    hidden = list()
    hidden.append(h)
    for i in range(len(x1)):
        X = np.array([[x1[i], x2[i]]])
        Y = y[i]
        # forward propogation
        h = sigmoid(np.dot(X, wx) + np.dot(h, wh))
        #         print(h, 'onh')
        a = sigmoid(h.dot(wy))

        # check loss
        loss = Y - a
        delta = loss * sigder(a)
        layer2_delta.append(delta)
        hidden.append(copy.deepcopy(hidden_layers))

        feature = np.zeros(hidden_layers)
        pred.append(a)

    print(pred)


    # backpropogation
    for j in range(len(x1) - 1, -1, -1):
        current_hidden = hidden[j + 1]
        X = np.array([[x1[j], x2[j]]])

        previous_hidden = hidden[j]
        delta_layer = layer2_delta[j]

        neuron_delta = feature_layer_delta.dot(wh.T) + delta_layer.dot(wy.T) + sigder(current_hidden)
        wy_update += np.atleast_2d(current_hidden).T.dot(delta_layer)
        wh_update += np.atleast_2d(previous_hidden).T.dot(neuron_delta)
        wx_update += X.T.dot(neuron_delta)

        feature = neuron_delta

    wy += wy_update * lr
    wx += wx_update * lr
    wh += wh_update * lr

    wy_update *= 0
    wx_update *= 0
    wh_update *= 0