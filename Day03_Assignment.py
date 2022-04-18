"""
1.Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
print(f"question number 1")
# By using update method
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4=dic1.copy()
dic4.update(dic2)
dic4.update(dic3)
print(f"by using update method dic4:-{dic4}")

#by using unpacking operator
dic5={**dic1, **dic2, **dic3}
print(f"by using unpacking operator dic5:-{dic5}")

print("_"*40)
print(f"question number 2")
"""
2.Write a Python script to check whether a given key already exists in a dictionary
"""

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_exits(dictionary):
    if dictionary in d :
        print("key is already exits in the dictionary ")
    else:
        print("key is NOT exits in the dictionary ")
is_key_exits(5)
is_key_exits(9)

print("_"*40)
print(f"question number 3")

"""
3.Write a Python program to iterate over dictionaries using for loops.
dictionaries are the combination of key and values 
"""
dictionary={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for key,value in dictionary.items():
    print(key,value)


print("_"*40)
print(f"question number 4")


"""
4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
dictionaries={1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
n=5
for i in range(1,n+1):
    dictionaries[i]=i*i
print(f"dictionary that contains a number in the form of (x,x*x):{dictionaries}")

print("_"*40)
print(f"question number 5")
"""
5.Write a Python program to remove duplicates (values) from Dictionary
duplicate values and keys also get removed if they are same
"""
dictionary5={1: 10, 2: 20, 3: 30, 4: 50, 5: 50, 6: 60, 3: 30}
temp=[]
res=dict()
for key, value in dictionary5.items():
    if value not in temp:
       # temp.append(key) {1: 10, 2: 20, 3: 30, 4: 50, 5: 50, 6: 60}
        temp.append(value)  # {1: 10, 2: 20, 3: 30, 4: 50, 6: 60}
        res[key]=value
print(res)

print("_"*40)
print(f"question number 6")
"""
6. Write a code to get the key of a minimum value from a dictionary
here two values are same but we first occurance value if we want to remove duplicate value or key then
use for loop as used in 5th questions with append method
"""
dictionary6={1: 120, 2: 20, 3: 330, 4: 550, 5: 50, 6: 660, 3: 20}
key_value1 = min(dictionary6, key=dictionary6.get)
key_value2 = max(dictionary6, key=dictionary6.get)
print(f"minimum key_value is:{key_value1}")
print(f"maximum key_value is:{key_value2}")

print("_"*40)
print(f"question number 7")
"""
7. Reverse a list in Python
we have methods to reverse like list_A.reverse(), systems.reverse()
by using slicing operator res=systems[::-1]
"""
list_A =[1, 2, 3, 4, 5, 6]
#list_A.reverse()

print(f"reversed list by using for loop:")
for i7 in reversed(list_A):
    print(i7)

print("_"*40)
print(f"question number 8")
"""
8. Remove all occurrences of a specific item from a list.
"""
item=[0,9,1,2,3,1,3,2,4,5,1,2]
occurance=1
print("Removed all occurrences of a specific item from a list")
for i8 in item:
    if i8!=occurance:
        print(i8)




print("_"*40)
print(f"question number 9")

"""
9. Write a Python program to sum all the items in a list
"""
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i9 in num:
    sum=sum+i9
print(sum)


print("_"*40)
print(f"question number 10")

"""
10. Write a Python program to get the second largest number from a list
here i taken one list then by using set method we removed duplicated backend data structure is hashtable so we sorted list
and i just taken index from last
"""
list10=[1,2,4,5,6,3,5]
res10=list(set(list10))

print(f"second largest number from a list:{res10[-2]}")
print("_"*40)
print(f"question number 11")

"""
11. Write a Python program to find the second smallest number in a list
"""
list11=[1,4,2,5,6,3,5]
res11=list(set(list11))

print(f"second smallest number in a list:{res11[1]}")

print("_"*40)
print(f"question number 12")
"""
12. Write a Python program to get unique values from a list
set in which duplicates are not allowed so here i used set
"""
unique = [1, 2, 3, 1, 2, 4, 5, 1, 4, 6]
unique = list(set(unique))
print(unique)

print("_"*40)
print(f"question number 13")
"""
13. Write a Python program to get count of repetition of each value from a list.
"""
t = [1, 2, 3, 1, 2, 1, 2, 1, 1, 3, 4, 2, 1, 2, 3, 1, 2, 5]
print(f"t :{t}")
print(type(t))
count={}
print(type(count))
for i in t:
    count[i]=t.count(i)
print(f"count of each occcurance is :{count}")
print(f"count of 1 is :{t.count(1)}")
print(f"count of 2 is :{t.count(2)}")
print(f"count of 3 is :{t.count(3)}")

print("_"*40)
print(f"question number 14")
"""
14. Write a Python program to find common items from two lists.
"""

A ={1, 2, 3, 4, 5, 6}
B ={7, 2, 8, 9, 10, 6}
print(type(A))
print("common items from two lists A & B are :", A & B)
print(A.intersection(B))


print("_"*40)
print(f"question number 15")
"""
15. Write a Python program to count number of lists in a list of lists.
"""
list_elements_01=[[1,2,3],[3,4,5],[6,7,8],[9,10],[0,11]]
list_len=len(list_elements_01)
print(list_len)

list_elements_02=[[1,2,3],[3,4,5],[6,7,8],[9,10],[0,11]]
count1=0
for list_ele in list_elements_02:
    count1 =len(list_elements_02)
print(f"total number os lists in list_elements_02 :{count1}")