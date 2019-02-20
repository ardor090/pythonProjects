alphabets = "abcdefghijklmnopqrstuvwxyz"
key = ""
newMessage = ""

userKey = raw_input("Please Enter your Key ")
message = raw_input("Please Enter a single Message ")

key = int(userKey)

for character in message:
    if character in alphabets:

        position = alphabets.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabets[newPosition]
        newMessage += newCharacter
        # print("The new Character is " + newMessage)
        print("Your new Message is "), newMessage

    else:
        newMessage += character

