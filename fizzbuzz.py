# Branch 1: Efficiency

# "Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

def main():
    numbers = [n for n in range(1, 101)]
    for number in numbers:
        if number %5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 3== 0:
            print("Fizz")
        elif number% 5 ==0:
            print("Buzz")
        else:
            print(number)
        number = number+ 1
main()

# Source: https://betterprogramming.pub/python-loops-performance-compared-the-fastest-is-b4638744a1ff