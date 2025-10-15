def int_check(question: object, low: object) -> object:

    error = f"Please enter a number that is more than {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculate how many bits needed to represent an integer
def integer_calc():
    # ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer:", 1)


# main routine goes here
if == integer_ans = integer_calc()
print(integer_ans)

else integer_calc == "xxx":
     break