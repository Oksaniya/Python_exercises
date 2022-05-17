#(P x T x R)/100 - This is a formula

from imaplib import Int2AP


P = input("enter P: ")
T = input("enter T: ")
R = input("enter R: ")

res = (float(P) * float(T) * float(R))/100
print("Result = ", format(res))