from sort import quicksort
from utils import swap
import random

####### QUICKSELECT ####### 
def partition(arr, p, r):
    """
    Partition algorithm for quickselect with a random pivot
    """
    # Choose a random pivot index within the range [p, r]
    pivot_index = random.randint(p, r)

    # Swap the pivot element with the last element in the subarray
    swap(arr, pivot_index, r)

    pivot = arr[r][1]
    i = p - 1
    for j in range(p, r):
        if arr[j][1] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, r)
    return i + 1

def quickselect(arr, x):
    """
    Quickselect algorithm
    """
    p = 0
    r = len(arr) - 1
    while p < r:
        q = partition(arr, p, r)
        if q == x:
            return arr[q]
        elif q < x:
            p = q + 1
        else:
            r = q - 1
    return arr[p] 

####### MEDIAN OF MEDIANS ####### 
def selectMOM(arr, k):
    """
    Median of Medians algorithm
    """
    if len(arr) == 1:
        return arr[0]
    
    # Divide the input into groups of 5
    groups_of_five = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Calculate the median of each group of 5 using quicksort
    medians = [quicksort(group)[len(group) // 2] for group in groups_of_five]

    # Find the median of medians
    pivot = selectMOM(medians, len(medians) // 2)

    left = []
    middle = []
    right = []

    for x in arr:
        if x[1] < pivot[1]:
            left.append(x)
        elif x[1] == pivot[1]:
            middle.append(x)
        else:
            right.append(x)

    if k < len(left):
        return selectMOM(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return selectMOM(right, k - len(left) - len(middle))