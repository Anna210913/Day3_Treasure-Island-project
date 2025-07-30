print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right'\n ").lower()

if choice_1 == 'left':
    choice_2 = input("You've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boat. Type 'swim' to swim across.\n ").lower()
    if choice_2 == 'wait':
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice_3 == 'yellow':
            print("You suddenly find yourself in the movie 'blink twice' and you do not survive. Game over!")
        elif choice_3 =='red':
            print("The ground is lava! Game over!")
        elif choice_3 == 'blue':
            choice_4 = input("The door opens to a train_track that will take you to the next island.\n The conductor offers you a ride for free. Do you accept or do you choose to walk?\n Type 'Y' to accept and 'N' to walk\n").lower()
            if choice_4 =='y':
                print("Didn't your mother teach you never to accept rides from strangers? The conductor kidnaps you and sells you for a treasure map. Game over!")
            elif choice_4 =='n':
                print("Congratulations, you won the treasure! You are now physically fit.")
        else:
            print("We do not have this option so, you are dead. Game over!")
    elif choice_2 == 'swim':
        print("The water was acidic and it burnt off all your flesh. Game over!")
    else:
        print("You picked something that wasn't an option. Game over!")

else:
   print("You've fallen and you can't get up. Game over.")


