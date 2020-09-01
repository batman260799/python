class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
class linkedlist:
	def __init__(self):
		self.head=None
	def insert_at_begin(self,data):
		node=Node(data,self.head)
		self.head=node
		#if self.head:
		#	self.head=Node(data,self.head.next)
		#else:
		#	self.head=Node(data,None)
	def insert_at_end(self,data):
		itr=self.head
		while itr.next:
			itr=itr.next
		itr.next=Node(data,None)
	def insert_list(self,list):
		for i in list:
			self.insert_at_end(i)
	def length(self):
		l=0
		itr=self.head
		while itr:
			l+=1
			itr=itr.next
		return l
	def insert_at_index(self,index,element):
		if index<0 or index>=self.length():
			raise Exception("InvalidIndex") 
			return
		if index==1:
			self.insert_at_begin(element)
			return
		count=0
		itr=self.head
		while itr:
			count+=1
			if count==index-1:
				itr.next==Node(element.itr.next)
			itr=itr.next
	def remove_at_index(self,index):
		if index<0 or index>=self.length():
			raise Exception("InvalidIndex")
			return
		if index==1:
			self.head=self.head.next
			return
		count=0
		itr=self.head
		while itr:
			count+=1
			if count==index-1:
				itr.next=itr.next.next
			itr=itr.next
	def insert_after_value(self,val,aval):
		itr=self.head
		while itr:
			if itr.data==val:
				itr.next=Node(aval,itr.next)
			itr=itr.next
	def show(self):
		itr=self.head
		lstr=""
		while itr:
			lstr=lstr+str(itr.data)+"----->"
			itr=itr.next
		return lstr
l=linkedlist()
l.insert_at_begin(210)
l.insert_list(["Batman","SuperMan","WonderWoman","AquaMan","Cyborg"])
l.insert_at_index(1,"Dheeraj")
#l.remove_at_index(5)
l.insert_after_value("Batman","Manisha")
print(l.length())
print(l.show())