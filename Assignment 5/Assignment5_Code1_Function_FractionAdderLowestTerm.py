# Assignment Q1: Create a function that adds two fractions.

print('Only fraction additions can be performed by this program.\n')
print('Note: Your calculation must be added in the format "a/b + x/y". Quotes must be included.\n')

def addFractions(calculation):

    '''Add two fractions with an inputted string.'''

    changed_calculation = calculation.replace('+', '/')
    broken_calculation = changed_calculation.split('/')

    a = int(broken_calculation[0]) # the top of fraction 1
    b = int(broken_calculation[1]) # the bottom of fraction 1
    c = int(broken_calculation[2]) # the top of fraction 2
    d = int(broken_calculation[3]) # the bottom of fraction 2

    fraction_top = (a*d)+(b*c)
    fraction_bottom = b*d

    # here, we use the 'for' and 'while' loop to get our answer in the lowest terms
    for i in range(2,100):
        if fraction_top % i == 0 and fraction_bottom % i == 0:
            while fraction_top % i == 0 and fraction_bottom % i == 0:
                fraction_top = fraction_top/i
                fraction_bottom = fraction_bottom/i

    # now, print the newly defined numerator and denominator
    fraction_sum = f'The solution to your input is {fraction_top}/{fraction_bottom}'
    print(fraction_sum)

addFractions('1/3 + 1/4')