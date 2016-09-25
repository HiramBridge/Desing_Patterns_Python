from abc import ABCMeta

class Command(metaclass=ABCMeta):
	def execute(self):
		pass


class Light:
	""" clase Receiver"""
	def turnOn(self):
		print("foco encendido")
		
	def turnOff(self):
		print("foco apagado")
		

class Switch:
	""" clase Invoker"""
	def __init__(self, onCommand, offCommand):
		self._onCommand = onCommand
		self._offCommand = offCommand
		
		
	def on(self):
		self._onCommand.execute();
		
	def off(self):
		self._offCommand.execute();
		
	
class OnCommand(Command):
	def __init__(self, light):
		self._light = light
		
	def execute(self):
		self._light.turnOn()
		
class OffCommand(Command):
	def __init__(self, light):
		self._light = light
		
	def execute(self):
		self._light.turnOff()


class LightSwitch:
	""" clase Client"""
	def __init__(self):
		self._foco = Light()
		self._switchUp = OnCommand(self._foco)
		self._switchDown = OffCommand(self._foco)
		self._switch = Switch(self._switchUp, self._switchDown)
		
	def operation(self, cmd):
		if cmd =="ON":
			self._switch.on()
		elif cmd =="OFF":
			self._switch.off()
		else:
			print("Operación invalida")
			
if __name__ == "__main__":
	client = LightSwitch()
	print("testing on command")
	client.operation("ON")
	print("testing off command")
	client.operation("OFF")
		