#function, iterates integers and replaces numbers with words
for numbers in range (50):
    if (numbers %3) ==0 and (numbers %5) == 0:
        print('FizzBuzz')
    elif (numbers %5) == 0:
        print('Buzz')
    elif (numbers %3) == 0:
        print('Fizz')   
    else:
        print(numbers)