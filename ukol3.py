#convert term to and from celsius and fahrenhait
# import math
# celsius = float(input('please tell me the tem in Celsius.\n'))
# fahrenheit = ((celsius-32)/1.8)

# print('If temp is:', celsius, 'then it is:', fahrenheit, 'in F.')


###################################


temp = input(""" 'is the temperature in Celsius or Fahrenheit?'
If temp is in \'°C\' press C, otherwise press F for temeprature in \'°F\' """)
grad = float(input('please tell me the temp.\n'))

if temp == 'C':
    #grad = float(input('please tell me the temp.\n'))
    fahrenheit = ((grad*1.8)+32)
    print ('The temp is:', fahrenheit, '°F.')
else:
   # grad = float(input('please tell me the temp.\n'))
    celsius =((grad-32)*(5/9))
    print ('The temp is:', celsius, '°C.')

# grad = float(input('please tell me the temp.\n'))
# fahrenheit = ((grad-32)/1.8)
# celsius =((grad+32)*1.8)

