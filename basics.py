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