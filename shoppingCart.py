shoppingList = []

def adding():
    shoppingList.append(input("What would you like to add? "))
    print ("This is your shopping list:")
    print(shoppingList)
    decision = input("Would you like to add anything else?")
    decision = decision.lower()
    if decision == "yes":
        adding()
    else:
        return

def deleting ():
    shoppingList.remove(input("What would you like to remove?"))
    print(shoppingList)
    decision = input("Would you like to delete anything else?")
    decision = decision.lower()
    if decision == "yes":
        deleting()
    elif decision == "no":
        return


def shoppingCart():
    done = False
    while done != True:
        decision = input("Would you like to add, delete, check or quit? ")
        decision = decision.lower()
        if decision == "quit":
            done = True
            print ("Ok. Here's your final shopping list:")
            print (shoppingList)
            break
            
        elif decision == "add":
            adding()
        elif decision == "delete":
            deleting()
        elif decision == "check":
            print (shoppingList)
        else:
            print("That command is not valid. Please try again")

print("Welcome to your shopping cart.")
shoppingCart()
print ("Goodbye")