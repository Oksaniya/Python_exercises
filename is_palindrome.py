# Given a string, write a python function to check if it is palindrome or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.
def palindrome(str):
    rev = "".join(reversed(str))
    if(str == rev):
        return "The string is palindrome"
    else:
        return "The string isn't palindrome"
# driver code
str = "malayalam"
print(palindrome(str))