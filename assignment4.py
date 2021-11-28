import random
import numpy as np

def main():
    
    items = ["Rusty Sword", "Rusty Armour", "Gold Coin"]
    
    inventory = {
        "Rusty Sword": 0,
        "Rusty Armour": 0,
        "Gold Coin": 0
    }
    
    rooms = np.array([(0,"You've entered The Dungeon. Before you lies a dark room lit by two torches on the left and righm moss covered walls. Ahead of you is a door.",first,""),
    (1,"The room is empty with a door on the other side.",empty,"\
__________________________________________________________________________\n\
=================================================================    -----|\n\
=========================================================    -------/     |\n\
 _____________________________________________________------/       ][    |\n\
|       ][       ][       ][       ][       ][       |      ][       -----|\n\
|       ][       ][       ][       ][       ][       |       -------/     |\n\
|_______][_______][_______][_______][_______][_______|------/       ][    |\n\
|       ][       ][       ][       ][       ][       |      ][       -----|\n\
|       ][       ][       ][       ][       ][       |       -------/     |\n\
|_______][_______][_______][_______][_______][_______|------/       ][    |\n\
|       ][       ][     ______     ][       ][       |      ][       -----|\n\
|       ][       ][  ,-'  ||  `-.  ][       ][       |       -------/     |\n\
|_______][_______][_/ {~~~||~~~} \_][_______][_______|------/       ][    |\n\
|       ][        /'{~~~~~||~~~~~}'\        ][       |      ][       -----|\n\
|       ][       | {~~~~~~||~~~~~~} |       ][       |       -------/     |\n\
|_______][_______|        ||        |_______][_______|------/       ][    |\n\
|       ][       |        ||        |       ][       |      ][       -----|\n\
|       ][       |        ||        |       ][       |       -------/     |\n\
|_______][_______|        ||        |_______][_______|------/       ][    |\n\
|       ][       |     () || ()     |       ][       |      ][       -----|\n\
|       ][       |        ||        |       ][       |       -------/     |\n\
|_______][_______|        ||        |_______][_______|------/       ][    |\n\
|       ][       |        ||        |       ][       |      ][       -----|\n\
|       ][       |        ||        |       ][       |       -------/     |\n\
|_______][_______|________||________|_______][_______|------/       ][    |\n\
 \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@\_    ][       -----|\n\
  \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_   -------/     |\n\
   \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\/       ][    |\n\
    \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_     -----|\n\
     \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--/     |\n\
      \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\_    |\n\
       \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\--|\n\
        \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~|\n\
         \~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@|"),
    (2,"The room opens out to the outside and there is a door to another room.",outside,"\
 ____________________________________________________\n\
|       ][       ][       ][       ][       ][       |\n\
|       ][       ][       ][       ][       ][       |\n\
|_______][_______][_______][_______][_______][_______|\n\
|       ][       ][       ][       ][       ][       |\n\
|       ][       ][       / \      ][       ][       |\n\
|_______][_______][______/_|_\_____][_______][_______|\n\
|       ][       ][    /( /'\ )\   ][       ][       |\n\
|       ][       ][ ///.\>   </.\ \][       ][       |\n\
|_______][_______][//(.\>     </.) \[_______][_______|\n\
|       ][       ]/(.\>         </.)\       ][       |\n\
|       ][       //.\>           </.\       ][       |\n\
|_______]_______/(.\>             </.)\_____][_______|\n\
|       ][    (/(.\>               </.)\)   ][       |\n\
|       ][    (//.\>               </.\,)   ][       |\n\
|_______][___(//.\>                 </.\,)__][_______|\n\
|       ][  (//.\>                   </.\,) ][       |\n\
|       ][   (//.\>         ~~~~\   </.\,)  ][       |\n\
|_______][____(//.\>    ~~~/~~~ \  </.\,)___][_______|\n\
|       ][     (//.\> ~/ ~~       </.\,)    ][       |"),
    (3,"There is a monster looming over you. You must defeat, or evade it to get to the door you can see past its hulking body.",monster,"\
                                             ,--,  ,.-.\n\
                                    .       '-,-`,'-.' | ._\n\
                ,          .    .   |\         }  )/  / `-,',\n\
               /|          |\  /|   | |        /  \|  |/`  ,`\n\
              [ ,       ,.`  `,` `, | |  _,...(   (      .',\n\
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\ \n\
               \  \_\,``,   ` , ,  /  |         )         _,/\n\
                \  '  `  ,_ _`_,-,<._.<        /         /\n\
                 ', `>.,`  `  `   ,., |_      |         /\n\
                   \/`  `,   `   ,`  | /__,.-`    _,   `\ \n\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \ \n\
                \_,,.) /\    ` /  / ) (-,, ``    ,        |\n\
               ,` )  | \_\       '-`  |  `(               \ \n\
              /  /```(   , --, ,' \   |`<`    ,            |\n\
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)\n\
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`\n\
      (-, \           ) \ ('_.-._)/ /,`    /\n\
      | /  `          `/ \ V   V ,/`     /\n\
   ,--\(        ,     <_/`\      ||      /\n\
  (   ,``-     \/|         \-A.A-`|     /\n\
 ,>,_ )_,..(    )\          ',,_-`  _--`\n\
(_ \|`   _,/_  /  \_            ,--`\n\
 \( `   <.,../`     `-.._   _,-`\n"),
    (4,"The room is empty save a closed chest between you and the door across the room",chest,"*******************************************************************************\n\
          |                   |                  |                     |\n\
 _________|________________.="'"'""'"'"_;=.______________|_____________________|_______\n\
|                   |  ,-"'"'"_,="'"'""'"'"     `"'"'"=.|                  |                   |\n\
|___________________|__"'"'"=._o`"'"'"-._        `"'"'"=.______________|___________________|\n\
          |                `"'"'"=._o`"'"'"=._      _`"'"'"=._                     |\n\
 _________|_____________________:=._o "'"'"=._."'"'"_.-="'"'"'"'"'"=.__________________|_______\n\
|                   |    __.--"'"'" , ; `"'"'"=._o."'"'" ,-"'"'""'"'""'"'"-._ "'"'".   |                   |\n\
|___________________|_._"'"'"  ,. .` ` `` ,  `"'"'"-._"'"'"-._   "'"'". '__|___________________|\n\
          |           |o`"'"'"=._` , "'"'"` `; ."'"'". ,  "'"'"-._"'"'"-._; ;              |\n\
 _________|___________| ;`-.o`"'"'"=._; ."'"'" ` '`."'"'"\` . "'"'"-._ /_______________|_______\n\
|                   | |o;    `"'"'"-.o`"'"'"=._``  '` "'"'" ,__.--o;   |                   |\n\
|___________________|_| ;     (#) `-.o `"'"'"=.`_.--"'"'"_o.-; ;___|___________________|\n\
____/______/______/___|o;._    "'"'"      `"'"'".o|o_.--"'"'"    ;o;____/______/______/____\n\
/______/______/______/_"'"'"=._o--._        ; | ;        ; ;/______/______/______/_\n\
____/______/______/______/__"'"'"=._o--._   ;o|o;     _._;o;____/______/______/____\n\
/______/______/______/______/____"'"'"=._o._; | ;_.--"'"'"o.--"'"'"_/______/______/______/_\n\
____/______/______/______/______/_____"'"'"=.o|o_.--"'"'""'"'"___/______/______/______/____\n\
/______/______/______/______/______/______/______/______/______/______/_____/__\n\
*******************************************************************************"),
    (5,"Three plinths lie before you each with an item on top.",choose,"\n\n\n\n\
   ___________             ___________             ___________\n\
 (___,.....,___)         (___,.....,___)         (___,.....,___)\n\
  \__,.....,__/           \__,.....,__/           \__,.....,__/\n\
    =========               =========               =========\n\
     |||||||                 |||||||                 |||||||\n\
     |||||||                 |||||||                 |||||||\n\
     [=====]                 [=====]                 [=====]\n\
     |||||||                 |||||||                 |||||||\n\
     |||||||                 |||||||                 |||||||\n\
     [=====]                 [=====]                 [=====]\n\
     |||||||                 |||||||                 |||||||\n\
     |||||||                 |||||||                 |||||||\n\
    ,_______,               ,_______,               ,_______,\n\
      )   (                   )   (                   )   (\n\
    ,      `                ,      `                ,      `\n\
  _/_________\_           _/_________\_           _/_________\_\n\
 |_____________|         |_____________|         |_____________|\n")])
    
    current_room = 0
    room_count = 0
    enter(rooms, items, inventory, current_room, room_count)

