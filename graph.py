## We are using the edge list representation to 
## form a graph. 
## If a node is not connected to any other nodes, we do not 
## list it in the graph. Hence the second if condition.
## { 'a': ['b', 'c']}
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                paths.append(newpath)

    return paths



graph = {
        'A': ['B', 'C'],
        'B': ['D', 'C'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
}


print find_path(graph, 'B', 'F')
print find_path(graph, 'A', 'F')
print find_path(graph, 'A', 'D')

print "All Paths between A & D"
print find_all_paths(graph, 'A', 'D')
