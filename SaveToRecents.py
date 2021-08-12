import pickle

class RecentsDBEditor(object):

	maxItems = 10
	def __init__(self, listPath):
		self.listPath = listPath

		try:		
			with open(listPath, "rb") as file:
				self.recentsList = pickle.load(file)
		except:
			print(f"Warning: No database file found at {listPath}, A new file will be created.")
			self.recentsList = []

		self.recentsListLength = len(self.recentsList)

	def addToDB(self,filename):

		alreadyExists = False

		for SavedFile in self.recentsList:
			if SavedFile == filename:
				alreadyExists = True

		if not alreadyExists:
			self.recentsList.append(filename)
			if self.recentsListLength > self.maxItems:
				self.recentsList.pop(0)

	def saveChangesToDB(self):
		with open(self.listPath, "wb") as file:
			pickle.dump(self.recentsList, file)

	def printDB(self):
		for i in range(self.recentsListLength):
			print(f"{i}) {self.recentsList[i]}")

	def getFileFromDB(self, index):
		return self.recentsList[int(index)]

#some shortcuts:

def saveToRecentsDBDecorator(func, listPath):
	""" File name must be entered as a key word arguement on the original function. The arguement's name should be just 'file'. """
	def wrapper(*args, **kwargs):
		editor = RecentsDBEditor(listPath)
		result = func(*args, **kwargs)
		editor.addToDB(kwargs["file"])
		editor.saveChangesToDB()

		return result
	return wrapper

def printDBFile(listPath):
	editor = RecentsDBEditor(listPath)
	editor.printDB()

def saveToRecentsDB(listPath,filename):
	editor = RecentsDBEditor(listPath)
	editor.addToDB(filename)
	editor.saveChangesToDB()





		