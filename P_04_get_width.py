# Ask user for width and loop until they
#enter a number this is more than zero

error = "Please enter a number that is more than zero\n"
while True:

    try:
        # ask the user for a number
        width = float(input("Width: "))

        # check that the number is more than zero
        if width > 0:
            break
        else:
            print("its too low")
            print(error)

    except ValueError:
        print("you have a value error")
        print(error)