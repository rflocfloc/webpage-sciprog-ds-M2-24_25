import random
import sys
import time

class SortingAlgorithm:
    def __init__(self, data, verbose = True):
        self.data = data
        self.comparisons = 0
        self.operations = 0
        self.time = 0 # novel addition!
        self.verbose = verbose
        
    def getData(self):
        return self.data
    
    def getOperations(self):
        return self.operations
    
    def getComparisons(self):
        return self.comparisons

    def getTime(self):
        return(self.time) # novel addition!

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
        start = time.time()
        self.comparisons = 0
        self.operations = 0

        for i in range(len(self.data) - 1):
                j = self.__argmin(i)
                self.__swap(i, j) 
                # keep track of what was done
                self.operations += 1

        end = time.time()
        self.time = end - start

class InsertionSort(SortingAlgorithm):

    def sort(self):
        start = time.time()
        self.comparisons = 0
        self.operations = 0

        for i in range(1, len(self.data)):
            temp = self.data[i]
            j = i
            while j > 0 and self.data[j-1] > temp:
                self.data[j] = self.data[j - 1]
                self.operations += 1
                self.comparisons += 1
                j = j - 1

            self.data[j] = temp
            self.operations += 1
            if j > 0:
                self.comparisons += 1
            if self.verbose:
                print("It. {}: {} comp: {} push+place:{}".format(i,
                                                           self.data,
                                                           self.comparisons,
                                                           self.operations
                                                          ))

        if self.verbose:
            print(self.data)
            print("\nNumber of comparisons: {}".format(self.comparisons))
            print("Number of push-ups+place: {}".format(self.operations))
        
        end = time.time()
        self.time = end - start


class MergeSort(SortingAlgorithm):
    def __init__(self,data, verbose = True):
        self.data = data
        self.time = 0
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose
    
    def __merge(self, first, last, mid):
        if self.verbose:
            print("Executing merge({},{},{})...".format(first,last,mid))
        tmp = []
        i = first
        j = mid + 1
        while i <= mid and j <= last:
            if self.data[i] < self.data[j]:
                self.comparisons += 1
                tmp.append(self.data[i])
                i += 1
            else:
                tmp.append(self.data[j])
                j += 1
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

class QuickSort(SortingAlgorithm):
    def __init__(self,data, verbose = True):
        self.data = data
        self.time = 0
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose

    def __swap(self, i,j):
        """swaps elements at positions i and j"""
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


#Need to extend the recursion limit for the test on reverse sorted
#array with 5000 elements
sys.setrecursionlimit(10000)
def getNrandom(n):
    res = []
    for i in range(n):
        res.append(random.randint(-10000,10000))
    return res

def testSorters(myList, verbose = False):
    #copy because the sorter will actually change the list!
    myList1 = myList[:]
    myList2 = myList[:]
    myList3 = myList[:]
    selSorter = SelectionSort(myList, verbose = False)
    insSorter = InsertionSort(myList1, verbose = False)
    mSorter = MergeSort(myList2, verbose = False)
    qSorter = QuickSort(myList3, verbose = False)
    if verbose:
        print("TestList:\n{}".format(myList))
        print("TestList1:\n{}".format(myList1))
        print("TestList2:\n{}".format(myList2))
        print("TestList3:\n{}".format(myList3))
    selSorter.sort()
    insSorter.sort()
    mSorter.sort()
    qSorter.sort()
    if verbose:
        print("Outputs:")
        print(myList)
        print(myList1)
        print(myList2)
        print(myList3)
    print("Test with {} elements".format(len(myList)))
    print("Insertion sort:")
    print("Number of comparisons: {}".format(insSorter.getComparisons()))
    print("Number of operations: {}".format(insSorter.getOperations()))
    print("In {:.4f}s".format(insSorter.getTime()))
    print("Selection sort:")
    print("Number of comparisons: {}".format(selSorter.getComparisons()))
    print("Number of operations: {}".format(selSorter.getOperations()))
    print("In {:.4f}s".format(selSorter.getTime()))
    print("Merge sort:")
    print("Number of comparisons: {}".format(mSorter.getComparisons()))
    print("Number of operations: {}".format(mSorter.getOperations()))
    print("In {:.4f}s".format(mSorter.getTime()))
    print("Quick sort:")
    print("Number of comparisons: {}".format(qSorter.getComparisons()))
    print("Number of operations: {}".format(qSorter.getOperations()))
    print("In {:.4f}s".format(qSorter.getTime()))

# script that finally executes the comparisons...
print("Test with a list of 10 elements...")
testList = getNrandom(10)
testSorters(testList, verbose = True) # just for testing that everything is OK...
print("#############")
print("Test with a list of 5000 elements...")
testList = list(range(5000))
testSorters(testList, verbose = False)
print("#############")
print("Test with a list of 5000 elements in reverse order...")
testList = list(range(5000))
testList.sort(reverse = True)
testSorters(testList, verbose = False)
print("#############")
print("Test with a list of 2000 elements, with last half in reverse order...")
a = list(range(1000))
b = list(range(1000,2000))
b.sort(reverse=True)
testSorters(a+b, verbose = False)
