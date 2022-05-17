# Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return “True” if the given array A is monotonic else return “False” (without quotes).

a = [67, 69, 69, 90]
i = 0
res_inc = all(i <= j for i, j in zip(a, a[1:]))
res_decr = all(i >= j for i, j in zip(a, a[1:]))
if((res_inc == True) or (res_decr == True)):
    print("True")
else:
    print("False")
