print("""
#################################
WELCOME TO DBS CONSOLE
#################################
""")
# Create an empty list to store the values
list_of_numbers = []
# current position of iteration
i = 0
# Check if there is error
try:
    # Ask user for the number of element they want to input
    number_of_element = int(input("input the number of element to be stored in the list : "))
    print(("input {} elements in the list : ").format(number_of_element))

    # check if the number of element the user typed has not exceeded
    while i < number_of_element:
    # ask user for integer value(s)
        try:
            user = int(input(("element - {}: ").format(i)))

            # Add the value to the list until the number of element has been reached
            list_of_numbers.append(user)
            # Increment iteration by 1
            i += 1
        except:
            print("Please enter an integer value")
# Ask user to input correct value
except ValueError:
    print("Please enter an integer value")

# look for similar integers
unique_words = set(list_of_numbers)
# count the number of times each integers occur
result = ([(x, list_of_numbers.count(x)) for x in unique_words])
# result = sorted([(x, list_of_numbers.count(x)) for x in unique_words], key=lambda y: y[1])
# Loop through the entire list to display results
for elem in result:
    print(('{} occurs {} times'.format(elem[0], elem[1])))

