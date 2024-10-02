# 1st Method

list1 = ['Table', 'Books', 'Chair', 'Fan', 'Clothes', 'Microphone']

add1 = input("Enter: ")
pos1 = int(input("Enter Position: "))

len1 = len(list1)
list2 = list1.copy()

# updated list
list3 = list1.copy() + ["Extra"]
list3[pos1] = add1

# only last elements
list4 = list1[(pos1+1):len1]

# print(list3)
# print(list4)

# Changing the position of Next elements to get Final List.
for i in range(len1-pos1):
    list3[pos1+(i+1)] = list1[pos1+i]

print("Previous list:", list1)
print(f"Final Inserted list {list3}, after inserting \"{add1}\" at {pos1}")

# ------------------------------
# 2nd method -The Simplest logic of List insertion

list1 = ['a', 'b', 'c', 'd', 'e', 'r', 'yooo']

add1 = input("Enter: ")
pos1 = int(input("Enter Position: "))
len1 = len(list1)

# splitting into forward and backward lists -
list2 = list1[: pos1]
list3 = list1[pos1:]
list4 = [add1]

print(list2)
print(list3)
print(list4)

# adding all lists accordingly --
final_list = list2+list4+list3
print(final_list)
