class tree:
	def __init__(self,data):
		self.data=data
		self.children=[]
		self.parent=None
	def add_child(self,child):
		child.parent=self
		self.children.append(child)
	def get_level(self):
		l=0
		p=self.parent
		while p:
			l+=1
			p=p.parent
		return l
	def print_tree(self):
		space=" "*self.get_level()*3
		prefix=space+"|......."if self.parent else ""
		print(prefix+self.data)
		if self.children:
			for child in self.children:
				child.print_tree()
def build_tree():
	root=tree("Electronics")
	lap=tree("Laptops")
	mob=tree("Mobiles")
	tv=tree("TV'S")
	lap.add_child(tree("DELL"))
	lap.add_child(tree("HP"))
	lap.add_child(tree("ASUS"))
	mob.add_child(tree("realme"))
	mob.add_child(tree("Xiaomi"))
	mob.add_child(tree("Samsung"))
	tv.add_child(tree("Sony"))
	tv.add_child(tree("MI"))
	tv.add_child(tree("Panasonic"))
	root.add_child(lap)
	root.add_child(mob)
	root.add_child(tv)
	return root
if __name__=="__main__":
	rt=build_tree()
	rt.print_tree()
