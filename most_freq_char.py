def char_search(str):
    i = 0
    char_lst = []
    while(i < len(str)):
        if(ident_check(char_lst, str[i]) == True) and (str[i] != ' '):
            char_lst.append(str[i])
        i += 1
    return char_lst

def ident_check(char_lst, n):
    i = 0
    while(i < len(char_lst)):
        if(char_lst[i] == n):
            return False
        i += 1
    return True

def freq_count(str, ch):
    i = 0
    ith = 0
    while(i < len(str)):
        if(str[i] == ch):
            ith += 1
        i += 1
    return ith

def biggest_ither(freq_lst):
    i = 0
    res = 0
    buf = freq_lst[0]
    while(i < len(freq_lst)):
        if(freq_lst[i] > buf):
            buf = freq_lst[i]
            res = i
        i += 1
    return res




# driver code
str = "GeeksforGGGGGGeeks                              "
print("The original string is : ", str)
char_lst = char_search(str)
print(char_lst)
i = 0
freq_lst = []
while(i < len(char_lst)):
    freq_lst.append(freq_count(str, char_lst[i]))
    i += 1
print(freq_lst)
res_iter = biggest_ither(freq_lst)
print(res_iter)
print(char_lst[res_iter])
