# Declaring an empty array

list1 = []



# A list of numbers

list1 = [50,51,52,53,54,55,56]


print(list1)

# Cheking Typee
print(type(list1))

# Length of a list

print(len(list1))

#A list of Strings

list2 = ["WhiteHarjr","Coding","Classes"]
print(len(list2))
print(list2)

# Index of an element

index = list1.index(50)
print(index)

print(list1[1])

print(list2[0])

print(list1[-1])

# Accessing list element using slice operator

print(list1[0:2])

print(list2[1:2])

# Slice Operator With Negative Index

print(list1[-3:-1])
print(list2[-3:-1])

#Accessing list elemts using For loop

for elem in list1:
    print(elem)

for elem in list2:
    print(elem)

