class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= 40:
         return f"{self.name}: Pass"
        else:
           return f"{self.name}: Fail"

s1 = Student ("Kaushal",0)
s2 = Student ("pratyush", 76)
s3 = Student ("kabin", 69)

print(s1.result())
print(s2.result())
print(s3.result())