def enter(rooms, items, inventory, current_room, room_count):

    room_count = room_count + 1
    print(rooms[current_room][1], f"\nInventory:{inventory}", rooms[current_room][3])
    rooms[current_room][2](rooms, items, inventory, current_room, room_count)

def change_room(rooms, items, inventory, current_room, room_count):
    
    new_room = random.randint(1, (len(rooms) - 1))
    current_room = new_room
    enter(rooms, items, inventory, current_room, room_count)

def get_item(rooms, items, inventory, current_room, room_count):
    
    item = random.choice(items)
    print(f"You got a {item}.")
    inventory[item] = inventory[item] + 1
    if item == "Rusty Sword":
        print("\
               />\n\
 (           //-------------------------------------(\n\
(*)OXOXOXOXO(*>======================================\ \n\
 (            \---------------------------------------)\n\
               \>")
    elif item == "Rusty Armour":
        print("\
                     _,--~~--,_\n\
                   ,`          `,\n\
                  /              \ \n\
                 ,=_            _=,\n\
                 |  "'"'"_        _"'"'"  |\n\
                 |_   '"'"'"-..-"'"'"'   _|\n\
                 | "'"'"-.        .-"'"'" |\n\
                 |    "'"'"\    /"'"'"    |\n\
                 |      |  |      |\n\
         ___     |      |  |      |     ___\n\
     _,-"'"'",  "'"'",   '_     |  |     _'   ,"'"'"  ,"'"'"-,_\n\
   _(  \  \   \ =--"'"'"-.  |  |  .-"'"'"--= /   /  /  )_\n\
 ,"'"'"  \  \  \   \      "'"'"-'--'-"'"'"      /   /  /  /  "'"'".\n\
!     \  \  \   \       \  /       /   /  /  /     !\n\
:      \  \  \   \       \/       /   /  /  /      :")
    elif item == "Gold Coin":
        print("\
                     ______________\n\
         __,.,---'''''              '''''---..._\n\
      ,-'                  ____                 '`-,\n\
    /'                   //----\                    '\  \n\
  ;                      ||    ||                    '\  \n\
|'                       ||  | ||                       \n\
                         ||  | ||                       \n\
                         ||  | ||                       \n\
                         ||  | ||                      }\n\
                         ||  | ||                     ;\n\
                          \__|_//                    ,\n\
   \ -.._                  ----             __,,- -/\n\
      '-.._''`---.....______________.....---''__,,-\n\
          ''`---.....______________.....---''\n")

