def remove_character(str, n):
    n -= 1
    i = 0
    new_str = ""
    while(i < len(str)):
        if(i == n):
            new_str = new_str
        else:
            new_str = new_str + str[i]
        i += 1
    return new_str

# driver code
str = "GeeksForGeeks"
n = 4
new_str = remove_character(str, n)
print(new_str)