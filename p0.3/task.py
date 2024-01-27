
import os

age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")


x = int(input("Прошу ввести ціле число: "))
if x < 0:
    x = 0
    print('Негативне число замінено на нуль')
elif x == 0:
    print('Нуль')
elif x == 1:
   print('Один')
else:
    print('Більше')


