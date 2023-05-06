#function rmovec char odd index

# odd_number = (index %2 != 0)
# uneven = 'Pyladies'

# print(uneven)

output =''
sente = str(input('please give me a sentence.\n'))

for index in range (len(sente)):
    if index %2 ==0:
        output = output+ sente[index]
print(output)
