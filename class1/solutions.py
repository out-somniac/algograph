import tests
import union_find
import djikstra

if __name__ == "__main__":
    tests.runtests("graphs/", union_find.lowest)
    tests.runtests("graphs/", djikstra.lowest)
