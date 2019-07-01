# Assignment Q3: Write a program to print the reversed form of a string input by a user.

def reverseWord(input_string):

    '''Reverse an inputted string.'''

    reversed_string = input_string[::-1]
    print(input_string[::])

    output = f'\nThe reverse of your input is {reversed_string}'
    print(output)

    # For a palindrome, the input_string and reversed_string variables will match. Therefore:
    if input_string == reversed_string:
        print('\nNote: Your input is a palindrome')

reverseWord('tuutu')