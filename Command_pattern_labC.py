

class Imvoker(Object):

	"""Clase Invocadora"""

	def __init__(self, Door, cas_actual):
		self.door = Door
		self.cas_actual = cas_actual

	def AbrirPuerta(self, id):

		if id == "Derecha":
			
			self.door.Execute()
		else:
			print "No autorizado"
			return

	def CerrarPuerta(self, id):
	
		if id == "Derecha":
			self.door.Execute()
		else:
			print "No autorizado"
			return	

	def PasarA(self, cas_next):

		self.door.Atravesar(self.cas_actual,cas_next)


class Casilla(Object):

	"""Clase Recibidora"""


	def __init__(self, cas_actual):
		self.cas_actual = cas_actual

	def get_casilla(self):
		return self.cas_actual

	def modificar(self, cas_next):
		self.cas_actual = cas_next			

	def Open(self):
		return  "La puerta está abierta"

	def Close(self):
		return "la puerta está cerrada"

	def Pasar(self, cas_next):
		self.cas_actual = cas_next
		return "Se ha cambiado la posición"

class Operador(Object):

	"""Clase Comandadora, Abstracta"""


	def __init__(self):
		pass

	def Execute(self):
		pass

	def Atravesar(self):
		pass

class AbriendoPuerta(Operador):
	"""Clase Comandadora"""

	def __init__(self, Casilla):
		self.casilla = Casilla

	def Execute(self):
		self.cassilla.Open()

class CerrandoPuerta(Operador):
	"""Clase Comandadora"""

	def __init__(self, Casilla):
		self.casilla = Casilla

	def Execute(self):
		self.casilla.Close()

class AtravesandoPuerta(Object):
	"""Clase Comandadora"""
	
	def __init__(self, Casilla):
		self.casilla = Casilla

	def Atravesar(self, cas_next):
		self.casilla.modificar(cas_next)











				
			