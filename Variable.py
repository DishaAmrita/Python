# Variable = A container for a value.
# Four diffrerent data types : string, integer, float, boolean.
# A variable behaves as if it was the value it contains.


# Strings
first_name = "Amrita"
print(first_name)

# f-string
print(f"My name is : {first_name}.")
print()

food = "Chicken Fry"
print(f"I like {food}.")

email = "bhawalamrita@gmail.com"
print(f"My email address is : {email}.")
print()




#Integers
age = 24
print(f"Your age is :{age}.")

qty = 5
print(f"You are buying {qty} items.")

num_of_students = 50
print(f"Your class has {num_of_students} students.")
print()




#Floats
price = 10.99
print(f"The price of the product is : ${price}.")

cgpa = 3.75
print(f"Your CGPA is : {cgpa}.")

distance = 5.5 
print(f"You ran for {distance} km.")
print()




#Boolean 
is_student = True
print(f"Are you a student? : {is_student}")

if is_student :
    print("You are a student.")
else :
    print("You are NOT a student.")


for_sale = False 
if for_sale :
    print("This product is available on store.")
else : 
    print("This product is NOT available on store.")