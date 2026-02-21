identity = "Alex" # A string
identity  = 10977320 # An integer

#Learning how python show different data types
# print(f"current identity: {identity} | type: {type(identity)}")


#Trying the multiple assignment role
name, level, is__active = "Alex", 200, True

# A remind that the input function always returns a string, no matter what the user types.
age_input = input("Please enter your age: ")

# Doing maths with it, so therefore we need to convert it to an integer first.
age_next_five_years = int(age_input) + 5
print(f"By the next five years, {name} will be {age_next_five_years} years old.")



# Your Challenge (Student Edition)
# Modify the code above to do the following:

# Ask the user for two numbers (e.g., num1 and num2).

# Multiply them together.

# Print the result in a clean f-string that says: "The product of [num1] and [num2] is [result]."


user_first_num = input("Please enter the first number: ")
user_second_num = input("Please enter the second number: ")
product = int(user_first_num) * int(user_second_num)
print(f"The product of {user_first_num} and {user_second_num} is {product}.")
summation  = int(user_first_num) + int(user_second_num)
print(f"The sum of {user_first_num} and {user_second_num} is {summation}.")

User_num1 = input("Please enter the first number: ")
user_num2 = input("Please enter the second number: ")
difference = int(User_num1) - int(user_num2)