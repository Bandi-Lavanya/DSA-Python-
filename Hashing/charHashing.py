def main():
    n = int(input("Enter the size of the array: "))
    print(f"Enter {n} space-separated lowercase characters: ")
    arr = list(input().split())  
    # Precompute the frequency of characters using ASCII values
    hash_map = [0] * 26  # Assuming only lowercase letters 'a' to 'z'
    for char in arr:
        index = ord(char) - ord('a')  # Convert character to index
        hash_map[index] += 1
    q = int(input("Enter the number of queries: "))
    for _ in range(q):
        char = input("Enter the character to check its frequency: ")
        index = ord(char) - ord('a')
        print(f"Frequency of '{char}': {hash_map[index]}")

if __name__ == "__main__":
    main()
