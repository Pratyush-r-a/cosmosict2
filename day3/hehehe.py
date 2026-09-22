with open("writenote.txt","w") as f:
    f.write("the shopping list")

with open("writenote.txt","r") as f:
 content = f.read()
 print(content)