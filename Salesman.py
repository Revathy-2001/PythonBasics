
import numpy
sm = int(input("No of Salesman: "))
lst = []

# Getting the Amount for each Salesman
print("Enter the Amount of Each Salesman: ")
for k in range(0,sm):
  amt = float(input())
  lst.append(amt)
arr = numpy.array(lst)
print("----------------------------------")
print("Array Values: ",arr )


# (A).Total Amount Of Sales
tot = 0
for j in range(len(arr)):
  tot = tot + arr[j]
print("Total: ",tot,sep = "\t\t\t")
# print("Total: ",arr.sum(),sep = "\t\t\t")

# (B).Average Of Sales
avg = tot/sm
print("Average: ",avg,sep = "\t\t")

# (C). Maximum Amount
print("Maximum amount:",arr.max())

# (D).MaximumIndex
maxid = arr[0]
index = 0
for j in range(len(arr)):
  if(arr[j] > maxid):
    maxid = arr[j]
    index = j
print("maximumId: ",index+1,sep = "\t\t")

# (E). Minimum Amount
print("Minimum amount:",arr.min())

# (F).Minimum index
minid = arr[0]
index = 0
for j in range(len(arr)):
  if(arr[j] < minid):
    minid = arr[j]
    index = j
print("MinimumId: ",index+1,sep = "\t\t")

# (G).Discount For Salesman
print("------------------------")
print("IdNo","Salary",sep = "\t\t")
print("------------------------")
for a in range(len(arr)):
  if(arr[a] > avg):
    bonus = 1000 * 10/100
    bs = bonus + arr[a]
    print(a+1,bs,sep = "\t\t\t")
print("------------------------")
print("----------------------------------")
  