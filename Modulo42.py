list=[]
for i in range(0,10):
    i =int(input())
    y = i % 42
    list.append(y)
print(len(set(list)))

