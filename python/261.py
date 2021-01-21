from collections import defaultdict 

def validTree( n, edges):
	graph = defaultdict(list)
	for x, y in edges:
		graph[x].append(y)
		graph[y].append(x)
	visit = [False] * n

	def helper(graph, visit, cur, pre):
		if visit[cur]:
			return False
		visit[cur] = True

		for node in graph[cur]:
			if node != pre:
				if not helper(graph, visit, node, cur):
					return False
		return True
	if not helper(graph, visit, 0, -1):
		return False
	if any( not i for i in visit):
		return False

	return True
