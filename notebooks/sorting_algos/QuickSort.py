import random
import time

class SortingAlgorithm:
    def __init__(self, data, verbose = True):
        self.data = data
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose
        
    def getData(self):
        return self.data
    
    def getOperations(self):
        return self.operations
    
    def getComparisons(self):
        return self.comparisons

    def sort(self):
        raise NotImplementedError

class QuickSort(SortingAlgorithm):
    def __init__(self,data, verbose = True):
        self.data = data
        self.time = 0
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose

    def getTime(self):
        return(self.time)

    def __swap(self, i,j):
        """swaps elements at positions i and j"""
        if(i != j): # no point in swapping if i==j
            self.operations += 1
            tmp = self.data[i]
            self.data[i] = self.data[j]
            self.data[j] = tmp

    def __pivot(self, start, end):
        """gets the pivot and swaps elements in [start, end]
        accordingly"""
        p = self.data[start]
        j = start

        for i in range(start + 1, end + 1):
            self.comparisons += 1
            if self.data[i] < p:
                j = j + 1
                self.__swap(i, j)

        self.__swap(start,j)

        return j

    def __recQuickSort(self, start, end):
        """gets the pivot and recursively applies
        itself on the left and right sublists
        """
        if start < end:
            #GET THE PIVOT
            j = self.__pivot(start, end)

            self.__recQuickSort(start, j - 1)

            self.__recQuickSort(j + 1, end)

    def sort(self):
        self.comparisons = 0
        self.operations = 0
        start = time.time()
        self.__recQuickSort(0, len(self.data) - 1)
        end = time.time()
        self.time = end - start


if __name__ == "__main__":
    # this code is executed when SelectionSort is directly executed... 
    # https://docs.python.org/3/library/__main__.html
    d = [7, 3, 10, -11 ,5, -4, 99, 1]
    qkSorter = QuickSort(d, verbose = True)
    qkSorter.sort()
    d = []

    for i in range(0,1000):
        d.append(random.randint(0,1000))
    qkSorter = QuickSort(d, verbose = False)
    qkSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(qkSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(qkSorter.getOperations()))
    print("In {:.4f}s".format(qkSorter.getTime()))

    d = []
    for i in range(0,10000):
        d.append(random.randint(0,1000))
    qkSorter = QuickSort(d, verbose = False)
    qkSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(qkSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(qkSorter.getOperations()))
    print("In {:.4f}s".format(qkSorter.getTime()))
    test = True

    d = []
    for i in range(0,300000):
        d.append(random.randint(0,1000))
    qkSorter = QuickSort(d, verbose = False)
    qkSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(qkSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(qkSorter.getOperations()))
    print("In {:.4f}s".format(qkSorter.getTime()))
    test = True

    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("\nSorting test passed? {}".format(test))