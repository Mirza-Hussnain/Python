print("Welcome to the Treasure Island")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|______|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|______|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/___
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("You find yourself at a crossroads. You have three options:")

choice1 = input("1. Turn right\n2. Turn left\n3. Go ahead\nChoose an option (1/2/3): ")

# Check the first choice
if choice1 == "1":
    print("You have reached the beach!")
    print("At the beach, you see two options:")
    choice2 = input("1. Swim to the boat\n2. Wait for the boat\nChoose an option (1/2): ")

    # Check the second choice at the beach
    if choice2 == "1":
        print("You decided to swim to the boat.")
        print("Oh no! There were sharks in the water. Game over!")
    elif choice2 == "2":
        print("You decided to wait for the boat.")
        print("The boat arrives, and you sail to an island.")

        print("On the island, you see three doors:")
        choice3 = input("1. Open the black door\n2. Open the blue door\n3. Open the red door\nChoose an option (1/2/3): ")

        # Check the third choice on the island
        if choice3 == "1":
            print("Congratulations! You opened the black door and found the treasure. You win!")
        else:
            print("Oops! You chose the wrong door. Game over!")
    else:
        print("Invalid choice. Game over!")

elif choice1 == "2" or choice1 == "3":
    print("Oops! You chose the wrong path. Game over!")

else:
    print("Invalid choice. Game over!")