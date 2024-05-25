print("""
#################################
WELCOME TO DBS CONSOLE
#################################
""")

# Ask user to enter username
user = input("Please enter your username: \n")

# Escape the string using \\ and Split the value entered by user using \
user = user.split('\\')

# Remove any spaces around the input
try:
    domain = user[0].strip()
    username = user[1].strip()

    # Print the Value
    print("Domain : ",domain)
    print("Username : ",username)
except IndexError:
    print("Please use backslash to seperate domain and username")