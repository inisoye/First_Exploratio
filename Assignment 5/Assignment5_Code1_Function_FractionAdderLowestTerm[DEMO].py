# Assignment Q1: Create a function that adds two fractions.

print('Only fraction additions can be performed by this program.\n')
def addFractions(a, b, c, d):
    fraction_top = (a*d)+(b*c)
    fraction_bottom = b*d

    # here, we use the 'for' and 'while' loop to get our answer in the lowest terms
    for i in range(2,100):
        if fraction_top % i == 0 and fraction_bottom % i == 0:
            while fraction_top % i == 0 and fraction_bottom % i == 0:
                fraction_top = fraction_top/i
                fraction_bottom = fraction_bottom/i

    # now, print the newly defined numerator and denominator
    fraction_sum = f'The solution to your input is {fraction_top}/{fraction_bottom}\n'
    print(fraction_sum)

addFractions(1,3,1,5)