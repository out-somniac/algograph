import os
import time


def loadWeightedGraph(name):
    V = 0
    L = []
    sol = None

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if(len(s) < 1):
            continue
        if(s[0] == "c"):
            sol = int(s[-1])
        elif(s[0] == "p"):
            V = int(s[2])
        elif(s[0] == "e"):
            (a, b, c) = (int(s[1]), int(s[2]), int(s[3]))
            (x, y, c) = (min(a, b), max(a, b), c)
            L.append((x, y, c))

    f.close()
    return (V, L, sol)


def test_file(file, solver):
    print("Testing: {}".format(file))
    size, edges, sol = loadWeightedGraph(file)
    print("Poprawna odpowiedź: {}".format(sol))
    time_start = time.time()
    user_solution = solver(size, edges)
    time_end = time.time()
    print("Twoja odpowiedź: {}".format(user_solution))
    print("W czasie: {:.2f}".format(time_end - time_start))
    print("=====================================")
    return user_solution == sol


def runtests(path_to_tests, solution):
    correct = 0
    total = 0
    for filename in os.listdir(path_to_tests):
        file = os.path.join(path_to_tests, filename)
        if os.path.isfile(file):
            total += 1
            if test_file(file, solution):
                correct += 1
    print("Zaliczonych {}/{}".format(correct, total))
