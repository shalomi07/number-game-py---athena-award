"""how does this game work:
1. you will choose a random number between 1 and the maximum number you put in
2. input your maximum number
3. the computer will show a few sequences of numbers with this pattern:
   Un = a + 1 for a-1 times
   Un = Un-1 + (a + 1) for 1 time
   a for every sequence = a from previous sequence x 2
   1st: 1 3 5 7 9 11 13 ...
   2nd: 2 3 6 7 10 11 14 ...
   3rd: 4 5 6 7 12 13 14 15 20..."""

print("Welcome to the world's famous number game!")
print("I am ShalleyCodes, and I will read your mind for today!")
print("Think of any number between 1 and the maximum number you input.")
max = int(input("Please input the maximum number you for the sequence (more than 200, please!): "))
if max > 16384:
    print("The maximum number is too high, please rerun the program and input a number less than 16384.")
    exit()
num = 0

# starts with 1
s = " "
if max < 1:
    print("Please input a positive number. Rerun the program.")
    exit()
for d in range (1, max+1, 2):
    s += str(d) + " "
print(s)
ans1 = input("Is your number in the sequence? (Y/N): ")
if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
    num += 1

# starts with 2
s = " "
S = -1
if max >= S:
    for d in range(S, max+1):
        if S % 2 == 0:
            S += 1
        else :
            S += 3
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 4
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 4 == 0:
            S += 5
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 8
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 8 == 0:
            S += 9
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 16
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 16 == 0:
            S += 17
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 32
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 32 == 0:
            S += 33
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 64
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 64 == 0:
            S += 67
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 128
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 128 == 0:
            S += 129
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 256
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 256 == 0:
            S += 257
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 512
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 512 == 0:
            S += 513
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 1024
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 1024 == 0:
            S += 1025
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 2048
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 2048 == 0:
            S += 2049
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 4096
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 4096 == 0:
            S += 4097
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 8192
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 8192 == 0:
            S += 8193
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

# starts with 16384
s = " "
S = -1
if max >= S:
    for d in range (S, max+1):
        if d % 16384 == 0:
            S += 16387
        else:
            S += 1
        print(s + str(S))
        ans1 = input("Is your number in the sequence? (Y/N): ")
        if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
            num += 1

print("Your number is ", num)
print("All credits to ShalleyCodes 2025 - for Athena Award")