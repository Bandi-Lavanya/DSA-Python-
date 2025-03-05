def main():
    n = int(input("Enter the size of the array: "))
    print(f"Enter {n} space-separated numbers: ")
    arr = list(map(int, input().split()))

    # Precompute the frequency of numbers in the array
    hash_map = [0] * 13  # Assuming numbers are in the range 0 to 12
    for num in arr:
        hash_map[num] += 1
    q = int(input("Enter the number of queries: "))
    for _ in range(q):
        number = int(input("Enter the number to check its frequency: "))
        print(f"Frequency of {number}: {hash_map[number]}")

if __name__ == "__main__":
    main()
