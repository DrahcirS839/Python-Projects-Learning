correct_password = "python123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password:
	password = input("Wrong password! Try password again: ")

print("Hi ", name, "you are Logged in")
