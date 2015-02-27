#!/usr/bin/env python
from collections import defaultdict
import fileinput


def build_graph(input):
    graph = defaultdict(list)
    for adj, node in input:
        graph[node].append(adj)

    return graph


def subtree_count(graph, v):
    count = 1
    queue = graph.setdefault(v, [])
    for v in queue:
        count += child_count(graph, v)
    return count


def main():
    input = [map(int, line.strip().split()) for line in fileinput.input()]
    vertexes, edges = input[0]

    graph = build_graph(input[1:])

    print subtree_count(graph, 1)


if __name__ == '__main__':
    main()
