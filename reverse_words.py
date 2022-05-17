# Reverse words in a given String in Python
def rev(str):
    words = str.split()
    str = ' '.join(reversed(words))
    return str
# Driver part
str = "Mama myla ramu"
print(rev(str))