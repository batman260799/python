class graph:
	def __init__(self,edges):
		self.edges=edges
		self.graph_dict={}
		for start,end in self.edges:
			if start in self.graph_dict:
				self.graph_dict[start].append(end)
			else:
				self.graph_dict[start]=[end]
	def find_paths(self,start,end,path=[]):
		path=path+[start]
		if start==end:
			return [path]
		if start not in self.graph_dict:
			return []
		paths=[]
		for node in self.graph_dict[start]:
			if node not in path:
				new_paths=self.find_paths(node,end,path)
				for p in new_paths:
					paths.append(p)
		return paths
	def short_paths(self,start,end,path=[]):
		path=path+[start]
		if start==end:
			return path
		if start not in self.graph_dict:
			return None
		Shortest_path=None
		for node in self.graph_dict[start]:
			if node not in path:
				sp=self.short_paths(node,end,path)
				if sp:
					if Shortest_path is None or len(sp)<=len(Shortest_path):
						Shortest_path=sp
		return Shortest_path

if __name__=="__main__":
	routes=[("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","NewYork"),("Dubai","NewYork"),("NewYork","Toronto")]
	route_graph=graph(routes)
	print(route_graph.graph_dict)
	start="Mumbai"
	end="NewYork"
	print("The Available paths between {} and {} are:".format(start,end),route_graph.find_paths(start,end))
	print("The Shortest Path between {} and {} are:".format(start,end),route_graph.short_paths(start,end))