
def is_symmetrical(str):
    firstpart = str[:len(str)//2]
    secondpart = str[len(str)//2:]

    if(firstpart == secondpart):
        return "Yes, this string is symmetrical"
    else:
        return "No, this string isn't symmetrical"

def palindrome(str):
    rev = "".join(reversed(str))
    if(str == rev):
        return "The string is palindrome"
    else:
        return "The string isn't palindrome"

# driver code
str = "fsfs"
print(is_symmetrical(str))
print(palindrome(str))
