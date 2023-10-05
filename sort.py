def swap(arr, j: int, i: int):
    arr[i], arr[j] = arr[j], arr[i]

#RADIX SORT
def radix_sort(arr, n: int, n_digitos: int, n_range_digitos: int):
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
def heapify(arr, n: int, i: int):
    idx = i
    leftIdx = 2*i+1
    rightIdx = 2*i+2
    if ((leftIdx<n) and (int(arr[leftIdx]) > int(arr[idx]))):
        idx = leftIdx
    if ((rightIdx<n) and (int(arr[rightIdx]) > int(arr[idx]))):
        idx = rightIdx 
    if (idx != i):
        swap(arr, i, idx)
        heapify(arr, n, idx)       
    
def buildHeap(arr, n: int):
    for i in range(int(n/2)-1, 0, -1):
        heapify(arr, n, i)

def heapsort(arr, n:int):
    buildHeap(arr, n) 
    for i in range(n-1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)    