from programs import squareFootage
from programs import circumferance

def footage():
    num1 = int(input('how tall is the room?'))
    num2 = int(input("how wide is the room?"))
    num3 = int(input("how long is the room?"))
    print(squareFootage(num1,num2,num3))

def circle():
    num = int(input("What's the radius of the circle?"))
    print(circumferance(num))    

def action():
    decision = input("Do you want to do circle or footage?")
    if decision == "footage":
        footage()
    elif decision == "circle":
        circle()
action()