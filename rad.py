import random
response = "y"
while response == "y":
    no = random.randint(1,6)
    if(no == 1):
        print("[-----]")
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]")
        print ()
        response = input("Press y to roll the dice and n to exit : ")

    elif(no == 2):
        print("[-----]")
        print("[0    ]") 
        print("[     ]") 
        print("[    0]") 
        print("[-----]")
        print ()
        response = input("Press y to roll the dice and n to exit : ")


    elif(no == 3):
        print("[-----]")
        print("[0    ]") 
        print("[  0  ]") 
        print("[    0]") 
        print("[-----]")
        print ()
        response = input("Press y to roll the dice and n to exit : ")

    elif(no == 4):
        print("[-----]")
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]")
        print ()
        response = input("Press y to roll the dice and n to exit : ")

    elif(no == 5):
        print("[-----]")
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]")
        print ()
        response = input("Press y to roll the dice and n to exit : ")

    elif(no == 6):
        print("[-----]")
        print("[0   0]") 
        print("[0   0]") 
        print("[0   0]") 
        print("[-----]")
        print ()
        response = input("Press y to roll the dice and n to exit : ")

    else :
        print("Seems like there is an error")

        