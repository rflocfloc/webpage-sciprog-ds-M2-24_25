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

class InsertionSort(SortingAlgorithm):

    def sort(self):
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


if __name__ == "__main__":
    # this code is executed when SelectionSort is directly executed... 
    # https://docs.python.org/3/library/__main__.html
    d = [7, 5, 10, -11 ,3, -4, 99, 1]
    insSorter = InsertionSort(d, verbose = True)
    insSorter.sort()
    print(d)

    d = []
    for i in range(0,1000):
        d.append(random.randint(0,1000))
    insSorter = InsertionSort(d, verbose = False)
    insSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(insSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(insSorter.getOperations()))

    d = []
    for i in range(0,2000):
        d.append(random.randint(0,1000))
    insSorter = InsertionSort(d, verbose = False)
    insSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(insSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(insSorter.getOperations()))
    
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("\nSorting test passed? {}".format(test))
