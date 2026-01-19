# Program to read data from a file

try:
    with open("users.txt", "r") as file:
        print("\nStored User Data:")
        print(file.read())
except FileNotFoundError:
    print("File not found. Please add data first.")