def filler(rooms, items, inventory, current_room, room_count):
    
    print("hi")

def event(rooms, items, inventory, current_room, room_count):
    
    rooms[current_room][2](rooms, items, inventory, current_room, room_count)

def empty(rooms, items, inventory, current_room, room_count):
    
    while True:
        ans = input("Do you want to go through the door.[y/n]:")
        if ans == "y":
            current_room = change_room(rooms, items, inventory, current_room, room_count)
            return current_room
        elif ans == "n":
            print("You have no choice.")
        else:
            print("You must type y or n.")

def outside(rooms, items, inventory, current_room, room_count):
    
    while True:
        ans = input("Do you want to go through the door.[y/n]:")
        if ans == "y":
            current_room = change_room(rooms, items, inventory, current_room, room_count)
            break
        elif ans == "n":
            out = input("Do you want to leave to the outside.[y/n]:")
            if out == "y":
                leave(rooms, items, inventory, current_room, room_count)
            elif out != "n":
                print("You must type y or n.")
        else:
            print("You must type y or n.")
                
def leave(rooms, items, inventory, current_room, room_count):
    
    score = int(room_count) + int(inventory["Gold Coin"])

    if current_room != 0 and current_room != 2:
        score = score - 2
        print(f"Your time in the dungion has come to an end.\nYou have a score of {score}")
        exit(0)
    else:
        print(f"Your time in the dungion has come to an end.\nYou have a score of {score}, your inventory had {inventory}.")
        exit(0)
    
def chest(rooms, items, inventory, current_room, room_count):
    
    while True:
        ans = input("Do you want to go through the door or open the chest. [d/c]:")
        if ans == "d":
            current_room = change_room(rooms, items, inventory, current_room, room_count)
            break
        elif ans == "c":
            trap = random.randint(1, 100)

            if trap == 1:
                print("The chest was trapped. A green gass fills the air and enters your lungs. You look to the door you'll never enter as you fall gasping for your last breath.")
                leave(rooms, items, inventory, current_room, room_count)
            elif trap == 100:
                print("The chest had two items")
                get_item(rooms, items, inventory, current_room, room_count)
            
            get_item(rooms, items, inventory, current_room, room_count)
            
            ans = input("Do you want to go through the door.[y/n]:")
            ref_door(rooms, items, inventory, current_room, room_count, ans)
        else:
            print("You must type d or c.")    
                
def first(rooms, items, inventory, current_room, room_count):
    
    while True:
        ans = input("Do you want to go through the door.[y/n]:")
        if ans == "y":
            current_room = change_room(rooms, items, inventory, current_room, room_count)
            break
        elif ans == "n":
            out = input("Do you want to leave.[y/n]:")
            if out == "y":
                leave(rooms, items, inventory, current_room, room_count)
            elif ans != "n":
                print("You must type y or n.")
        else:
            print("You must type y or n.")

