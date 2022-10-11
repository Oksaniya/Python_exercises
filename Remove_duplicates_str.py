def rem_dub(str):
    i = 0
    new_str = ""
    while(i < len(str)):
        if(check_char(new_str, str[i]) == False):
            new_str = new_str + str[i]
        else:
            new_str = new_str
        i += 1
    return new_str

def check_char(new_str, n):
    res = False
    i = 0
    while(i < len(new_str)):
        if(new_str[i] == n):
            res = True
        i += 1
    return res

# driver code
str = "geeksforgeeks"
new_str = rem_dub(str)
print(new_str)