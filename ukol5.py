#function to count even and odd numbers from a series of numbers

list_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_even = 0
cound_odd = 0

for number in list_numbers:
    if (number % 2)==0:
        print(number,'is an even number')
        count_even = count_even + 1
    elif (number %2) !=0:
        print(number, 'is an odd number')
        cound_odd = cound_odd+1
print('the number of even numbers is:', count_even)
print('the number of odd numbers is:', cound_odd)
 


# print('The number of even numbers is:')
# print('The number of odd numbers is:')