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

class MergeSort(SortingAlgorithm):
    def __init__(self,data, verbose = True):
        self.data = data
        self.time = 0
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose
    
    def getTime(self):
        return(self.time)
    
    def __merge(self, first, last, mid):
        if self.verbose:
            print("Executing merge({},{},{})...".format(first,last,mid))
        tmp = []
        i = first
        j = mid + 1
        while i <= mid and j <= last:
            if self.data[i] < self.data[j]:
                tmp.append(self.data[i])
                i += 1
            else:
                tmp.append(self.data[j])
                j += 1
            self.comparisons += 1
        while i <= mid:
            tmp.append(self.data[i])
            i += 1
        self.data[first:first+len(tmp)] = tmp
            
    def __recursiveMergeSort(self, first, last):
        if self.verbose:
            print("Executing recursive merge sort({},{})...".format(first,last))

        self.operations += 1
        if first < last:
            mid = (first + last)//2 #<- index so mid+1 elements go in the first sublist!!! 
            self.__recursiveMergeSort(first, mid)
            self.__recursiveMergeSort(mid +1, last)
            self.__merge(first,last,mid)
        
    def sort(self):
        self.comparisons = 0
        self.operations = 0
        start = time.time()
        self.__recursiveMergeSort(0,len(self.data)-1)    
        end = time.time()
        self.time = end - start



if __name__ == "__main__":
    # this code is executed when SelectionSort is directly executed... 
    # https://docs.python.org/3/library/__main__.html
    d = [7, 5, 10, -11 ,3, -4, 99]
    mergeSorter = MergeSort(d, verbose = True)
    mergeSorter.sort()
    print(d)

    d = []
    for i in range(0,1000):
        d.append(random.randint(0,1000))
    mergeSorter = MergeSort(d, verbose = False)
    mergeSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(mergeSorter.getComparisons()))
    print("Number of swaps: {}".format(mergeSorter.getOperations()))
    print("In {:.4f}s".format(mergeSorter.getTime()))
    
    d = []
    for i in range(0,2000):
        d.append(random.randint(0,1000))
    mergeSorter = MergeSort(d, verbose = False)
    mergeSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(mergeSorter.getComparisons()))
    print("Number of recursions: {}".format(mergeSorter.getOperations()))
    print("In {:.4f}s".format(mergeSorter.getTime()))
    
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("\nSorting test passed? {}".format(test))
