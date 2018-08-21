#uses python3

import sys
import threading

class missing_element:
    """finding the missing element of a linear array """

    def __init__(self):
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(sys.stdin.readline())
        self.array = list(map(int, sys.stdin.readline().split()))

    def element(self):

        for i in range(self.n):
            if i+1 != self.array[i]:
                break;
        return i+1


def main():

    missing = missing_element()

    test = int(sys.stdin.readline())
    cases = []
    for number in range(test):
        missing.read_input()
        cases.append(missing.element())

    for x in range(test):
        print (cases[x])

threading.Thread(target=main).start()
