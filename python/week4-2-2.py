print('Numbers from 1 to 10')
x = 7
input('Guess the number: ')
while int(input('Guess the number: ')) != x:
    if 1 < int(input('Guess the number: ')) < 10:
        continue
    else:
        print('Number is between 1 and 10')
        continue
print('Great! You did it')
