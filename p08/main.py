import random

# range(40)
# range(1, 4)
# range(0, 40, 4)
# #
# y = {'x': 222, 'y': 111, 'z': 12}
# for key, item in y.items():
#     print(key, ' = ', item)
# print(y['y'])

guess = random.randint(1, 10)
while True:
    number = int(input('Input number:'))
    if guess == number:
        print("Win!")
        break
    elif guess > number:
        print("Більше")
    elif guess < number:
        print("Менше")