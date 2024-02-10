import random
print("\u2591" * 40)
print("\u2591"*4, ' Guess the number from 1 to 3 ', "\u2591"*4)
print("\u2591" * 40)
rating = 0
for i in range(1 , 5):
    print('Raund: {i}:', end=' ')
    random_number = random.randint(1, 3)
    number = int(input('Input number: '))

    if random_number == number:
        print('You guessed!')
        rating += 1
    else:
        print(f'Wrong! [{number} <> {random_number}]')

print(rating)