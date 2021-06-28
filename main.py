# here we are going to try and solve the fizzbuzz test


# here we ask the user what range of numbers we want to test for fizzbuzz
n = int(input("\nInput desired range integer\n")) # note that the input value is an integer, so we
#specified it

# here we go through the range of numbers by using i in range. n is the input varible that is given by
# the user
for i in range(n):
    if i % 3==0 and i % 5 ==0:      # there is a specfic reason we started the if statement with "fizzbuzz". If we didn't, our output would be selective. Try it
        print(i, "fizzbuzz")
    elif i % 3== 0:
        print(i, "fizz")
    elif i % 5== 0:
        print(i, "buzz")
    else:
        print(i)                    # Any number not outputed per the previous conditions will still show
    