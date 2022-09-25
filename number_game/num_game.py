from sys import exit
import random

def input_begin():
    i = 3
    begin = 0
    while (i > 0):
        try:
            begin = int(input("Pleace enter the begin number:"))
            break
        except:
            i -= 1
            if (i > 1):
                print("You should enter a NUMBER\nYou have", i, "more tries")
            elif (i == 1):
                print("Your last try!")
            else:
                exit("I asked you to enter a number. Now it is the end of game. You've lost")
    return begin

def input_end():
    i = 3
    end = 0
    while (i > 0):
        try:
            end = int(input("Pleace enter the end number:"))
            break
        except:
            i -= 1
            if (i > 1):
                print("You should enter a NUMBER\nYou have", i, "more tries")
            elif (i == 1):
                print("Your last try!")
            else:
                exit("I asked you to enter a number. Now it is the end of game. You've lost")
    return end

def make_lst(begin, end):
    if (begin > end):
        buf = begin
        begin = end
        end = buf
    else:
        print("Thank you for a good choice =)")
    print("The choosen number range is", begin, "to", end)
    lst = []
    while (begin <= end):
        lst.append(begin)
        begin += 1
    return lst

def make_random_num(lst):
    random_num = random.choice(lst)
    print(random_num)
    return random_num

def input_res1():
    i = 3
    res1 = 0
    while (i > 0):
        try:
            res1 = int(input("Now, select one number in this range "))
            break
        except:
            i -= 1
            if (i > 1):
                print("You should enter a NUMBER\nYou have", i, "more tries")
            elif (i == 1):
                print("Your last try!")
            else:
                exit("I asked you to enter a number. Now it is the end of game. You've lost")
    return res1

def is_res1_in_lst(lst):
    i = len(lst) - 1
    mark = 0
    while (i >= 0):
        if (lst[i] == res1):
            print("Good first choice")
            mark = 1
            break
        i -= 1
    return mark

def is_res1_win(res1, random_num):
    if (res1 == random_num):
        exit("CONGRATULATIONS! YOU HAVE WON")

def input_and_check(lst, random_num):
    res1 = input_res1()
    is_res1_in_lst(lst)
    is_res1_win(res1, random_num)

def not_correct(random_num, lst):
    print ("I'm sorry, but rhis is not right answer. \nPleace. try again.\nYou should choose a number in range", lst[0], "-", end)
    i = 2
    while (i > 0):
        print("You have", i, "more tries")
        i -= 1
        input_and_check(lst, random_num)
        input_and_check(lst, random_num)
        exit("sorry, but You've lost")

# Driver Code
begin = input_begin()
end = input_end()
lst = make_lst(begin, end)
random_num = make_random_num(lst)
res1 = input_res1()
mark = is_res1_in_lst(lst)
print(mark)
if (mark == 1):
    is_res1_win(res1, random_num)
    not_correct(random_num, lst)
if (mark == 0):
    not_correct(random_num, lst)
