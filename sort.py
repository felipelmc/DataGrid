def swap(arr, j: int, i: int):
    arr[i], arr[j] = arr[j], arr[i]

def custom_key(element):
    return element[1]

def radix_sort_strings(strings, max_len):   
    strings = [s.ljust(max_len) for s in strings]

    for i in range(max_len - 1, -1, -1):
        count = [0] * 256

        for s in strings:
            char = ord(s[i])
            count[char] += 1

        for j in range(1, 256):
            count[j] += count[j - 1]

        output = [''] * len(strings)
        for s in reversed(strings):
            char = ord(s[i])
            output[count[char] - 1] = s
            count[char] -= 1

        strings = output

    sorted_strings = [s.rstrip() for s in strings]
    return sorted_strings

#MERGESORT
def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result        

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergesort(left_half)
    right_half = mergesort(right_half)

    return merge(left_half, right_half)

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    
    left = []
    middle = []
    right = []
    
    if type(pivot) == tuple:
        for x in arr:
            if x[1] < pivot[1]:
                left.append(x)
            elif x[1] == pivot[1]:
                middle.append(x)
            elif x[1] > pivot[1]:
                right.append(x)
    else:
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

    return quicksort(left) + middle + quicksort(right)

#HEAPSORT
def heapify(arr, n: int, i: int, key=lambda x: x):
    idx = i
    leftIdx = 2 * i + 1
    rightIdx = 2 * i + 2

    if leftIdx < n and key(arr[leftIdx]) > key(arr[idx]):
        idx = leftIdx
    if rightIdx < n and key(arr[rightIdx]) > key(arr[idx]):
        idx = rightIdx

    if idx != i:
        swap(arr, i, idx)
        heapify(arr, n, idx, key)

def buildHeap(arr, n: int, key=lambda x: x):
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i, key)


def heapsort(arr):
    n = len(arr)
    buildHeap(arr, n, key=custom_key) 
    for i in range(n-1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0, key=custom_key)  
    return arr      
