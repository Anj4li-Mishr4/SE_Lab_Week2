#Version 3: Using a file for user details
# Read name from a file
with open("user_name.txt", "r") as file:
    name = file.read().strip()

# Other predefined values
age = 21
email = "amishra12@gitam.in"
country = "India"

# Output
print(f"User Profile Initialized: Name = {name}, Age = {age}, Email = {email}, Country = {country}")
        