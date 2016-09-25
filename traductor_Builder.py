
class Lector(object):

	"""Clase director. Implementa al constructor(Traductor)"""
	def __init__(self, Traductor):
		self.traductor = Traductor

	def Traduciendo_texto(self, Texto):
		self.texto = Texto
		self.traductor.traducir()
		self.traductor.ingresar_texto(self.texto)
		self.traductor.texto_traducido("Hola como estas")

	def Retornar_traduccion(self):
		return self.traductor.traduccion		
	


class Traductor(object):  

	"""Abstract Construct (Constructor)"""

	def __init__(self):
		self.text = None

	def traducir(self):
		self.traduccion = Traduccion()

	def ingresar_texto(self, Text):
		pass

	def texto_traducido(self, text):
		pass
			

class traductor_ingles(Traductor): 

	"""Concrete Construct"""
	def ingresar_texto(self, Text):
		self.traduccion.texto = Text

	def texto_traducido(self, Text):
		self.traduccion.texto_traduct = Text		
	                 
	
class Traduccion(object):  

	"""clase Producto"""

	def __init__(self):
		self.texto = None
		self.texto_traduct = None

	def __repr__(self):
		return 'Texto Original: {0.texto} | Texto Traducido: {0.texto_traduct}'.format(self)	
	


if __name__ == "__main__":
	
	lector = Lector(traductor_ingles())
	lector.Traduciendo_texto("How are you")
	texto_final = lector.Retornar_traduccion()
	print (texto_final)




		





