shopping = []
shopping.append("milk")
print(shopping)

shopping.append("bread")
print(shopping)

shopping.append("butter")
print(shopping)
shopping.append("water")
print(shopping)
shopping.remove("water")
print(shopping)
if "milk" in shopping:
 print("milk is in the list")
total_count = len(shopping)
print(total_count)  
for i in range(len(shopping)):
  idx = i+1
  item = shopping[i]
  print(f"{idx}. {item}")