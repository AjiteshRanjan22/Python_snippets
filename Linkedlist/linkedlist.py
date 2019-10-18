class Node:
	def __init__(self,data):
		self.data = data
		self.next =None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newNode):
		if self.head is None:
			self.head = newNode
			
		else:
			lastNode = self.head
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode

	def printlist(self):

		if self.head == None:
			print("List is empty")

		currentnode = self.head

		while True:
			print(currentnode.data,end = ' ')
			if currentnode.next == None:
				break
			currentnode = currentnode.next
