def swap(arr, j: int, i: int):
    arr[i], arr[j] = arr[j], arr[i]

def custom_key(element):
    return element[1]

#RADIX SORT
def radix_sort(arr):
    #Getting n
    n = len(arr)

    #n digitos
    n_digitos = 0
    for _ in range(len(arr[0])):
        n_digitos+=1

    n_range_digitos = 10 #numeros variam de 0 a 9

    contagem = [0]*(n_range_digitos+1)
    aux = [0]*n
    for digit in range(n_digitos-1, -1, -1):

        #Seta vetor de contagem com zeros
        for digito in range(n_range_digitos+1):
            contagem[digito] = 0

        #Atualiza vetor de contagens com ocorrencias de cada digito
        for elemento in arr:
            contagem[int(elemento[digit])] += 1

        #Vetor acumulados
        for j in range(1, n_range_digitos+1):
            contagem[j] += contagem[j-1]        

        for elemento in arr:
            j = int(elemento[digit]) #0 a 9
            aux[contagem[j]-1]= elemento
            contagem[j]-=1  
    return aux   

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

#QUICKSORT
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

