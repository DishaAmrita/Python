# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Amrita Bhawal"
age = 24
cgpa = 3.75
is_student = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))
print()



#str
age = str(age)
print(f"My age is {age} which is {type(age)}")


#int 
cgpa = int(cgpa)
print(f"My CGPA is : {cgpa}")


#float
age = float(age)
print(f"My age is : {age}")


#boolean 
name = bool(name)
age = bool(age)
cgpa = bool(cgpa)
print(f"Name : {name}")
print(f"Age : {age}")
print(f"CGPA : {cgpa}")
print()
