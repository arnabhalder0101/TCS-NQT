inp = int(input("Enter any 5 digit number: "))
list1 = []
inp1 = inp

# Extracting digits from number
for i in str(inp):

    store1 = inp % 10
    list1.append(int(store1))
    inp = (inp - store1) / 10
    print("The updated", inp)
    print("The updated list", list1)


x = list1.copy()
y = len(list1)
#
for i in range(y):
    x[i] = list1[(y-1)-i]

print("The number entered is: ", inp1)
print("The number entered after running the program: ", inp)
print("This numbers are: ", x)

print(min(x))
print(max(x))