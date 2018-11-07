print('Numbers from 1 to 10')
x = 7

m = int(input('Guess the number: '))
if m == x:
    print('Great! You did it')
else:
    while m != x:
        if m <1 or m >10:
            print('number is between 1 and 10')
            input('Guess the number: ')
            continue
        else:
            input('Guess the number: ')
            continue
