def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

filename = input("Enter file name: ")
shift = int(input("Enter shift: "))
mode = input("Encrypt(e) or Decrypt(d): ")

try:
    with open(filename, "r") as f:
        content = f.read()

    if mode == "e":
        result = encrypt(content, shift)
        newfile = "encrypted_" + filename
    else:
        result = decrypt(content, shift)
        newfile = "decrypted_" + filename

    with open(newfile, "w") as f:
        f.write(result)

    print("Done! Saved as", newfile)
except:
    print("Error occurred!")
