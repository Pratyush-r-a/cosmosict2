fruits = ("apple","banana","cherry")
single = (10)
mixed = ("Mike", 25 , "developer")

print(fruits[0], fruits[-1])
print(fruits[0:2])

print(single)

name,age,role = mixed
print(f"{name} is {age} as {role}")

nums = (4,2,7,2)
print("Count of 2:", nums.count(2))
combined =  fruits + ("mango",)
print("Total items:", len(combined))

nested = ("point",(3,4))
print("X:", nested[1][0])