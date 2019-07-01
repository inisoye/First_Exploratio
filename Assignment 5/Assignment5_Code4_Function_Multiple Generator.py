# Assignment Q3: Write a program to print the 12 multiples of a number given by the user in the format below.

def timesTable12(number):

    '''Generates the product of any number and all numbers between zero and twelve.'''

    for i in range(0,13):
        print(f'{number} * {i} = {number*i}')

timesTable12(93)