import datetime
today = datetime.date.today()
year = today.year
month = today.month
#print(year)
age = int(input('pleae let me know your age.\n'))
moonat = int(input('please let me know which month you were born.\n'))
sto = year-age

if moonat < month:
    sto = sto+100
else:
    sto = sto + 99

print('You current age is:', age)
print('You will turn 100 years old in the year:', sto)