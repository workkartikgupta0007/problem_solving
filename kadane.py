#finding the max sum of contigous array
import sys
import threading

class elements:
    """
    Kadane algo for finding the max sum of contiguous array elements
    finding out the maxelement each time and  overall max value
    max_ending_here = max_ending_here +a[i]
    if(max_ending_here < 0 )
        max_ending_here = 0

    """
    def __init__(self):
        """
        n >> size of array
        array >> elements to be entered
        max_here >> max at each interval
        max_overall >> max value of the contigous array
        """
        self.n = 0
        self.array = []
        self.max_here = 0
        self.max_overall = 0


    def get_input(self):
        print( "Enter the size of array : ")
        self.n = int(sys.stdin.readline())
        print("Enter the array elements : ")
        self.array = self.parent = list(map(int, sys.stdin.readline().split()))


    def find_max(self):
        for i in range(self.n):
            self.max_here = self.max_here + self.array[i]
            if(self.max_here < 0):
                self.max_here = 0
            if(self.max_overall < self.max_here):
                self.max_overall = self.max_here

        return self.max_overall


def main():
    element = elements()
    element.get_input()
    print(element.find_max())

threading.Thread(target=main).start()
