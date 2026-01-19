# Program to store user details in a file

name = input("Enter your name: ")
email = input("Enter your email: ")

# Writing data to file
with open("users.txt", "a") as file:
    file.write(f"{name}, {email}\n")

print("User data saved successfully!")
