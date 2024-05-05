port networkx as nx

def dijkstra(graph, start_node):
    shortest_distances = {node: float('infinity') for node in graph.nodes()}
    shortest_distances[start_node] = 0  
    
    pred = {}
    
    unvisited_nodes = list(graph.nodes())
    
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: shortest_distances[node])
        unvisited_nodes.remove(current_node)

        # actualizar
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_distance = shortest_distances[current_node] + weight
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
    
    return shortest_distances, predecessors


