"""
1. l1 = [1, 2, 3, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 4, 1, 2, 1]
   discard all 1's in the list
"""

l1=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4, 1, 2, 3 ]
l2=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4, 1, 2, 3 ]
while(True):
    try:
        l1.remove(1)
    except ValueError:
        break
print(l1)

print("_"*40)

print(f"1:{l1.count(1)}")
print(f"2:{l1.count(2)}")
print(f"3:{l1.count(3)}")

l3=[1,2,3,1,2,3,4,1,2,1,2,1,3,1,4]
print("index".center(40,"_"))

print(f"l3.index(1):{l3.index(1)}")
print(f"l3.index(4):{l3.index(4)}")
print(f"l3.index(4):{l3.index(4,7)}")

print("_"*40)

print(f"+str(l2):{l2}")
rest=[]
for i in l2:
    if i not in rest:
     rest.append(i)
     print(f"by for loop str(rest):{str(rest)}")
print("_"*40)
[rest.append(x)for x in l2 if x not in rest]
print(str(rest))
print("_"*40)
"""
2. l2 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
   discard the elements in the internal lists

"""
p=[1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
print(p)
p[4].clear()
p[7].clear()
print(p)