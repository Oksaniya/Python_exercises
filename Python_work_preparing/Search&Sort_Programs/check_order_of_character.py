# def check_str(str, pattern):
#     i = 0
#     res = False
#     while(i < len(str)):
#         e = 0
#         i2 = 0
#         counter = i
#         while(e < len(pattern)):
#             if(str[counter] == pattern[e]):
#                 counter += 1
#                 i2 += 1
#                 if(e == len(pattern)):
#                     res = True
#             e += 1
#         i += 1
#     return res

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

# def check_str(str, pattern):
#
#     for i in str:
#         counter = 0
#         for e in pattern:
#             if(e == i):
#                 print("i = ", i)
#                 print("e = ", e)
#                 counter += 1
#                 if (counter == len(pattern) - 1):
#                     print(counter)
#                     return True
#
#     return False


# driver code
str = "engineers rock"
pattern = 'eeer'
i = 0
res = check_str(str, pattern)

print(res)