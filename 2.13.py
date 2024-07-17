list = [1, "One", 2, "Two"]
print(list)
print(type(list))

print(len(list))

list.append("Three")
print(list)
list.insert(4, 3)
print(list)

list.remove(1)
list.remove(2)
list.remove(3)
print(list)