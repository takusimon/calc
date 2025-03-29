from math import pi

while True:
    # output possible options to the user
    print('The following shape areas can be calculated:\n'
    '\t1.Square\n'
    '\t2.Rectange\n'
    '\t3.Triangle\n'
    '\t4.Circle')
    # ask user what shape they are interested in
    shape = int(input('Enter the shape whose area you want calculated: '))

    # determine the shape the user has requested 
    # Ask for relevant values
    if shape == 1:
        sides = int(input('Enter the lenght of the sqaure\'s sides: '))
        area = sides**2
    elif shape == 2:
        length = int(input("Enter the length of your rectangle here: "))
        width = int(input('Enter the width of your rectangle here: '))
        area = length * width
    elif shape == 3:
        height = int(input('Enter the height of the triangle here: '))
        base = int(input('Enter the triangles base here: '))
        area = round((base*height)/2,2)
    elif shape == 4:
        radius = int(input('Enter the radius of the circle here: '))
        area = pi * radius**2
    else:
        print('Oops that is not a valid shape')
    
    print(f'The area is {area}')

    # allow the user to exit the program or calculate more areas
    quit = input("Enter 'q' to quit or 'n' to calculate something else")
    if quit == 'q' or quit == 'Q':
        print('Have a nice day!')
        break