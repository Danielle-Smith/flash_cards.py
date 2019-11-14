from random import randint

start = 0

while start > -1:
    x = randint(1,12)
    y = randint(7,8)

    print(x, 'x', y,)
    
    ans = int(input('= '))

    if ans == x*y:
        print('Correct!')
    else:
        print('Incorrect')
        print('The correct answer is', x*y)

