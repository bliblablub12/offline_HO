#ask for 5 numbres and return the lowest one
#from random import randrange

low = int(input('Please give me a random number.\n')) #zwischenspeicher niedrigster Nummer

for quer in range (4):
    number = number = int(input('Please give me a random number.\n'))
    if number < low:
        low = number


print('the lowest number is', low)