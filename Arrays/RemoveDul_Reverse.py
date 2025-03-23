'''Enter array elements:1 2 3 4 5
Enter k value:2
After rotating k elements to the right: [4, 5, 1, 2, 3]
Enter array elements:1 2 3 4 5
Enter k value:2
After rotating k elements to the left: [3, 4, 5, 1, 2]'''

# Function to reverse the array from start to end
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap elements
        start += 1
        end -= 1

# Function to rotate k elements to the right
def rotate_right(arr, k):
    n = len(arr)  # Get the length of the array
    k = k % n  # Handle cases where k > n 

    # Reverse the entire array
    reverse(arr, 0, n - 1)
    # Reverse the first k elements
    reverse(arr, 0, k - 1)
    # Reverse the remaining n-k elements
    reverse(arr, k, n - 1)

# Example usage
arr=list(map(int,input("Enter array elements:").split()))
k = int(input("Enter k value:"))
rotate_right(arr, k)
print("After rotating k elements to the right:", arr)

# Function to reverse the array from start to end
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Function to rotate k elements to the left
def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n

    # Reverse first k elements
    reverse(arr, 0, k - 1)
    # Reverse remaining n-k elements
    reverse(arr, k, n - 1)
    # Reverse the whole array
    reverse(arr, 0, n - 1)

# Example usage
arr=list(map(int,input("Enter array elements:").split()))
k = int(input("Enter k value:"))
rotate_left(arr, k)
print("After rotating k elements to the left:", arr)

