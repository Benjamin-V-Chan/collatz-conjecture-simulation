def formula(number):
    if number % 2 == 0: # even
        return number // 2
    return (number * 3) + 1 # odd

running = True

while running:
    number = input("enter a number (or 'q' to quit): ").lower().strip()
    if number == 'q':
        running = False
    else:
        number = int(number)
        print(number)
        while number != 1:
            number = formula(number)
            print(number)