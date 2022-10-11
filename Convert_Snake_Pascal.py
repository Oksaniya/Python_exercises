def transform_str(str, n):
    i = 0
    new_str = ""
    while(i < len(str)):
        if(str[i] == n):
            new_str = new_str
        else:
            new_str = new_str + str[i]
        i += 1
    return new_str



# driver code
str = "geeksforgeeks_is_best"
n = '_'
new_str = transform_str(str, n)
print("Transformed str is: ", new_str)
