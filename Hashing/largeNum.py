#Using Python's Built-in hash() Function:
large_number = 10**9  # or any large number
hashed_value = hash(large_number)
print(hashed_value)

# Using hashlib for Cryptographic Hashing:
import hashlib
large_number = 10**9  # or any large number
# Convert the number to a byte representation
large_number_bytes = str(large_number).encode()
# Create a SHA256 hash of the large number
hashed_value = hashlib.sha256(large_number_bytes).hexdigest()
print(hashed_value)
