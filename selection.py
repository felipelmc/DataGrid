from sort import swap

def partition(arr, p, r):
    pivot = arr[r][1]
    i = p - 1
    for j in range(p, r):
        if arr[j][1] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, r)
    return i + 1

# define quickselect inputing just arr and x
def quickselect(arr, x):
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