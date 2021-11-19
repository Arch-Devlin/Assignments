def main():
    
    colours = []
    names = []
    adjectives = []
    objects = []
    verbs = []
    
    for a in range(2):
        colours.append(input("Pick colour.\n"))
    for b in range(3):
        names.append(input("Pick name.\n"))
    for c in range(3):
        adjectives.append(input("Pick adjective.\n"))
    for d in range(3):
        objects.append(input("Pick object.\n"))
    for e in range(3):
        verbs.append(input("Pick verb.\n"))
        
    print(names[0] + ' jumped on the '+ adjectives[0] + ' ' + objects[0] + ' where, ' + colours[0] + ' hair flowing in the in the wind, ' + 
    names[0] + ' told ' + names[1] + ' "We need to ' + verbs[0] + ' then, ' + verbs[1] + ' get the '+ objects[1] + 
    ' and get out of there.". "What a ' + adjectives[1] + ' plan ' + names[0] + ' .", ' + names[1] +' replied.\nFar away past the '
    + colours[1] + ' ' + objects[2] + ', ' + names[2] + ' thought as they ' + verbs[2] + ' "What a ' + adjectives[2] + ' story.".')    

main()
