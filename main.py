from grafo import Grafo
import sys


def find_all_paths(graph, start, end, path=[], p=0):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph.keys():
            return []
        paths = []
        p = 0
        for node in graph[start]:
            if node[0] not in path:
                p += node[1]
                newpaths = find_all_paths(graph, node[0], end, path, p)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths


def get_arestas_input():
    new_arestas = []
    with open("input.txt") as f:
        for line in f:
            input_ = line.split(" ")
            tup = (str(input_[0]), str(input_[1]), int(input_[2]))
            new_arestas.append(tup)

    return new_arestas


if __name__ == "__main__":
    arestas = get_arestas_input()
    grafo = Grafo(arestas, direcionado=True)
    list_paths = find_all_paths(grafo.adj, sys.argv[1], sys.argv[2])
    group_list = []
    for lists in list_paths:
        new_list = []
        for i in range(len(lists)-1):
            new_list.append((lists[i], lists[i+1]))
        group_list.append(new_list)

    list_sum = []
    for each in group_list:
        sum_ = 0
        for k1, k2 in each:
            for item in grafo.adj[k1]:
                if item[0] == k2:
                    sum_ += item[1]
        list_sum.append(sum_)

    for i in range(len(list_paths)):
        print("Network Way: {} Latency: {}".format(list_paths[i], list_sum[i]))
