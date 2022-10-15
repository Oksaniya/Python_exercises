def check_str(str, pattern):
    i = 0
    res = False
    while (i < len(str)):
        e = 0
        counter = i
        while (e < len(pattern)):
            if (str[counter] == pattern[e]):
                counter += 1
                e += 1
            else:
                break
        if (e == len(pattern)):
            res = True
            break
        i += 1
    return res
# driver code
str = "engineers rock"
pattern = 'eeer'
i = 0
res = check_str(str, pattern)

print(res)