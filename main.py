def formula(number):
    pass

running = True

while running:
    number = int(input("enter a number (or 'q' to quit): "))
    if number == 'q':
        running = False
    else:
        print(number)
        while number != 1:
            number = formula(number)
            print(number)