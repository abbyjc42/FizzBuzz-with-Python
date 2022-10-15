# Branch 3: Readability

def main():
    # Print numbers in range 1 to 100
    num_range = [n for n in range(1, 101)]
    for i in num_range:
        if i % 5 == 0 and i % 3 == 0:   # If divisible by 3 and 5, print 'FizzBuzz'
            print("FizzBuzz")
        elif i % 3 == 0:    # If divisible by 3 (not 5), print 'Fizz'
            print("Fizz")
        elif i % 5 == 0:    # If divisible by 5 (not 3), print 'Buzz'
            print("Buzz")
        else:   # If divisible by neither 3 nor 5, 
            print(i)

main()

# -------------------------
#  Notes and References
# -------------------------

# "i" was used in place of "number" because context makes the variable's purpose evident and its use
# is confined to the scope of a loop. For those reasons, in this case the decision was made to shorten
# the variable for cleaner code; otherwise, a more descriptive variable would be used.

# foreach was chosen in place of while due to better performance.
# See source on loop comparison: https://betterprogramming.pub/python-loops-performance-compared-the-fastest-is-b4638744a1ff