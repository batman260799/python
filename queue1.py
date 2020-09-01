from collections import deque as d
class Queue:
	def __init__(self):
		self.queue=d()
	def enqueue(self,element):
		self.queue.appendleft(element)
	def dequeuee(self):
		return self.queue.pop()
	def is_empty(self):
		return len(self.queue)<0
	def peek(self):
		return self.queue[-1]
	def length(self):
		return len(self.queue)
q=Queue()
q.enqueue("Dheeraj")
q.enqueue("Manisha")
q.enqueue("Mom")
#print(q.queue)
print(q.dequeuee())
print(q.peek())
print(q.is_empty())