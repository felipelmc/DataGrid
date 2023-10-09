import random

def is_prior_to(date1, date2): 
    for i in range(19):
        if date1[i]<date2[i]:
            return True
        elif date1[i]==date2[i]:
            i+=1
        else:
            return False    

def is_posterior_to(date1, date2):
    for i in range(19):
        if date1[i]>date2[i]:
            return True
        elif date1[i]==date2[i]:
            i+=1
        else:
            return False     

def is_substring(text, pattern, len_pattern):
    matches = 0
    for i in range(len(text)):
        if text[i] == pattern[matches]:
            matches += 1
        else:
            matches = 0
            
        if matches == len_pattern: 
           return True
    return False

def generateRandomNumberList(len, min_value, max_value):
    random_list = []
    for i in range(len):
        random_list.append(random.randint(min_value, max_value))
    return random_list    

def swap(arr, j: int, i: int):
    arr[i], arr[j] = arr[j], arr[i]

def custom_key(element):
    return element[1]   
