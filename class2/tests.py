#from ford_fulkerson import *
from edmonds_karp import *
from tabulate import tabulate
import os
import dimacs


def load_graphs(path):
    graphs = []
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        if os.path.isfile(file):
            size, edges = dimacs.loadDirectedWeightedGraph(file)
            solution = dimacs.readSolution(file)
            graphs.append((size, edges, solution))
    return graphs


def runtests(path, solver):
    graphs = load_graphs(path)
    table = []
    correct = 0
    for size, edges, solution in graphs:
        try:
            user_solution = EdmondsKarp(edges, size)
            table.append([size, len(edges), solution, user_solution])
            if int(solution) == user_solution:
                correct += 1

        except KeyboardInterrupt:
            print("Execution interupted by user")

    print(tabulate(table, ["Vertices", "Edges", "Correct Solution",
          "Your solution"], tablefmt="simple_outline"))
    print("Passed: {}/{}".format(correct, len(graphs)))


if __name__ == "__main__":
    runtests("/home/outsomniac/dev/algograph/graphs/lab2/flow/", EdmondsKarp)
