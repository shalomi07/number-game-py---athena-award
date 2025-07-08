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
num = 0

# starts with 1
s = " "
for d in range (1, max+1, 2):
    s += str(d) + " "
print(s)
ans1 = input("Is your number in the sequence? (Y/N): ")
if ans1 == 'y' or ans1 == 'Yes' or ans1 == 'YES' or ans1 == 'Y':
    num += 1

# starts with 2
s = " "
S = -1
for d in range(S, max+1):
    if S % 2 == 0:
        S += 1
    else :
        S += 3
    print(s + str(S))

print("Your number is ", num)
print("All credits to ShalleyCodes 2025 - for Athena Award")