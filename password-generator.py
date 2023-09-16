import random
import string

def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def savePassword(label, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{label} : {password}\n")

label = input("Masukkan label password Anda : ")
length = int(input("Masukkan panjang password Anda : "))

password = generatePassword(length)
savePassword(label, password)

print(f"Password untuk {label} telah disimpan di passwords.txt")
