import random

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

class SelectionSort(SortingAlgorithm):
    
    def __swap(self, i, j):
        """
        swaps elements i and j in data.
        """
        if(i != j): #no point in swapping if i==j
            if self.verbose:
                print("Swapping position {} with {}".format(i,j))
            self.operations += 1
            tmp = self.data[i]
            self.data[i] = self.data[j]
            self.data[j] = tmp
        
    def __argmin(self, i):
        """
        returns the index of the smallest element of
        self.__data[i:]
        """
        mpos = i
        N = len(self.data)
        minV = self.data[mpos]
        for j in range(i + 1, N):
            if self.data[j] < minV:
                mpos = j
                minV = self.data[j]
            # keep track of what was done
            self.comparisons += 1
        
        return mpos
    
    def sort(self):
        self.comparisons = 0
        self.operations = 0

        for i in range(len(self.data) - 1):
                j = self.__argmin(i)
                self.__swap(i, j) 


if __name__ == "__main__":
    # this code is executed when SelectionSort is directly executed... 
    # https://docs.python.org/3/library/__main__.html
    d = [7, 5, 10, -11 ,3, -4, 99, 1]
    selSorter = SelectionSort(d, verbose = True)
    selSorter.sort()
    print(d)
    d = []

    for i in range(0,1000):
        d.append(random.randint(0,1000))
    selSorter = SelectionSort(d, verbose = False)
    selSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(selSorter.getComparisons()))
    print("Number of swaps: {}".format(selSorter.getOperations()))
    
    d = []
    for i in range(0,2000):
        d.append(random.randint(0,1000))
    selSorter = SelectionSort(d, verbose = False)
    selSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(selSorter.getComparisons()))
    print("Number of swaps: {}".format(selSorter.getOperations()))
    
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("\nSorting test passed? {}".format(test))