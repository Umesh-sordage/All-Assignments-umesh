"""
write a code to generate identity matrix
"""
# print("identity matrix".center(40,"_"))
# import numpy as np
# # dimension =int(input("Enter the dimensions of identity matrix: "))
# identity_matrix=np.identity(5, dtype="int")
# print(identity_matrix)

print(40*"_")
print("identity matrix".center(40,"_"))
for i in range(0,5):
    for j in range (0, 5):
        if(i==j):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
print(40*"_")

print("armstrong numbers between 1 and 500".center(40,"_"))

# 2. generate armstrong numbers between 1 and 500
#    153 = 1 ** 3 + 5 ** 3 + 3 ** 3
#        = 1 + 125 + 27
#        = 153
lower=1
upper=500
for num in range(lower,upper + 1):
    sum=0
    temp = num
    while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //=10
      if num == sum:
         print(num)

# """
# 1. l1 = [1, 2, 3, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 4, 1, 2, 1]
#    discard all 1's in the list
# """
print("discard all 1's in the list".center(40,"_"))
l1=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4, 1, 2, 3 ]
l2=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4, 1, 2, 3 ]
while(True):
    try:
        l1.remove(1)
    except ValueError:
        break
print(l1)

print("discard the elements in the internal lists".center(40,"_"))
# """
# 2. l2 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
#    discard the elements in the internal lists
#
# """
p=[1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
p[4].clear()
p[7].clear()
print(p)

# problem
# -------
# months = ['dec', 'aug', 'oct', 'nov', 'sep', 'jan', 'apr', 'mar', 'jul', 'feb', 'jun', 'may']
# sort it by months in the calendar

# import datetime
# months_dict={}
# for i in range(1,13):
#     months_dict=['dec', 'aug', 'oct', 'nov', 'sep', 'jan', 'apr', 'mar', 'jul', 'feb', 'jun', 'may']
#     months_dict=months_dict.sort_values(by='datetime')
# print((months_dict))

"""

"""
# Python program to generate
# odd sized magic squares
# A function to generate odd
# sized magic squares
print("_"*40)
print(" code to generate magic matrix")
def generateSquare(n):

	# 2-D array with all
	# slots set to 0
	magicSquare = [[0 for x in range(n)]
				for y in range(n)]

	# initialize position of 1
	i = n // 2
	j = n - 1

	# Fill the magic square
	# by placing values
	num = 1
	while num <= (n * n):
		if i == -1 and j == n: # 3rd condition
			j = n - 2
			i = 0
		else:

			# next number goes out of
			# right side of square
			if j == n:
				j = 0

			# next number goes
			# out of upper side
			if i < 0:
				i = n - 1

		if magicSquare[int(i)][int(j)]: # 2nd condition
			j = j - 2
			i = i + 1
			continue
		else:
			magicSquare[int(i)][int(j)] = num
			num = num + 1

		j = j + 1
		i = i - 1 # 1st condition

	# Printing magic square
	print("Magic Square for n =", n)
	print("Sum of each row or column",
		n * (n * n + 1) // 2, "\n")

	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magicSquare[i][j]),
				end='')

			# To display output
			# in matrix form
			if j == n - 1:
				print()

# Driver Code


# Works only when n is odd
n = 3
generateSquare(n)

# This code is contributed
# by Harshit Agrawal
