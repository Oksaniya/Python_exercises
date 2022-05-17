str = "12345"
i = 0
n = len(str)
while(i < n):
    if(str[i] == "0"):
        print("| ")
    elif(str[i] == "1"):
        print('|*')
    elif (str[i] == "2"):
        print('|**')
    elif (str[i] == "3"):
        print('|***')
    elif (str[i] == "4"):
        print('|****')
    elif (str[i] == "5"):
        print('|*****')
    elif (str[i] == "6"):
        print('|******')
    elif (str[i] == "7"):
        print('|*******')
    elif (str[i] == "8"):
        print('|********')
    elif (str[i] == "9"):
        print('|*********')
    i = i + 1
