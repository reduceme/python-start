def get_user_input(start, end):
    loop = True
    while (loop):
        try:
            userInput = int(input('enter your choice'))

            if userInput > end or userInput < start:
                print("Please try again. Not in valid bounds.")

            else:
                loop = False

        except ValueError:
            print("Please try again. Only numbers")

    return userInput

x = get_user_input(1, 20)
print(x)