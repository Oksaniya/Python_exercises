dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(dict)

del dict["Mani"]
print("Deleted Mini: ", dict)

removed_val = dict.pop('Arushi')
print("The dictionary after remove Arushi is : " + str(dict))
print("The removed key's value is : " + str(removed_val))

