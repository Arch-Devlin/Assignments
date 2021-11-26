import random
import numpy as np

def main():
    
    items = ["Rusty Sword", "Rusty Armour", "Gold Coin"]
    
    inventory = {
        "Rusty Sword": 0,
        "Rusty Armour": 0,
        "Gold Coin": 0
    }
    
    rooms = np.array([(0,"You've entered The Dungeon. Before you lies a dark room lit by two torches on the left and righm moss covered walls. Ahead of you is a door.",first),
    (1,"The room is empty with a door on the other side.",empty),
    (2,"The room opens out to the outside and there is a door to another room.",outside),
    (3,"There is a monster looming over you. You must defeat, or evade it to get to the door you can see past its hulking body.",monster),
    (4,"The room is empty save a closed chest between you and the door across the room",chest)])
    
    current_room = 0
    room_count = 0
    enter(rooms, items, inventory, current_room, room_count)

def enter(rooms, items, inventory, current_room, room_count):

    room_count = room_count + 1
    print(rooms[current_room][1], f"\nInventory:{inventory}")
    rooms[current_room][2](rooms, items, inventory, current_room, room_count)

def change_room(rooms, items, inventory, current_room, room_count):
    
    new_room = random.randint(1, 4)
    current_room = new_room
    enter(rooms, items, inventory, current_room, room_count)

def get_item(rooms, items, inventory, current_room, room_count):

    trap = random.randint(1, 100)

    if trap == 1:
        print("The chest was trapped. A green gass fills the air and enters your lungs. You look to the door you'll never enter as you fall gasping for your last breath.")
        leave(rooms, items, inventory, current_room, room_count)
    elif trap == 100:
        print("The chest had two items")
        item = random.choice(items)
        inventory[item] = inventory[item] + 1
    item = random.choice(items)
    inventory[item] = inventory[item] + 1

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
            get_item(rooms, items, inventory, current_room, room_count)
            while True:
                ans = input("Do you want to go through the door.[y/n]:")
                if ans == "y":
                    current_room = change_room(rooms, items, inventory, current_room, room_count)
                    break
                elif ans == "n":
                    print("You plan on staying here till you starve?.")
                else:
                    print("You must type y or n.")
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
                print("Your trusty rusty sword betrays you , breaking on first contact with the monster. Luckily the blade does enough damage to injure it enough that you can leave or finish it at leasure.")
                while True:
                    ans = input("Do you want to go through the door.[y/n]:")
                    if ans == "y":
                        current_room = change_room(rooms, items, inventory, current_room, room_count)
                        break
                    elif ans != "n":
                        print("You must type y or n.")
            elif option == "d":
                inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
                print("You make a break for the door, the monster reaches towards you as you pass geting a hit in, your trusty armour breaks on first contact with the monster. Luckily the armour defends you enough that you make it to the door.")
                current_room = change_room(rooms, items, inventory, current_room, room_count)
            else:
                print("You must type f or d.")
    elif int(inventory["Rusty Sword"]) != 0 and int(inventory["Rusty Armour"]) == 0:
        print("You can use your sword to fight the monster")
        inventory["Rusty Sword"] = inventory["Rusty Sword"] - 1
        print("Your trusty rusty sword betrays you , breaking on first contact with the monster. Luckily the blade does enough damage to injure it enough that you can leave or finish it at leasure.")
        while True:
            ans = input("Do you want to go through the door.[y/n]:")
            if ans == "y":
                current_room = change_room(rooms, items, inventory, current_room, room_count)
                break
            elif ans == "n":
                print("Why, what are you planing on in here?. The monster isn't dead you know.")
            else:
                print("You must type y or n.")
    elif int(inventory["Rusty Sword"]) == 0 and int(inventory["Rusty Armour"]) != 0:
        print("You hope your armour will defend you as you run to door")
        inventory["Rusty Armour"] = inventory["Rusty Armour"] - 1
        print("You make a break for the door, the monster reaches towards you as you pass geting a hit in, your trusty armour breaks on first contact with the monster. Luckily the armour defends you enough that you make it to the door.")
        current_room = change_room(rooms, items, inventory, current_room, room_count)
                    


    
main()
