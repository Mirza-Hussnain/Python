def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decode_caesar_cipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)

# Main program
message = "Hello, World!"
shift_amount = 3

# Encode the message
encoded_message = caesar_cipher(message, shift_amount)
print("Encoded:", encoded_message)

# Decode the message
decoded_message = decode_caesar_cipher(encoded_message, shift_amount)
print("Decoded:", decoded_message)
