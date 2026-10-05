#NB P7 ceaser cipher


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift_base = 65
            else:
                shift_base = 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
text = input("Enter the text to encrypt/decrypt: ")
shift = int(input("Enter the shift value: "))
choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
if choice == "encrypt":
    print(caesar_cipher(text, shift))
elif choice == "decrypt":
    print(caesar_cipher(text, -shift))
else:
    print("Invalid choice.")