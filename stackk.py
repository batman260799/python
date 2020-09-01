from collections import deque as d
class Stack:
	def __init__(self):
		self.stack=d()
	def push(self,data):
		self.stack.append(data)
	def pop(self):
		return self.stack.pop()
	def length(self):
		return len(self.stack)
	def peek(self):
		return self.stack[-1]
	def is_empty(self):
		return self.length()<0
s=Stack()
s.push("Harry Potter")
s.push("Lord of Rings")
s.push("Batman")
print(s.length())
print(s.pop())
print(s.stack)