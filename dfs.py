#IMPLEMENTAÇÃO DA FUNÇÃO DFS(Busca em profundidade)
graph = {'A': ['B', 'D', 'E'],
         'B': ['A', 'C', 'E'],
         'C': ['B', 'E'],
         'D': ['A', 'E'],
         'E': ['A', 'B', 'C', 'D', 'F'],
         'F': ['E']}

visited = set()

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'B')



