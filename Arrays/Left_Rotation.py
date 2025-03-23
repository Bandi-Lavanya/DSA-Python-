#Brute Force-->TC: O(N)
arr=list(map(int,input("Enter array elements:").split()))
def solve(arr):
    n=len(arr)
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
    print()
solve(arr)
#Optimal Approach-->Tc: O(N)

def solve2(arr):
    n=len(arr)
    temp = arr[0]  # storing the first element of the array in a variable
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  # assign the value of the variable at the last index
    for i in range(n):
        print(arr[i], end=" ")
solve(arr)
'''O/P:
Enter array elements:1 2 3 4 5
2 3 4 5 1 '''


