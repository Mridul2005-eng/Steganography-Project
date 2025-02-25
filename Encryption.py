import cv2
import os
import string

img = cv2.imread("OIP.jpeg")

msg = input("Enter secret message:")
password = input("Enter a password:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

n = 0
m = 0
z = 0

img[n, m, z] = d[str(len(password))]

n = n + 1
m = m + 1
z = (z + 1) % 3

for i in range(len(password)):
    img[n, m, z] = d[password[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

for i in "end_of_message":
    img[n, m, z] = d[i]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
# os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows
