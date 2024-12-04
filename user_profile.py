# Version 5: Debug and Fix Errors

try:
    # Attempt to read from a file
    with open("user_profile.txt", "r") as file:
        name = file.readline().strip()
        age = int(file.readline().strip())  # Ensure age is an integer
        email = file.readline().strip()
        country = file.readline().strip()

except FileNotFoundError:
    print("Error: The file 'user_profile.txt' was not found.")
    name = "Unknown"
    age = 0
    email = "unknown@example.com"
    country = "Unknown"

except ValueError:
    print("Error: Invalid data format. Age should be an integer.")
    age = 0

# Output
print(f"User Profile Initialized: Name = {name}, Age = {age}, Email = {email}, Country = {country}")
