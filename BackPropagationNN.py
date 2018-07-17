import numpy as np
import time

class NeuralNetwork(object):

	def __init__(self, inputs, hidden, outputs, activation='tanh', output_act='sigmoid'):
		
		# Función de activación de capa oculta
		if activation == 'sigmoid':
			self.activation = sigmoid
			self.activation_prime = sigmoid_prime
		elif activation == 'tanh':
			self.activation = tanh
			self.activation_prime = tanh_prime
		elif activation == 'linear':
			self.activation = linear
			self.activation_prime = linear_prime

		# Función de activación de la capa de salida
		if output_act == 'sigmoid':
			self.output_act = sigmoid
			self.output_act_prime = sigmoid_prime
		elif output_act == 'tanh':
			self.output_act = tanh
			self.output_act_prime = tanh_prime
		elif output_act == 'linear':
			self.output_act = linear
			self.output_act_prime = linear_prime
		elif output_act == 'softmax':
			self.output_act = softmax
			self.output_act_prime = linear_prime

		# Inicialización de pesos
		self.wi = np.random.randn(inputs, hidden)/np.sqrt(inputs)
		self.wo = np.random.randn(hidden + 1, outputs)/np.sqrt(hidden)

		# Inicialización de pesos de actualizacion
		self.updatei = 0
		self.updateo = 0


	def feedforward(self, X):

		# Activación de capa oculta
		ah = self.activation(np.dot(X, self.wi))
			
		# Agregar baias a los resultados de la capa oculta
		ah = np.concatenate((np.ones(1).T, np.array(ah)))

		# salidas
		y = self.output_act(np.dot(ah, self.wo))

		# Return los resultados
		return y


	def fit(self, X, y, epochs=10, learning_rate=0.2, learning_rate_decay = 0 , momentum = 0, verbose = 0):
		
		# Timer 
		startTime = time.time()

		
		for k in range(epochs):
	
			# Dataset loop
			for i in range(X.shape[0]):

				# Activación de capa oculta
				ah = self.activation(np.dot(X[i], self.wi))
			
				# Agregar baias a la capa oculta
				ah = np.concatenate((np.ones(1).T, np.array(ah))) 

				# salida
				ao = self.output_act(np.dot(ah, self.wo))

				# Deltas	
				deltao = np.multiply(self.output_act_prime(ao),y[i] - ao)
				deltai = np.multiply(self.activation_prime(ah),np.dot(self.wo, deltao))

				# Actualización de pesas con momentun
				self.updateo = momentum*self.updateo + np.multiply(learning_rate, np.outer(ah,deltao))
				self.updatei = momentum*self.updatei + np.multiply(learning_rate, np.outer(X[i],deltai[1:]))

				# actualizacion de pesos
				self.wo += self.updateo
				self.wi += self.updatei

			# impresion del status
			if verbose == 1:
				print ('Ciclo: {0:4d}/{1:4d}\t\tLearning rate: {2:4f}\t\tTiempo [Segundos]: {3:5f}'.format(k,epochs,learning_rate, time.time() - startTime))
				
			# actualizacion del porcentaje de entrenamiento(learning rate)
			learning_rate = learning_rate * (1 - learning_rate_decay)

	def predict(self, X): 

		# arreglo para las salidas
		y = np.zeros([X.shape[0],self.wo.shape[1]])

		# ciclo de la entrada
		for i in range(0,X.shape[0]):

			y[i] = self.feedforward(X[i])

		# Return de los resultados
		return y


# Posibles funciones de activacion
def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
	return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
	return np.tanh(x)

def tanh_prime(x):
	return 1.0 - x**2

def softmax(x):
    return (np.exp(np.array(x)) / np.sum(np.exp(np.array(x))))

def softmax_prime(x):
    return softmax(x)*(1.0-softmax(x))

def linear(x):
	return x

def linear_prime(x):
	return 1
