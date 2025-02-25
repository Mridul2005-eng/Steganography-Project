import cv2
import os
import string

img = cv2.imread("encryptedImage.png")

message = ""
password = input("Enter password:")
secret_pass = ""

c = {}

for i in range(255):
    # d[chr(i)] = i
    c[i] = chr(i)

n = 0
m = 0
z = 0

pass_size = int(c[img[n, m , z]])

n = n + 1
m = m + 1
z = (z + 1) % 3

for i in range(pass_size):
    secret_pass += c[img[n, m, z]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

if secret_pass != password:
    print("Incorrect passcode!")
    exit()

i = pass_size + 1

while i < len(img) and i < len(img[0]) and img[n, m, z] != 255:
    # print(c[img[n, m, z]])
    message += c[img[n, m, z]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3
    i += 1
    if message[-14:] == "end_of_message":
        break

print("Decrypted message:", message[:-14])

