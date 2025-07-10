import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def y_function(x):
    return x ** 2 

# derivative of x**2 is 2x
def y_derivative(x):
    return 2 * x 


current_pos = (1.5, y_function(1.5))
print(current_pos)

# defines the step-size, how fast we want to move closure to the minimum
learning_rate = 0.01

print(matplotlib.get_backend())

plt.ion()
for i in range(1000):
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)

    x = np.arange(-5, 5, 0.1)
    y = y_function(x)  # the square of each point of x

    plt.clf()

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color="red")
    plt.pause(0.0001)

plt.ioff()
plt.show()
