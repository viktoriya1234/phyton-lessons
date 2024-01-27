import os
os.system('clear')

print('---------------')
print('----Start------')
print('---------------', end='\n'*3)

p = '123'
passw = input('Введіть пароль: ')

if passw == p:
    print('**********')
    print('*** OK ***')
    print('**********')

    allow = input('Дати доступ до нових y/n')
    if allow == 'y':
        print('\n',"\U0001f44d \U0001F923")

elif passw == '0':
    print('** Ви увійшли як гість **')
elif passw == '1':
    print('** Ви увійшли як користувач **')
else:
    print('!!! В доступі відмовлено !!!')

print('\n'*3)
print('---------------------')
print('-------  END  -------')