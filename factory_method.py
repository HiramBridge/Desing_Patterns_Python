from abc import ABCMeta
class Pizza (metaclass = ABCMeta):
	def __init__(self):
		self.tamanio = None
		self.salsa = None

	def __str__(self):
		return "la pizza tiene tamanio {:s} y salsa {:s}".format(self.tamanio,self.salsa)

class Margarita(Pizza):
	def __init__ (self):
		self.tamanio = "Grande"
		self.salsa = "Roja"

class Pepperonni(Pizza):
	def __init__(self):
		self.tamanio = "Pequeño"
		self.salsa = "Azul"

class Cocina:
	def crear_pizza (self, tipo):
		self.pizza = None
		if tipo == "Margarita":
			self.pizza = Margarita();
		elif tipo == "Pepperonni":
			self.pizza = Pepperonni();
		else:
			print ("El tipo de pizza {:s} no se encuentra".format(tipo))
		return self.pizza

	def Imprimir(self):
		print(self.pizza)	

if __name__ == "__main__":
	cocina = Cocina()
	pizza1 = cocina.crear_pizza("Margarita")
	pizza2 = cocina.crear_pizza("Pepperonni")
	print(pizza1)
	print(pizza2)


	

