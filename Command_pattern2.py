#!/usr/bin/env python
# -*-coding:utf-8-*-

class Interruptor:


	"""clase invocadora"""
	def __init__(self, encenderluz, apagarluz):
		self.apagar = encenderluz
		self.prender = apagarluz

	def TurnOn(self):
		self.prender.execute()

	def TurnOff(self):
		self.apagar.execute()

class Luz:
	"""clase recibidora"""

	def ON(self):
		print "la luz está encendida"

	def OFF(self):
		print "la luz esta apagada"

class Command:
	"""Clase comando Abstracta"""
	def __init__(self):
		pass

	def execute(self):
		pass

class EncenderLuz(Command):
	"""Clase comando que enciende la luz"""
	def __init__(self, luz):
		self.luz = luz

	def execute(self):
		self.luz.ON()

class ApagarLuz(Command):
	"""Clase comando que apaga la luz"""

	def __init__(self, luz):
		self.luz = luz


	def execute(self):
		self.luz.OFF()

class ClienteLuz:
	""" clase cliente"""

	def __init__(self):
		self.lampara = Luz()
		self.encenderluz = EncenderLuz(self.lampara)
		self.apagarluz = ApagarLuz(self.lampara)
		self.interruptor = Interruptor(self.encenderluz, self.apagarluz)

	def eleccion(self, cmd):
		self.cmd = cmd.strip().upper()

		try:
			if self.cmd  == "ON":
				self.interruptor.TurnOn()
			elif self.cmd  == "OFF":
				self.interruptor.TurnOff()
			else:
				print "Argumento ON o Off es requerido"
		except Exception, msg:
			print "Exception occured: %s" % msg

if __name__ == "__main__": 
	
	Apagador = ClienteLuz() 

	print "Switch ON test." 
	Apagador.eleccion("ON") 

	print "Switch OFF test" 
	Apagador.eleccion("OFF") 

	print "Invalid Command test"
	Apagador.eleccion("****")					 	


