import numpy as np

X = np.array([[2, 9],
              [1, 5],
              [3, 6]], dtype=float)

Y = np.array([[92],
              [86],
              [89]], dtype=float)

Y = Y / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivative_sigmoid(x):
    return x * (1 - x)

input_neurons  = 2      
hidden_neurons = 3     
output_neurons = 1      

lr = 0.1                
epochs = 5000         

wh = np.random.uniform(size=(input_neurons, hidden_neurons))
bh = np.random.uniform(size=(1, hidden_neurons))

wout = np.random.uniform(size=(hidden_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for epoch in range(epochs):

    # Forward Propagation
    hidden_input = np.dot(X, wh) + bh
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, wout) + bout
    output = sigmoid(final_input)

    # Backpropagation
    error = Y - output
    d_output = error * derivative_sigmoid(output)

    error_hidden = d_output.dot(wout.T)
    d_hidden = error_hidden * derivative_sigmoid(hidden_output)

    # Update weights
    wout += hidden_output.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hidden) * lr
    bh += np.sum(d_hidden, axis=0, keepdims=True) * lr

print("\nFinal Predictions (0–1 scaled):")
print(output)

print("\nFinal Predictions (Original Scale):")
print(output * 100)