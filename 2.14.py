dic = {1:'One', 2:'Two', 3:'Three'}
print(dic)

print(dic[2])
dic[4] = 'Four'
print(dic)
dic[5] = 'Five'
print(dic)
del dic[4]
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get(2))
print(dic.pop(3))
print(dic)
dic.clear()
print(dic)