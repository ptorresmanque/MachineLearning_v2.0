import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fmin_bfgs

# Define sigmoid, cost function and gradients
def sigmoid(z):
  return 1 / (1 + sp.exp(-z))

def cost_function(theta, X, Y):
  theta = sp.matrix(theta).T
  J = (1 / m) * (-Y.T * sp.log(sigmoid(X * theta)) - ((1 - Y).T * sp.log(1 - sigmoid(X * theta))))
  print(J)
  return J[0, 0]

def gradients(theta, X, Y):
  theta = sp.matrix(theta).T
  grad = ((1 / m) * X.T * (sigmoid(X * theta) - Y)).T
  grad = sp.squeeze(sp.asarray(grad))
  return grad

def predict(theta, X):
  return sp.around(sigmoid(X * theta))

# Load data from data source 1
data = sp.matrix(sp.loadtxt("data.txt", delimiter=' '))
X = data[:, 0:2]
X = (X - mean(X))/std(X) 
Y = data[:, 2]
m, n = X.shape

# Compute cost and gradients
# Initialize
X = sp.hstack((sp.ones((m, 1)), X))
theta = sp.zeros(n+1) # Use row vector instead of column vector for applying optimization

# Optimize using fmin_bfgs
res = fmin_bfgs(cost_function, theta, fprime=gradients,disp=True, maxiter=100, args=(X, Y))
theta = sp.matrix(res).T

# Plot fiqure 1 (data)                 
plt.figure(1)
plt.xlabel('x1')
plt.ylabel('x2')

pos = sp.where(Y == 1)[0]
neg = sp.where(Y == 0)[0]

plt.plot(X[pos, 1], X[pos, 2], 'k+', linewidth=2, markersize=7)
plt.plot(X[neg, 1], X[neg, 2], 'ko', markerfacecolor='y', markersize=7)

# Plot fiqure 2 (decision boundary)
plt.figure(2)
plt.xlabel('x1')
plt.ylabel('x2')

pos = sp.where(Y == 1)[0]
neg = sp.where(Y == 0)[0]

plt.plot(X[pos, 1], X[pos, 2], 'k+', linewidth=2, markersize=7)
plt.plot(X[neg, 1], X[neg, 2], 'ko', markerfacecolor='y', markersize=7)

if X.shape[0] >= 3:
  plot_x = sp.array([sp.amin(X[:, 1]) - 2, sp.amax(X[:, 1]) + 2])
  plot_y = (-1 / theta[2, 0]) * (theta[0, 0] + theta[1, 0] * plot_x)
  plt.plot(plot_x, plot_y)
  plt.savefig('1.png')

p = predict(theta, X)
r = sp.mean(sp.double(p == Y)) * 100

print("Train Accuracy: {r}%".format(**locals()))