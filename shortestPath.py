from mapToGraph import graph

info = graph()
graph1 = info[0]
end_points = info[1]
start_point = info[2]
print(start_point[0])
graph = {}
for i in range(len(graph1)):
    x = graph1[i][0]
    y = graph1[i][1]

    if x == 10 and y == 10:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y + 16}": y + 16, f"siema{x + 16}od{y}" : x + 16}})
    
    elif x == 10 and y == 650:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y - 16}": y - 16, f"siema{x + 16}od{y}" : x + 16}})
    
    elif x == 618 and y == 10:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y + 16}": y + 16, f"siema{x - 16}od{y}" : x - 16}})
    
    elif x == 618 and y == 650:
        graph.update({f"siema{x}od{y}" : {f"siema{x - 16}od{y}" : x - 16, f"siema{x}od{y - 16}": y - 16}})

    elif y == 650:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y - 16}": y - 16, f"siema{x + 16}od{y}" : x + 16, f"siema{x - 16}od{y}" : x - 16}})

    elif y == 10:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y + 16}": y + 16, f"siema{x - 16}od{y}": x - 16, f"siema{x + 16}od{y}" : x + 16}})

    elif x == 10:
        graph.update({f"siema{x}od{y}" : {f"siema{x + 16}od{y}" : x + 16, f"siema{x}od{y - 16}" : y - 16, f"siema{x}od{y + 16}" : x + 16}})

    elif x == 618:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y - 16}": y - 16, f"siema{x - 16}od{y}" : x - 16, f"siema{x}od{y + 16}" : x + 16}})
        
    else:
        graph.update({f"siema{x}od{y}" : {f"siema{x}od{y - 16}": y - 16, f"siema{x + 16}od{y}" : x + 16, f"siema{x - 16}od{y}" : x - 16, f"siema{x}od{y + 16}" : y + 16}})


def dijkstra(graph, start, goal):
    shortest_distance = {} 
    track_predecessor = {} 
    unseenNodes = graph 
    infinity = 9999999999999999999
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        
        path_options = graph[min_distance_node].items()


        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except:
            print("Nie ma takiej drogi")
            break

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print("Najmniejszy koszt to %s" % str(shortest_distance[goal]))
        print("Najszybsza droga to %s" % str(track_path))


dijkstra(graph, f"siema{start_point[0]}od{start_point[1]}", f"siema{end_points[0][0]}od{end_points[0][1]}")
