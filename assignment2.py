import random

def main():
    
    num = roll()
    
    
    while True:
        run = int(input( "guess the number (between 1 and 10)\n " ))
        if ( run < num ):
            print( "guess too low" )
        elif ( run > num ):
            print( "guess too high" )
        elif ( run == num ):
            print( "Correct!!" )
            break

def roll():
    
    num = random.randint(1, 10)
    
    return num
    
main()
