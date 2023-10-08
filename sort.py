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
