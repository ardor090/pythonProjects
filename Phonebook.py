# create an empty contact dictionary
contact = {}


# creating a while loop to continuously run the phonebook program

def phonebook():
    while True:
        print('''''
        #################################
        MYPY PHONE BOOK
        #################################
        
        1 : Add New Entry
        2 : Delete Entry
        3 : Update Entry
        4 : Lookup Number
        5 : Quit
        ''')
        #   Ask the User to make a selection
        selection = input("Please make your selection: ").lower()

        # if the selection is 1 add new contact
        if selection == "1":
            add_new_entry()
        # if the selection is 2 add delete contact
        elif selection == "2":
            delete_entry()
        # if the selection is 3 update already added contact
        elif selection == "3":
            update_entry()
        # if the selection is 4 find contact
        elif selection == "4":
            lookup_number()
        # if the selection is 5 exit the program
        elif selection == "5":
            print("Thanks for using MYPY phone book")
            break
        # if the selection is not between 1-5, inform user wrong selection
        else:
            print("You've entered a wrong selection")


def add_new_entry():
    #   Request for phone number and contact name
    phone_number = input("Please enter your phone number: ")
    contact_name = input("Please enter the contact name (Enter in the format 'FirstName, Lastname'): ").lower()
    #   Check if the contact already exist in the phonebook
    #   If it does not exist, Update contact list
    if phone_number not in contact.values():
        contact.update({contact_name: phone_number})
        print("Contact Successfully saved")
        print("Shown below is your updated contact: ")
        #  display all the contacts in the phonebook
        for k, v in contact.items():
            print(k, "------>", v)
    #  if the contact exist, inform the user
    else:
        print("The contact already exists")


def delete_entry():
    #   Request for contact name that's already in the phonebook
    name = input("Enter the name of contact you wish to delete: ")
    # check if the contact exists
    if name in contact:
        print("The contact is", name, ":", contact[name])
    # inform user name does not exist
    else:
        print("That contact does not exist, Return to the Main Menu to add it")

    # Ask the user to confirm if they want to delete the contact
    confirm = input("Are you sure you want to delete this contact? Yes/No: ")
    if confirm.capitalize() == "Yes":
        contact.pop(name, None)
        print("You have deleted contact", name)
        # Print the updated contact list
        for k, v in contact.items():
            print("Your updated phonebook is shown below")
            print(k, "------>", v)
    # Take the user back to main menu
    else:
        print("Return to main menu")


def update_entry():
    #   Request for old and new phone number and contact name
    number3 = input("Enter current phone number: ")
    numberNew = input("Enter updated phone number: ")
    name = input("Enter current name: ")
    nameNew = input("Enter updated name: ")
    #   Check if the contact exist in the phonebook
    if number3 in contact.values():
        print("The contact to be changed is", name, ":", contact[name])
        # Delete the old contact
        contact.pop(name)
        # update it with the new info
        contact.update({nameNew: numberNew})
        print("""                              \n
              The new updated contact is""", contact)
    # inform user number does not exist
    else:
        print("                               \n"
              "* Number does not exist in phone book *")


def lookup_number():
    #   Request for contact name that's already in the phonebook
    name = input("Enter the name of contact you wish to view: ")
    # check if entered name already exist
    if name in contact:
        print("The contact is", name, ":", contact[name])
    # inform the user the name does not exist
    else:
        print("That contact does not exist, Return to the Main Menu to add it")


# def display_number():
#     # First check if contact isn't empty
#     # If not empty, print contact
#     if bool(contact) != False:
#         for k, v in contact.items():
#             print(k, "------>", v)
#     else:
#         # Inform the user the contact does not exist.
#         print("You have an empty phonebook!, please return to the Main Menu to add Entry")


# call the function mainMenu to display the available options
phonebook()
