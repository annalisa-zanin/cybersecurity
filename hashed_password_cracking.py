import hashlib
import itertools

# Function to hash a password using SHA-256
def hash_password(password):
    """
    Hash a password using SHA-256.
    :param password: The password string to hash.
    :return: The hexadecimal representation of the hash.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
    # Convert the password to bytes using UTF-8 encoding, as hashing functions require binary input.
    # Apply the SHA-256 hashing algorithm to the byte sequence. => The output of **hashlib.sha256(<some-bytes>).digest()** would be something like: b'\x2c\xf2\x4d\xba\x5f\xb0\xa3\x0e\x26\' (the b in the front indicates a byte string).
    #(Note that the output without 'digest' would be a python hash object like <sha256 HASH object at 0x...>)
    # Use hexdigest() to convert the hash into a readable hexadecimal string for storage or comparison. =>=> The output would be something like:'2cf24dba5fb0a30e26e83b2ac5b9e2526ae56e650babd34e7fb712e3049d'. 

# Brute force cracking: Try all combinations of characters
def brute_force_crack(hash_to_crack, max_length):
    """
    Attempt to crack a password hash using brute force.
    :param hash_to_crack: The hash to crack.
    :param max_length: Maximum length of the password to try.
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    print("[*] Starting brute force attack...")
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt_password = ''.join(attempt)
            if hash_password(attempt_password) == hash_to_crack:
                print(f"[+] Password found: {attempt_password}")
                return
    print("[-] Password not found with brute force.")

# Dictionary-based attack: Use a predefined list of passwords
def dictionary_attack(hash_to_crack, dictionary_file):
    """
    Attempt to crack a password hash using a dictionary file.
    :param hash_to_crack: The hash to crack.
    :param dictionary_file: File containing potential passwords, one per line.
    """
    print("[*] Starting dictionary attack...")
    try:
        with open(dictionary_file, 'r') as file:
            for line in file:
                word = line.strip() #removes white spaces and characters like \n, \t, e \r.
                if hash_password(word) == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found in dictionary.")
    except FileNotFoundError:
        print(f"[-] Dictionary file {dictionary_file} not found.")

# Main function to demonstrate the attacks
def main():
    # Hash of the password we want to crack
    target_password = "secret"
    target_hash = hash_password(target_password)
    print(f"[!] Target hash: {target_hash}")

    # Brute force attack (max length of 4 characters)
    brute_force_crack(target_hash, max_length=6)

    # Dictionary attack (using a sample dictionary file)
    dictionary_attack(target_hash, dictionary_file='password_dictionary.txt')

if __name__ == "__main__":
    main()