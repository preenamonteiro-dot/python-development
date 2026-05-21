# Caesar Cipher File Encryption and Decryption

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Read original file
with open("sample.txt", "r") as file:
    original_text = file.read()

print("Original Text:")
print(original_text)

# Encrypt text
shift = 3
encrypted_text = encrypt(original_text, shift)

# Save encrypted text
with open("encrypted.txt", "w") as file:
    file.write(encrypted_text)

print("\nEncrypted Text:")
print(encrypted_text)

# Decrypt text
decrypted_text = decrypt(encrypted_text, shift)

# Save decrypted text
with open("decrypted.txt", "w") as file:
    file.write(decrypted_text)

print("\nDecrypted Text:")
print(decrypted_text)

print("\nFiles created successfully!")