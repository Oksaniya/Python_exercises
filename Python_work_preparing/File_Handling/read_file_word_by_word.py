f = open("example_file.txt", "r")

text = f.read()
result = text.split()
for i in result:
    print(i)