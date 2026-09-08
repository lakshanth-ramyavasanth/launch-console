print('Welcome to my Launch Console, my name is Lakshanth.')
name = input('What is your name? ')
print()
print(f'Hi, ' + name + '!')
print('What would you like to know about me?')
print()

menu_loop = True
while menu_loop:
    print('1: About me')
    print('2: My goals')
    print('3: Fun Fact')
    print('4: Exit')
    print()
    choice = input('Pick 1-4: ')

    if choice == '1':
        print('I am a current sophmore who is studying Java in school and learning Python through Code2College. I am really \ninterested in the connection between coding and the physical world, and want to go into a career that explores \nthis aspect such as embdeded systems.')
        print()

    elif choice == '2':
        print('My goals are to learn as much as I can about coding, by furthering my skills in Java and Python, and learning C++. \nI also want to learn better communication and professional skills to help me in future internships, interviews, and jobs.')
        print()

    elif choice == '3':
        print('One fun fact about me is that I have a dog name Leo.\nHe is a 6 year old maltipoo, and loves to play and be around people.')
        print()

    elif choice == '4':
        print('Goodbye!')
        menu_loop = False

    else:
        print("Please pick 1, 2, 3, or 4.")
        print()
