# Assignment Q2: Create a program that tells if a number is odd or even.

def evenOrNot(number):

    '''Determine if a number is odd or even.'''

    if number%2 == 0:
        print(f'The number you have inputted ({number}) is an even number')
    else:
        print(f'The number you have inputted ({number}) is an odd number')

evenOrNot(29)