# # function = a block of of reusable code 
# # Place () after the function name to invoke it

# def happy_birthday():
#     print("Happy Birthday to you")
#     print("You are old")
#     print("Happy birthday to you")
#     print()

# happy_birthday()
# happy_birthday()
# happy_birthday()
# def happy_birthday (name, age):
#     print(f"Happy Birthday to {name}")
#     print(f"You are {age} years old")
#     print("Happy birthday to you")
#     print()

# happy_birthday("Alice", 25)

# def display_invoice(user_name, amount_due, due_date):
#     print(f"Hello {user_name}")
#     print(f"Amount Due: ${amount_due:.2f}")
#     print(f"Due Date: {due_date}")
#     print("Thank you for your business!")
#     print()

# display_invoice("John Doe", 150.75, "2023-12-31")
# # Methods, Help & Documentation Practice #1
# # Remove the characters to the left of our main text:

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z
# print(add(10, 5))       # Output: 15
# print(subtract(10, 5))  # Output: 5
# print(multiply(10, 5))  # Output: 50
# print(divide(10, 5))    # Output: 2.0

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = f"{first_name} + "" + {last_name}"
full_name = create_name("john", "doe")
print(full_name)  # Output: John Doe
# ,

# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.
