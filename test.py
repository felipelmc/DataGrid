from datagrid import Event
import time
import random
from sort import radix_sort, heapsort, mergesort, quicksort

def calculateTime(startTime):
    total = time.time()-startTime
    print(f'The total time of this operation was: {total}')

def generateRandomNumberList(len, min_value, max_value):
    random_list = []
    for i in range(len):
        random_list.append(random.randint(min_value, max_value))
    return random_list    

def shouldOrderByRadixSortWithSuccess():
    startTime = time.time()
    
    #Arrange
    df = Event()
    df.owner_id = generateRandomNumberList(1000, 100, 999)
    to_assert = sorted(df.owner_id)
    final = [str(number) for number in to_assert]
    df.owner_id = [str(number) for number in df.owner_id]

    #Act
    sorted_list = radix_sort(df.owner_id)

    #Assert
    #assert final==sorted_list
    calculateTime(startTime)    

def shouldOrderByHeapSortWithSuccess():
    startTime = time.time()
    
    #Arrange
    df = Event()
    df.owner_id = generateRandomNumberList(1000, 0, 999)

    #Act
    sorted_list = heapsort(df.owner_id)

    #Assert
    assert sorted(df.owner_id)==sorted_list
    calculateTime(startTime)        

def shouldOrderByMergeSortWithSuccess():
    startTime = time.time()
    
    #Arrange
    df = Event()
    df.owner_id = generateRandomNumberList(1000, 0, 999)

    #Act
    sorted_list = mergesort(df.owner_id)

    #Assert
    assert sorted(df.owner_id)==sorted_list
    calculateTime(startTime)     

def shouldOrderByQuickSortWithSuccess():
    startTime = time.time()
    
    #Arrange
    df = Event()
    df.owner_id = generateRandomNumberList(1000, 0, 999)

    #Act
    sorted_list = quicksort(df.owner_id)

    #Assert
    assert sorted(df.owner_id)==sorted_list
    calculateTime(startTime)      

#Running tests
# shouldOrderByRadixSortWithSuccess()
# shouldOrderByHeapSortWithSuccess()
# shouldOrderByMergeSortWithSuccess()
# shouldOrderByQuickSortWithSuccess()