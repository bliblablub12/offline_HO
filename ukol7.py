#dogs age in dogs years


dog_age = float(input('PLease tell me how old your dog is in human years.\n'))
human_age=0

if dog_age <= 2:
    human_age = dog_age*10.5
else:
    human_age = 21 + ((dog_age-2) *4)

print('You dog is:', human_age, 'in dog years')


