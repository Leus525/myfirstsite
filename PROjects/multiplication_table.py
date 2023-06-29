from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = a * b
print('What\'s' , a , 'x' , b, '?')
z = int(input('Enter answer: '))
if z == c:
    print('Corect!')
else:
    for i in range(2):
        print('Error')
        z = int(input('Enter again: '))
        if z == c:
            print('Corect!')
            break
    if z != c:
        print('Incorrectly')
    
    
