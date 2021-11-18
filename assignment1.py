import random

def main():
    
    num = roll()
    print(num)
    
    while True:
        run = input( "enter roll to roll again \n " )
        if ( run == "roll" ):
            num = roll()
            print(num)
        else:
            break

def roll():
    
    num = random.randint(1, 6)
    
    return num
    
main()
