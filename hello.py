from ast import comprehension


saarc = ["Bangladesh", "India", "Sri Lanka", "Pakistan", "Nepal", "Bhutan"]
print(saarc)
saarc.append("Afganistan")
print(saarc)
saarc.sort()
print(saarc)
li = [1, 3, 7, 2, 4, 6, 1]
li.sort()
print(li)
li = [1, 2, 3, 4]
li.reverse()
print(li)
li = ['mango', 'banana', 'orange']
li.reverse()
print(li)
li.sort()
print(li)
fruits = ["mango", "banana", "orange"]
# insert(index, item)
fruits.insert(0, "apple")
print(fruits)
fruits.insert(2, "coconut")
print(fruits)
fruits.remove("coconut")
print(fruits)

# fruits.remove("pineapple")
# print(fruits)
# item = "pineapple"
# if item in fruits:
#     fruits.remove(item)
# else:
#     print(item, "not in list")

print(fruits)
item = fruits.pop()
print(item)
print(fruits)

item = fruits.pop(1)
print(item)
print(fruits)

li1 = [1, 2, 3]
li2 = [4, 5, 6, 7, 8]

li1.extend(li2)

print(li1)

li = [1, 2, 3, 3, 4, 5, 6]

print(li.count(3))
print(li.count(5))
print(li.count(10))

li = [1, 2, 3, 3, 4, 5, 6]
del (li[1])
print(li)
del (li[2])
print(li)
# del (li)
# print(li)

li = []
for x in range(10):
    li.append(x)

print(li)

li1 = [1, 2, 3]
li2 = [4, 5, 6]

li = li1 + li2

print(li)

li = li1 * 3

print(li)

li = ["I", "am", "Tasfia"]
print(li)
str = " ".join(li)
print(str)
li = ["a", "b", "c"]
print(li)
str = ",".join(li)
print(str)
li = ["well", "known"]
# well-known
str = "-".join(li)
print(str)

li = [1, 2, 3, 4]
new_li = []

for x in li:
    new_li.append(2 * x)

print(new_li)

# list comprehension

li = [1, 2, 3, 4]
new_li = [2 * x for x in li]
print(new_li)

li = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
even_numbers = []

for x in li:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

even_numbers = [x for x in li if x % 2 == 0]
print(even_numbers)

# Tuple

x = (1, 2, 3)
print(type(x))
x = 1, 2, 3
print(type(x))
x = 1
print(type(x))
x = 1,
print(type(x))

t = ()
print(type(t))

tpl = (1, 2, 3)
print(tpl[0])
print(tpl[1])
print(tpl[2])
# print(tpl[3])

# tuple is a non-mutable object

li = [1, 2, 3]
li[0] = 5
print(li)

tpl = (1, 2, 3)
# tpl[0] = 5  # 'tuple' object does not support item assignment

print(tpl[0])

# packing and unpacking a tuple

# packing
numbers = (10, 20, 30, 40)

n1, n2, n3, n4 = numbers

print(n1)
print(n2)
print(n3)
print(n4)

a1 = 1
a2 = 2
a3 = 3

tpl = a1, a2, a3

print(tpl)

# items = (1, 2, 5.5, ["a", "b", "c"], ("apple", "mango"))
# for item in items:
#     print(item)

# print(items[3][1])
# print(items[4][1])

# rand_list = [1, 2, 5.5, ["a", "b", "c"], ("apple", "mango")]
# for item in rand_list:
#     print(item)

# print(rand_list[3][0])
# print(rand_list[4][0])

# set

# my_set = {"laptop", "cellphone", "cellphone", "glass", "notebook", "pen"}
# for item in my_set:
#     print(item)


# print(type(my_set))

# A = set()

li = [1, 2, 3, 4]
tpl = (4, 5, 6, 7)
A = set(li)
B = set(tpl)

print(A, type(A))
print(B, type(B))

str = "Bangladesh"
A = set(str)

print(A)

str = "Sri Lanka"
A = set(str)

print(A)

A = {1, 2, 3}
print("1", 1 in A)
print("2", 2 in A)
print("5", 5 in A)

A = [4, 5, 6]
print("4", 4 in A)
print("5", 5 in A)
print("8", 8 in A)

A = (7, 8, 9)
print("7", 7 in A)
print("8", 8 in A)
print("9", 9 in A)

# marks = [77, 76, 65, 78, 62, 64, 60, 77, 75, 79]
# roll = input("please enter your roll number: ")

# print("Your marks is", marks[int(roll) - 1])

# marks = [[74, 73], [70, 75], [68, 72], [75, 77]]
# print(marks[0])
# print(marks[1][0])

# dict = {name:value, name:value, name:value}

marks = {1: 77, 2: 76, 3: 65, 4: 78, 5: 62, 6: 64, 7: 60, 8: 77, 9: 75, 10: 79}
print(type(marks))

# Show the marks of roll 4

print(marks[4])

# Show the marks of ID 192473

cse445_marks = {1721360: 78, 192473: 85, 191765: 93}

print(cse445_marks[192473])

# show the marks of Tasfia

# cse445_marks = {"Tasfia": 71, "Musfiq": 85, "Writhy": 93}

# print(cse445_marks["Tasfia"])

# dt = {}
# print(type(dt))

# dt[1] = "Tasfia"
# dt[2] = "Writhy"
# dt[3] = "Musfiq"

# print(dt[4])

# number, strings and tuples can be used for name

dt = {"a": "A", "b": "B", "c": "C"}
dt[(1, 2, 3)] = "tuple"

print(dt)

dt[{1, 2, 3}] = "set"

print(dt)

marks = {"DH1001": {"Bangla": 74, "English": 73},
         "DH1002": {"Bangla": 78, "English": 85}}
