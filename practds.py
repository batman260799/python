class graph:
	def __init__(self,edges):
		self.edges=edges
		self.graph_dict={}
		for start,end in self.edges:
			if start in self.graph_dict:
				self.graph_dict[start].append(end)
			else:
				self.graph_dict[start]=[end]
	def find_path(self,start,end,path=[]):
		path=path+[start]
		if start==end:
			return [path]
		if start not in self.graph_dict:
			return []
		paths=[]
		for node in self.graph_dict[start]:
			if node not in path:
				new_path=self.find_path(node,end,path)
				for p in new_path:
					paths.append(p)
		return paths
	def shortest_paths(self,start,end,path=[]):
		path=path+[start]
		if start==end:
			return path
		if start not in self.graph_dict:
			return None
		shortest_path=None
		for node in self.graph_dict[start]:
			if node not in path:
				sp=self.shortest_paths(node,end,path)
				if sp:
					if shortest_path is None or len(sp)<len(shortest_path):
						shortest_path=sp
		return shortest_path



if __name__=="__main__":
		routes=[("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","NewYork"),("Dubai","NewYork"),("NewYork","Toronto")]
		route_graph=graph(routes)
		start="Mumbai"
		end="NewYork"
		print("The Available routes between {} and {} are:".format(start,end),route_graph.find_path(start,end))
		print("The Shortest path/paths between {} and {} is/are:".format(start,end),route_graph.shortest_paths(start,end))
