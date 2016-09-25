from abc import ABCMeta, abstractmethod


class Publisher(metaclass=ABCMeta):
	""" interfaz Observable"""
	def __init__(self):
		pass
	
	def addObserver(self, observer):
		pass
		
	def removeObserver(self, observer):
		pass
	
	def notifyAll(self):
		pass

class PlatziForum(Publisher):
	def __init__(self):
		self.usersList = []
		self.post = None
		
	def addObserver(self, observer):
		if observer not in self.usersList:
			self.usersList.append(observer)
		
	def removeObserver(self, observer):
		self.usersList.remove(observer)
	
	def notifyAll(self):
		for observer in self.usersList:
			observer.notify(self.post)
			
	def writePost(self, text):
		self.post = text
		self.notifyAll()
		
		
class Subscriber:
	def __init__(self):
		pass
	def notify(self, post):
		pass
		
class UserA(Subscriber):
	
	def __init__(self):
		pass
	def notify(self, post):
		print("UserA ha sido notificado %s" % post)
		
class UserB(Subscriber):
	
	def __init__(self):
		pass
	def notify(self, post):
		print("UserB ha sido notificado %s" % post)

if __name__ == "__main__":
	foroPlatzi = PlatziForum()
	user1 = UserA()
	user2 = UserB()
	
	foroPlatzi.addObserver(user1)
	foroPlatzi.addObserver(user2)
	
	foroPlatzi.writePost("mi primer post en Platzi")
	
	foroPlatzi.removeObserver(user2)
	
	foroPlatzi.writePost("mi segundo post ")
	