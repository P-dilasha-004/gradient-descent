import numpy as np 
import matplotlib.pyplot as plt

def z_function(x,y):
  #return 20 * (x ** 2) + 20 * (y ** 2)
  return np.sin(5 * x) * np.cos(5 * y) / 5 

# the gradient of function z(x,y) is [dz/dx, dz/dy]
def calculate_gradient(x,y):
  #return 20 * 2 * x, 20 * 2 * y 
  return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)

x = np.arange(-1,1,0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x,y)
Z = z_function(X,Y)

ax = plt.subplot(projection='3d', computed_zorder = False)

current_pos = (0.7, 0.4, z_function(0.7, 0.4))

# defines the step-size, how fast we want to move closure to the minimum
learning_rate = 0.01

plt.ion()
for i in range(1000):
  
  X_derivative, Y_derivative = calculate_gradient(current_pos[0], current_pos[1])
  X_new, Y_new = current_pos[0] - learning_rate * X_derivative, current_pos[1] - learning_rate * Y_derivative
  current_pos = X_new, Y_new, z_function(X_new, Y_new)
  
  ax.plot_surface(X,Y,Z, cmap="viridis", zorder = 0 )
  ax.scatter(current_pos[0], current_pos[1], current_pos[2], color="magenta", zorder= 1)
  plt.pause(0.001)
  ax.clear()
