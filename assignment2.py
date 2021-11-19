import random

def main():
    
    num = roll()
    
    while True:
        try:
            run = int(input( "guess the number (between 1 and 10)\n " ))
        except ValueError:
            print("Must guess an interger.")
            continue
        if run < 0 or run > 10:
            print( "must guess between 1 and 10" )
        elif ( run < num ):
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
