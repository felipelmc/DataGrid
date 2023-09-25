from datagrid import Event
import time
from sort import radix_sort, heapsort

def calculateTime(startTime):
    total = time.time()-startTime
    print(f'The total time of this operation was: {total}')

#def shouldReadCSVwithSuccess(file):
#    startTime = time.time()
#    df = Event()
#    df.read_csv(file)
#    calculateTime(startTime)

def shouldOrderByRadixSortWithSuccess():
    startTime = time.time()
    
    #Arrange
    df = Event()
    df.owner_id = ['12045', '18492', '09471', '83713', '17387']
    n = len(df.owner_id)
    k = 10 #0 to 9
    w = 5

    #Act
    sorted = radix_sort(df.owner_id, n, w, k)

    #Assert
    print(sorted)
    print(calculateTime(startTime))    

def shouldOrderByHeapSortWithSuccess():
    startTime = time.time()
    
    #Arrange
    df = Event()
    df.owner_id = ['12045', '18492', '09471', '83713', '17387']
    n = len(df.owner_id)

    #Act
    heapsort(df.owner_id, n)

    #Assert
    print(df.owner_id)
    print(calculateTime(startTime))        


#Running tests
#shouldOrderByRadixSortWithSuccess()
shouldOrderByHeapSortWithSuccess()