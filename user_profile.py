# Version 4: Read From File (Multiple Inputs)

# Read data from file
with open("user_profile.txt", "r") as file:
    name = file.readline().strip()    # First line is name
    age = int(file.readline().strip())  # Second line is age
    email = file.readline().strip()    # Third line is email
    country = file.readline().strip()  # Fourth line is country

# Output
print(f"User Profile Initialized: Name = {name}, Age = {age}, Email = {email}, Country = {country}")
