"""
a.

1
23
456
7890
"""
# n=int(input("enter the number of rows:"))
num = 1

for row in range(5):  # (1,6)
    for col in range(1, row + 1):  # (1,row)
        print(num, end='')
        num = num + 1

    print()
print("_" * 40)

"""
    b.

    1
    22
    333
    4444
    55555

"""
for row in range(6):
    for col in range(row):
        print(row, end="")
    print("")

print("_" * 40)

"""
c.
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""
a = int(input("Enter a value: "))  # a=5

for row in range(1, a + 1):  # 1,2,3,4,5
    print(" " * (a - row), end="")  # 5-2=3
    for col in range(1, row + 1):  # 1,3-1,2
        print(col, end=" ")
    print()

for row in range((a - 1), 0, -1):
    print(" " * (a - row), end="")
    for col in range(1, row + 1):
        print(row, end=" ")
    print()

print("_" * 40)
"""
Pascal triangle
"""
print("Pascal triangle")
# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # for new line
    print()

print("_" * 40)
print("Identity Matrix")
n = int(input("Enter a number: "))
for i in range(0, n):
    for j in range(0, n):
        if (i == j):
            print("1", sep=" ", end=" ")
        else:
            print("0", sep=" ", end=" ")
    print()

print("_" * 40)

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print("_" * 40)

"""
write a code to genrate fibonacci series
"""
num = int(input("Enter the number of terms"))
num1, num2, = 0,1
count=0
if num == 1:
    print(num1)
else:
    print("fibonacci series")
    while count < num:
        print(num1)
        sum= num1 + num2
        num1 = num2
        num2 = sum
        count += 1

"""
5. (greedy ? )
	farmer -> 3 daughters -> each daughter had a son
        farmer had  mangoes in a room
        farmer promisses his daughters that he is going distribute mangoes to them equally in the evening after his shopping.
        In the absence of the father 1st daughter enters the room without the knowledge of her siblings
	She makes three divisions of the available mangoes in the room and 1 mango was extra she gives that to her child, takes 1 division(heap) and mixes other two divsions and leaves the room.
	Now 2nd daughter same idea and same execution
	Now 2rd daughter same idea and same execution
       Finally the father enters the room and finds some mangoes and distributes it as he promised.

  how many mangoes were there in the room? num1,num2,num3

Generate 5 such numbers

"""



cntr = 0
j = 1
while cntr < 6:
    num = j
    flag = False
    lst = []
    for i in range(3):
        if (num - 1) % 3 == 0:
            res = (num - 1) // 3 + 1
            lst.append(res)
            num = num - res
            if i == 2:
                flag = True
        else:
            break
    if flag and num and num % 3 == 0:
        print("Total {} -->  remaining {} --> father distributes {} to each daughter".format(j, num, num//3))
        print("\t\tDaughter #1 --> {}\n\t\tDaughter #2 -->{}\n\t\tDaughter #3 --> {}".format(lst[0], lst[1], lst[2]))
        cntr += 1
    j += 1