def monster(rooms, items, inventory, current_room, room_count):

    if int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) == 0:
        print("The monster reaches across and grabs you in its hand. Your brief life flashes before your eyes as you look into the creatures gaping jaw closing on your head.")
        leave(rooms, items, inventory, current_room, room_count)
    
    elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) != 0:
        
        while True:
            option = input("Would you like to fight the monster or make a run for the door. [f/d]:")
            if option == "f":
                inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
                print("Your trusty rusty sword betrays you, breaking on first contact with the monster.\
 Luckily the blade does enough damage to injure it enough that you can leave or finish it at leasure.")
                
                while True:
                    ans = input("Do you want to go through the door.[y/n]:")
                    if ans == "y":
                        current_room = change_room(rooms, items, inventory, current_room, room_count)
                        break
                    elif ans != "n":
                        print("You must type y or n.")
            
            elif option == "d":
                inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                print("You make a break for the door, the monster reaches towards you as you pass geting a hit in, your trusty armour breaks on first contact with the monster.\
 Luckily the armour defends you enough that you make it to the door.")
                current_room = change_room(rooms, items, inventory, current_room, room_count)
            else:
                print("You must type f or d.")
    
    elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) == 0:
        print("You can use your sword to fight the monster")
        inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
        print("Your trusty rusty sword betrays you , breaking on first contact with the monster.\
 Luckily the blade does enough damage to injure it enough that you can leave or finish it at leasure.")
        
        while True:
            ans = input("Do you want to go through the door.[y/n]:")
            if ans == "y":
                current_room = change_room(rooms, items, inventory, current_room, room_count)
                break
            elif ans == "n":
                print("Why, what are you planing on here?. The monster isn't dead you know.")
            else:             
                print("You must type y or n.")
    
    elif int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) != 0:
        print("You hope your armour will defend you as you run to door")
        inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
        print("You make a break for the door, the monster reaches towards you as you pass geting a hit in, your trusty armour breaks on first contact with the monster.\
 Luckily the armour defends you enough that you make it to the door.")
        current_room = change_room(rooms, items, inventory, current_room, room_count)
                    
def choose(rooms, items, inventory, current_room, room_count):
    
    while True:
        ans = input("Do you want to take one. [y/n]:")
        if ans == "y":
            trap = random.randint(1, 100)
            
            if trap == 1:
                print("The plinth was trapped. The room fills with water, you try to swim to the top but you hit the ceiling.\
 Changing tactic you head towards the door which turns out to be locked.\
 You bang against the door in futility untill you can no longer help but gasp for breath. Water fills your lungs. You drown.")
                leave(rooms, items, inventory, current_room, room_count)
            elif trap < 80:
                 print("The plinths slide into the floor.")
                 get_item(rooms, items, inventory, current_room, room_count)
                 ref_door(rooms, items, inventory, current_room, room_count, ans)
            elif trap >= 80:
                get_item(rooms, items, inventory, current_room, room_count)
                ans = input("Do you want to take another one. [y/n]:")
                if ans == "y":
                    trap = random.randint(1, 100)

                    if trap < 20:
                        print("The plinth was trapped. The room fills with water, you try to swim to the top but you hit the ceiling.\
 Changing tactic you head towards the door which turns out to be locked.\
 You bang against the door in futility untill you can no longer help but gasp for breath. Water fills your lungs. You drown.")
                        leave(rooms, items, inventory, current_room, room_count)
                    elif trap < 90:
                        print("The plinths slide into the floor.")
                        get_item(rooms, items, inventory, current_room, room_count)
                        ref_door(rooms, items, inventory, current_room, room_count, ans)
                    elif trap >= 20:
                        get_item(rooms, items, inventory, current_room, room_count)
                        ans = input("Do you want to take another one. [y/n]:")
                        if ans == "y":
                            trap = random.randint(1, 100)
                            if trap <= 50:
                                print("The plinth was trapped. The room fills with water, you try to swim to the top but you hit the ceiling.\
 Changing tactic you head towards the door which turns out to be locked.\
 You bang against the door in futility untill you can no longer help but gasp for breath. Water fills your lungs. You drown.")
                                leave(rooms, items, inventory, current_room, room_count)
                            elif trap > 50:
                                get_item(rooms, items, inventory, current_room, room_count)
                                ref_door(rooms, items, inventory, current_room, room_count, ans)
                        
                        if ans == "n":
                            ref_door(rooms, items, inventory, current_room, room_count, ans)
                        
                if ans == "n":
                    ref_door(rooms, items, inventory, current_room, room_count, ans)
           
        if ans == "n":
            ref_door(rooms, items, inventory, current_room, room_count, ans)

def ref_door(rooms, items, inventory, current_room, room_count, ans):
    
    if ans == "n":
   
        while True:
            ans = input("Do you want to go through the door.[y/n]:")
            if ans == "y":
                current_room = change_room(rooms, items, inventory, current_room, room_count)
            elif ans == "n":
                print("You plan on staying here till you starve?")
            else:
                print("You must type y or n.")
    elif ans == "y":
        print("You leave into the next room.")
        current_room = change_room(rooms, items, inventory, current_room, room_count)
    else:
        print("You must type y or n.")
    
main()
