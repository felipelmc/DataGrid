def is_prior_to(date1, date2):
    for i in range(len(date1)):
         if date1[i]<date2[i]:
              return True
         else:
              i+=1
    return False

def is_posterior_to(date1, date2):
    for i in range(len(date1)):
         if date1[i]>date2[i]:
              return True
         else:
              i+=1
    return False

def is_equal_to(date1, date2):
    for i in range(len(date1)):
        if date1[i] != date2[i]:
            return False
        else:
            i+=1
    return True

def build_bad_char_table(pattern):
    table = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - i - 1
    return table

def boyer_moore(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    if pattern_length == 0:
        return False

    bad_char_table = build_bad_char_table(pattern)
    i = pattern_length - 1

    while i < text_length:
        j = pattern_length - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1

        if j == -1:
            return True

        bad_char_shift = bad_char_table.get(text[i], pattern_length)
        i += max(1, j - bad_char_shift)

    return False           