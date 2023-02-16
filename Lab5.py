'''
lab5
if statment
'''

#3.1
alien_color = 'blue'
if alien_color == 'green':
    print('you got 5 points')
    
#3.2
alien_color= 'red'
if alien_color == 'green':
    print('you got 5 points')
else:
    print('you got 10 points ')

#3.3
favorite_fruits= ('kiwi', 'apples', 'raspberries')
if 'kiwi' in favorite_fruits:
    print('I love kiwi')
if 'apples' in favorite_fruits:
    print('I love apples')
if 'raspberries' in favorite_fruits:
    print('I love raspberries')

#3.4
age = 25
if age<=10:
    print('kid')
elif 20>age>=10:
    print('teenager')
else:
    print('adult')
if age>=65:
        print('elder')