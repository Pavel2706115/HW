# ---------------------------------- Task 1 ---------------------------------- #
### Description:
#  Ask the user for their name, age, and favorite color. Store this information
#  into variables and print a greeting in the console, for example:
#  "Hello, my name is Alice, I am 30 years old, and my favorite color is black."
#  Use f-strings and the variables to construct the message.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
###
    # name = input("Enter your name: ")
    # age = int(input("Enter your age: "))
    # favorite_color = input("Enter your favorite color: ")
    # print(f"Hello, my name is {name}, I am {age} years old, and my favorite color is {favorite_color}.")


### Expected output (example):
# Enter your name: Alice
# Enter your age: 30
# Enter your favorite color: black
# Hello, my name is Alice, I am 30 years old, and my favorite color is black.

# ---------------------------------- Task 2 ---------------------------------- #
### Description:
#  Ask the user for their birth year and the current year.
#  Calculate their age using these inputs, then print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here

    # past = int(input("Enter your birth year: "))
    # current = int(input("Enter the current year: "))
    # age = current - past
    # print(f"You are {age} years old.")

### Expected output (example):
# Enter your birth year: 1995
# Enter the current year: 2025
# You are 30 years old.

# ---------------------------------- Task 3 ---------------------------------- #
### Description:
#  Ask the user to enter a large numeric amount (e.g., 1234567.89).
#  Format this number to be displayed as a USD currency with two decimal places and
#  commas for thousands separators. Example: "$1,234,567.89".
#  Use an f-string to format and print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
    # amount = float(input("Enter an amount: "))
    # formatted_amount = f"${amount:,.2f}"
    # print(formatted_amount)

### Expected output (example):
# Enter an amount: 1234567.89
# $1,234,567.89

# ---------------------------------- Task 4 ---------------------------------- #
### Description:
#  Ask the user for the names and prices of three different shopping items.
#  Create a simple receipt format. Use f-strings to format each item name
#  aligned to the left and its price aligned to the right.
#  Each line for an item should be 30 characters wide.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
    # product_1 = input("Enter name of item 1:")
    # price_1 = int(input("Enter price of item 1:"))
    # product_2 = input("Enter name of item 2:")
    # price_2 = int(input("Enter price of item 2:"))
    # product_3 = input("Enter name of item 3:")
    # price_3 = int(input("Enter price of item 3:"))


    # print(f"{'Shopping list' :^30}")
    # print(f"{product_1:<15}{price_1:>15}")
        
    # print(f"{product_2:<15}{price_2:>15}")
        
    # print(f"{product_3:<15}{price_3:>15}")
      



### Expected output (example):
# Enter name of item 1: Milk
# Enter price of item 1: 1.99
# Enter name of item 2: Bread
# Enter price of item 2: 2.49
# Enter name of item 3: Eggs
# Enter price of item 3: 3.59
#
#           Shopping Items:
# Milk                          1.99
# Bread                         2.49
# Eggs                          3.59

# ---------------------------------- Task 5 ---------------------------------- #
### Description:
#  Ask the user for the current temperature in Celsius.
#  Convert this temperature to Fahrenheit using the formula: $F = (C \times 9/5) + 32$.
#  Print both the Celsius and Fahrenheit temperatures, formatted to one decimal place,
#  using an f-string.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here
    # C = float(input("Enter temperature in Celsius: "))
    # F = (C * 9/5) + 32
    # print(f"{C:.1f}°C is equal to {F:.1f}°F")

### Expected output (example):
# Enter temperature in Celsius: 25
# 25.0°C is equal to 77.0°F