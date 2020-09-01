class BST:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	def add_child(self,child):
		if child==self.data:
			return
		if child<self.data:
			if self.left:
				self.left.add_child(child)
			else:
				self.left=BST(child)
		else:
			if self.right:
				self.right.add_child(child)
			else:
				self.right=BST(child)
	def in_order_traversal(self):
		elements=[]
		if self.left:
			elements+=self.left.in_order_traversal()
		elements.append(self.data)
		if self.right:
			elements+=self.right.in_order_traversal()
		return elements
	def find_min(self):
		if self.left is None:
			return self.data
		if self.left:
			return self.left.find_min()
	def find_max(self):
		if self.right is None:
			return self.data
		if self.right:
			return self.right.find_max()
	def sum(self):
		s=0
		if self.left:
			s+=self.left.sum()
		s+=self.data
		if self.right:
			s+=self.right.sum()
		return s
	def search(self,val):
		if val==self.data:
			return "found"
		if val<self.data:
			if self.left:
				return self.left.search(val)
			else:
				return "Not found"
		else:
			if self.right:
				return self.right.search(val)
			else:
				return "Not found"
	def delete(self,val):
		if val<self.data:
			self.left=self.left.delete(val)
		elif val>self.data:
			self.right=self.right.delete(val)
		else:
			if self.left is None and self.right is None:
				return None
			if self.left is None:
				return self.right
			if self.right is None:
				return self.right
			min_val=self.right.find_min()
			self.data=min_val
			self.right=self.right.delete(min_val)
		return self
def build_tree(data):
	root=BST(data[0])
	for i in range(1,len(data)):
		root.add_child(data[i])
	return root
if __name__=="__main__":
	rt=build_tree([32,21,56,89,0,1,45,2])
	print(rt.in_order_traversal())
	print(rt.search(2100))
	print(rt.find_min())
	print(rt.find_max())
	print(rt.sum())
	rt.delete(2)
	rt.delete(89)
	print(rt.in_order_traversal())


