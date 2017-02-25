""" Finds all shortests paths of all nodes in a graph.

All-pairs shortest path of all nodes on a graph using the
Floyd-Warshall algorithm.
"""
import math

def floyd_warshall(graph, show_all=False):
    """Calculates all shortests paths between all points on a graph."""

    dist_matrix = []

    # The initial pass through the graph. Should only calculate distances from
    # two adjacent verticies and set the distance from a vertex to itself to be
    # 0.
    for pos, start_vert in enumerate(graph):
        dist_matrix.append([])
        for end_vert in graph:
            if start_vert == end_vert:
                dist_matrix[pos].append(0)
            else:
                # Handle the case where the verticies are adjecent.
                if end_vert in graph[start_vert]:
                    dist_matrix[pos].append(graph[start_vert][end_vert])
                # If the verticies aren't adjacent, then set the distance to
                # infinity.
                else:
                    dist_matrix[pos].append(math.inf)

    # Loop over all the verticies in the graph. The value assigned to `k` at
    # each pass corresponds to which nodes can be traversed through. At any
    # given pass, only nodes less than or equal to `k + 1` can be traversed
    # through.
    for k in range(len(graph)):
        for i, start_vert in enumerate(graph):
            for j, end_vert in enumerate(graph):
                # If the distance from the previous pass is larger than the
                # distance it takes to go from the current node to the newly
                # allowed node plus the distance from the newly allowed
                # vertex to the end vertex, then that means the passing through
                # the newly allowed vertex is a shorter path and the table
                # should be updated.
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]

        if show_all:
            print('--- k = {} ---'.format(k))
            print_table(dist_matrix)

    return dist_matrix


def print_table(matrix):
    """Prints out a simple table for a given matrix."""
    table = '\t'

    for i in range(len(matrix)):
        table += '{:7}'.format(i + 1)

    table += '\n'
    for i, row in enumerate(matrix):
        table += '{}\t|'.format(i + 1)
        for value in row:
            table += '{:6}|'.format(value)
        table += '\n'

    print(table)


if __name__ == '__main__':
    import argparse
    import importlib

    parser = argparse.ArgumentParser(description="Calculates all-pairs' "
                                               + "shortest paths.")

    parser.add_argument('file', metavar='file', type=str, 
                        help='file that contains the python dictionary '
                           + 'that represents the graph.')
    parser.add_argument('--all', help='show all iterations of distance matrix.',
                        action='store_true')


    args = parser.parse_args()
    graph = importlib.import_module(args.file.split('.')[0], package=None)

    if args.all:
        floyd_warshall(graph.graph, True)
    else:
        print_table(floyd_warshall(graph.graph))
