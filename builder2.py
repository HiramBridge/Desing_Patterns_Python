"""Construcción de Inmoviliarios usando el diseño Builder"""
""" partes de Builder: Director, Constructor, Costructor_Concreto, Producto y el cliente """



class Director(object):

	def __init__(self):
		self.constructor = None

	def construyendo_estructura(self):
		self.constructor.iniciando_construccion()
		self.constructor.construir_piso()
		self.constructor.construir_paredes()

	def retornar_construccion(self):
		return self.constructor.construyendo


class Constructor(object):

	def __init__(self):
		self.construyendo = None

	def iniciando_construccion(self):
		self.construyendo = Construyendo()

	def construir_piso(self):
		pass	

	def construir_paredes(self):
		pass		

""" Constructores Concretos """


class ConstruirCasa(Constructor):

	def construir_piso(self):
		self.construyendo.piso = 'Granito'

	def construir_paredes(self):
		self.construyendo.paredes = 'Blancas'

class ConstruirDepartamento(Constructor):

	def construir_piso(self):
		self.construyendo.piso = 'Marmol'

	def construir_paredes(self):
		self.construyendo.paredes = 'Azules'


""" La clase producto es justamente Construyendo """

class Construyendo(object):

	def __init__(self):
		self.piso = None
		self.paredes = None

	def __repr__(self):
		return 'Piso: {0.piso} | Paredes: {0.paredes}'.format(self)



"""Cliente """

if __name__ == "__main__":

	director = Director()
	director.constructor = ConstruirDepartamento()
	director.construyendo_estructura()
	construyendo = director.retornar_construccion()
	print(construyendo)

