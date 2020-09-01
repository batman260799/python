class hashmap:
	def __init__(self):
		self.MAX=100
		self.arr=[[] for i in range(self.MAX)]
	def get_hash(self,key):
		count=0
		for i in key:
			count+=ord(i)
		return count%self.MAX
	def __setitem__(self,key,value):
		for index,element in enumerate(self.arr[self.get_hash(key)]):
			if len(element)==2 and element[0]==key:
				self.arr[self.get_hash(key)][index]=(key,value)
				return
		self.arr[self.get_hash(key)].append((key,value))
	def __getitem__(self,key):
		for index,element in enumerate(self.arr[self.get_hash(key)]):
			if len(element)==2 and element[0]==key:
				return self.arr[self.get_hash(key)][index]
	def __delitem__(self,key):
		for index,element in enumerate(self.arr[self.get_hash(key)]):
			if len(element)==2 and element[0]==key:
				del self.arr[self.get_hash(key)][index]
h=hashmap()
h["Dheeraj"]=60000
h["Manisha"]=70000
h["jareehD"]=100000
h["Dheeraj"]=600000000
print(h.arr)
print(h["Manisha"])
print(h["Dheeraj"])
del h["Dheeraj"]
print(h["Dheeraj"])