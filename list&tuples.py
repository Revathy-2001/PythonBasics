x = [1,5]
print(x)

x.insert(1,3)
print("Inserting 3 at: ",x)

x.append(6)
print("Appending 6: ",x)
x.append([7,9])
print("Appending [7,9]",x)

x.remove(6)
print("Removed 6",x)

x.extend([11,13,15])
print("Extended list: ",x)

x.reverse()
print("Reversed List: ",x)

x.remove([7,9])
print("Removed [7,9]",x)

x.insert(-3,7)
x.insert(-4,9)
print("Inserted 7 and 9: ",x)

x.sort()
print("Sort in asc order: ",x)

print("list has ",len(x), " values")
print("Largest value: ",max(x))

del(x[3])
print("Deleted value at index 3: ",x)

del(x[-1:-4:-1])
print("Deleted last three values: ",x)

del(x[:2])
print('Deleted first Two values: ',x)

