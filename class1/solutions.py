import tests
import union_find
import djikstra
import os

if __name__ == "__main__":
    tests.runtests("graphs/lab1",
                   union_find.lowest)
    tests.runtests("graphs/lab1",
                   djikstra.lowest)
