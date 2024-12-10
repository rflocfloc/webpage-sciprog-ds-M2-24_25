import time

def recCatalan(n):
    if n <= 1:
        return 1
    else:
        cat = 0
        for i in range(0, n):
            cat += recCatalan(i) * recCatalan(n - 1 - i)
        return cat

def dpCatalan(n):
    if n <= 1:
        return 1
    else:
        catNums = [1,1]
        for i in range(2,n+1):
            catNums.append(0)
            for j in range(0,i):
                catNums[i] += catNums[j] * catNums[i - j - 1]
        return catNums[-1]
    

catN = []
for i in range(0,15):
    catN.append(recCatalan(i))
    
print("First 15 catalan numbers:")
print(catN)

catN = []
start_t = time.time()
#for i in range(0,19):
#    catN.append(recCatalan(i))
catN = recCatalan(20)
end_t = time.time()
print("20th catalan number:")
print(catN)
print("It took {:.2f}s".format(end_t-start_t))


catN = []
start_t = time.time()
print("First 15 catalan numbers (dyn.p):")
for i in range(0,15):
    catN.append(dpCatalan(i))
print(catN)
end_t = time.time()
print("It took {:.2f}s".format(end_t-start_t))

catN = []
start_t = time.time()
for i in range(0,30):
    catN.append(dpCatalan(i))
end_t = time.time()
print("First 30 catalan numbers (dyn.p):")
print(catN)
print("It took {:.2f}s".format(end_t-start_t))