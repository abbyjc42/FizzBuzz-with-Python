# Branch 1: Functionality

# "Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

number = 1
while number <=100:
    if number %5 == 0:
        if number% 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    elif number % 3== 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        print(number)
    number = number+ 1

# Note: Given the simplicity of the assignment and the requirement to use 3 branches, the code here
# was written as it was in order to give myself a baseline to improve on.