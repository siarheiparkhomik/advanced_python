import sys

sys.setrecursionlimit(10000)


def f(x):
    f(x)


if __name__ == "__main__":
    f(f)
