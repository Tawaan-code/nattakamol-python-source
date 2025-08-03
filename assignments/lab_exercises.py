"""
Week 1 Lab - Additional Practice Exercises
Complete these exercises to reinforce your learning.
"""

# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
Full_name = input("Enter Your Name : ")
Age = int(input("Enter Your ages : "))
Email = input("Enter your Email : ")
Phone_number = input("Enter Your Phone Number : ")
Favorite_hobby = input("Enter Your Hobby : ")
print(f"{Full_name}")
print(f"{Age}")
print(f"{Email}")
print(f"{Phone_number}")
print(f"{Favorite_hobby}")



# Exercise 2: Shopping Receipt
print("\n=== Shopping Receipt ===")
# Ask the user for:
# - Item name
# - Item price
# - Quantity
# Calculate and display the total cost

# Write your solution here:
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total_cost = item_price * quantity
print(f"Item: {item_name}")
print(f"Price: {item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total cost: {total_cost:.2f}")


# Exercise 3: Student Grade Calculator
print("\n=== Student Grade Calculator ===")
# Ask for three test scores and calculate the average
# Display each score and the average

# Write your solution here:


# Exercise 4: Time Converter
print("\n=== Time Converter ===")
# Ask user for a number of minutes
# Convert and display as hours and minutes
# Example: 150 minutes = 2 hours and 30 minutes

# Write your solution here:
minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")





# Exercise 5: Circle Calculator
print("\n=== Circle Calculator ===")
# Ask for the radius of a circle
# Calculate and display:
# - Diameter (2 * radius)
# - Circumference (2 * pi * radius)
# - Area (pi * radius^2)
# Use 3.14159 for pi

# Write your solution here:
radius = float(input("Enter Your Radius : "))
pi = 3.14159
Diameter = 2 * radius
Circumference = 2*pi*radius
Area = pi*radius**2
print(f"{Diameter}")
print(f"{Circumference}")
print(f"{Area}")
# Exercise 6: String Manipulator
print("\n=== String Manipulator ===")
# Ask user for a sentence
# Display:
# - The sentence in uppercase
# - The sentence in lowercase
# - The number of characters
# - The number of words (hint: count spaces + 1)

sentence = input("Enter Your sentence : ")
print(sentence.upper())
print(sentence.lower())
print(f"Number of characters: {len(sentence)}")
print(f"Number of words: {len(sentence.split())}")



# Write your solution here:


# Exercise 7: Password Strength Checker (Basic)
print("\n=== Password Strength Checker ===")
# Ask user for a password
# Display:
# - Length of password
# - Whether it's longer than 8 characters
# - First and last character

# Write your solution here:
password = input("Enter Your Password: ")
print(f"Length of password: {len(password)}")
if len(password) > 8:
    print("Password is longer than 8 characters: True")
else:
    print("Password is longer than 8 characters: False")
if len(password) > 0:
    print(f"First character: {password[0]}")
    print(f"Last character: {password[-1]}")
else:
    print("Password is empty.")




# Exercise 8: Distance Calculator
print("\n=== Distance Calculator ===")
# Ask for speed (miles per hour) and time (hours)
# Calculate and display the distance traveled
# Formula: distance = speed × time

# Write your solution here:
Miles = float(input("Enter your miles/hour : "))
Time = float(input("Enter your hours : "))
Formula = Miles * Time 
print(f"Your Distance is {Formula}")


# Exercise 9: Age in Days
print("\n=== Age in Days Calculator ===")
# Ask for user's age in years
# Calculate and display their age in:
# - Days (approximately, use 365 days per year)
# - Hours
# - Minutes

# Write your solution here:
age = int(input("Enter your age/years : "))
days = age*365
hour = 365*24*age
Minutes = 365*24*60*age
print(f"Age per days : {days} days")
print(f"Age per hour : {hour} hour")
print(f"Age per Minutes : {Minutes} minutes")



# Exercise 10: Bill Splitter
print("\n=== Bill Splitter ===")
# Ask for:
# - Total bill amount
# - Number of people
# - Tip percentage
# Calculate and display:
# - Tip amount
# - Total with tip
# - Amount per person

Total = float(input("Enter your total bill : "))
Number = float(input("Enter amount people : "))
Percent = float(input("Enter Percentage : "))
Tip_amount = (Total * Percent) / 100
Total_with_tip = Total + Tip_amount
Amount_per_person = Total_with_tip / Number
print(f"Tip amount: {Tip_amount:.2f}")
print(f"Total with tip: {Total_with_tip:.2f}")
print(f"Amount per person: {Amount_per_person:.2f}")

Total = float(input("Enter your total bill : "))
Number = float(input("Enter amount people : "))
Percent = float(input("Enter Percentage : "))
Tip_amount = (Total*Percent)/100
Total_with_tip = Tip_amount + Total
Amount_per_person = Total_with_tip / Number
print(f"Tip Amount : {Tip_amount}")

# Write your solution here:


# Bonus Challenge: Mad Libs Game
print("\n=== Mad Libs Game ===")
# Ask user for various words (noun, verb, adjective, etc.)
# Use them to create a funny story
# Example: "The [adjective] [noun] [verb] over the [noun]"

# Write your solution here: