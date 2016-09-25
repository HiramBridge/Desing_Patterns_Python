""" Programa para generar claves"""


import random


class Key_Gen:


	"""Generador de Clave"""

	def __init__(self, FabricaClaves = None):
		self.fabricaclaves = FabricaClaves

	def Mostrar_clave(self):
		"""Crea y muestra la clave generada a través de la clase abstracta FabricaClaves"""
		clave = self.fabricaclaves.get_clave()
		print("la clave generada fue {}".format(clave.Imprimir()))

""" Concrets """

class Ramdom_Key:

	def Imprimir(self):
		return "Clave previamente Generada"

	def __str__(self):
		return "Clave"

class Key_Factory:

	def get_clave(self):
		return Ramdom_Key()


if __name__ == "__main__":
	for i in range(4):
		generador = Key_Gen(Key_Factory())
		generador.Mostrar_clave()
		print("=" * 20)



		










