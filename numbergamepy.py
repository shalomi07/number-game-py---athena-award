print("How to play the number game:")
print("Think about any number. This game will guess your number CORRECTLY (trust me!)")
print("The computer will give you a sequence of numbers, and you have to answer whether your number is in that sequence or not.")
print(" ")

hasil = 0

Z = int(input("Input maximum number in the sequence: "))
z = " "
for x in range (1, Z+1, 2):
    z += str(x)+' '
print(z)
jawab1 = input("Is your number in this sequence? (Y/N) ")

if jawab1 == 'y' or jawab1 == "Y":
    hasil += 1

#1

z = " "
y = -1
for x in range (y, Z+1):
    if x % 2 == 1:
        y = y + 3
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
""" cara kerja:
x = -1 (nilai y), jadi masuk kategori ganjil, y = -1 + 3 = 2
x = 0, jadi masuk kategori genap, y = 2 + 1 = 3
x = 1, jadi masuk kategori ganjil, y = 3 + 3 = 6 dst
barisan = 2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31
"""
jawab2 = input("Is your number in this sequence? (Y/N) ")
if jawab2 == 'y' or jawab2 == "Y":
    hasil += 2
#2

""" rumus untuk deret berikutnya
angka pertama = angka pertama dari deret sebelumnya x 2
pola utk selisihnya: +1 sebanyak (angka pertama deret -1) lalu tambahkan dgn (angka pertama deret + 1)"""
z = " "
y = -1
for x in range (0, Z+1):
    # 4 (+1) 5 (+1) 6 (+1) 7 (+3) 10
    # x = 1, 2, 3, 5, 6, 7,
    if x % 4 == 0:
        y = y + 5
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab3 = input("Is your number in this sequence? (Y/N) ")
if jawab3 == 'y' or jawab3 == "Y":
    hasil += 4
#4

z = " "
y = -1
for x in range (0, Z+1):
    # +1 7x lalu +9
    if x % 8 == 0:
        y = y + 9
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab4 = input("Is your number in this sequence? (Y/N) ")
if jawab4 == 'y' or jawab4 == "Y":
    hasil += 8
#8

z = " "
y = -1
for x in range (0, Z+1):
    if x % 16 == 0: #ganti saja jadi if x % sampai 512 (kali" 2 terus)
        y = y + 17
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab5 = input("Is your number in this sequence? (Y/N) ")
if jawab5 == 'y' or jawab5 == "Y":
    hasil += 16

z = " "
y = -1
for x in range (0, Z+1):
    if x % 32 == 0:
        y = y + 33
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab6 = input("Is your number in this sequence? (Y/N) ")
if jawab6 == 'y' or jawab6 == "Y":
    hasil += 32

z = " "
y = -1
for x in range (0, Z+1):
    if x % 64 == 0:
        y = y + 65
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab7 = input("Is your number in this sequence? (Y/N) ")
if jawab7 == 'y' or jawab7 == "Y":
    hasil += 64

z = " "
y = -1
for x in range (0, Z+1):
    if x % 128 == 0:
        y = y + 129
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab8 = input("Is your number in this sequence? (Y/N) ")
if jawab8 == 'y' or jawab8 == "Y":
    hasil += 128

z = " "
y = -1
for x in range (0, Z+1):
    if x % 256 == 0:
        y = y + 257
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab9 = input("Is your number in this sequence? (Y/N) ")
if jawab9 == 'y' or jawab9 == "Y":
    hasil += 256

z = " "
y = -1
for x in range (0, Z+1):
    if x % 512 == 0:
        y = y + 513
    else:
        y = y + 1
    if y > Z:
        break
    z += str(y) + ' '
print(z)
jawab10 = input("Is your number in this sequence? (Y/N) ")
if jawab10 == 'y' or jawab10 == "Y":
    hasil += 512


print("Your number is", hasil)
print("Told ya I can guess your number correctly!")
# please ignore the language used in naming variables and comments, I used Indonesian language to make it easier for me :)