#name = 'Jon' 
#num  123
#print(f'Text {name}, Integer{num}')

#print('Text: %d Number: %s' %('Text', 123))
import os
os.system('clear')


print( 7 == 7)
print( 7 >= 7)
print( 7 > 7)

print(20 // 7)
print(20 % 7)

x = 7
x = x + 10
print(x)

x = int(input('Input number: '))
answer = 'Error'

if x >= 5:
    if x <= 10:
       answer = 'OK!'

print(answer)