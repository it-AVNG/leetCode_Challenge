str = input("input a string: ")
reverse = ''
list = [*str]
while len(list)!=0:
    reverse += list.pop()

print(str)
print(reverse)