def radix_sort(arr: str, n: int, W: int, K: int):
    contagem = [0]*(K+1)
    print(contagem)
    aux = [0]*n
    for w in range(W-1, -1, -1):
        print(w)
        #Seta vetor de contagem com zeros
        for j in range(K+1):
            contagem[j] = 0

        #Atualizar vetor de contagens com ocorrencias de cada digito
        for i in range(n):
            contagem[int(arr[i][w])] += 1

        #Vetor acumulados
        for j in range(1, K+1):
            contagem[j] += contagem[j-1]        

        for i in range(n):
            j = int(arr[i][w])
            aux[contagem[j]] = arr[i]
            contagem[j]+=1
        for i in range(n):
            arr[i] = aux[i]
    return arr        