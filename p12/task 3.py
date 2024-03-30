import pygame

def test(a, b):
    if a > 0:
        result = '> 0'
    else:
        result = '< 0'

    if b < 0:
        result += ' : b - > 0'

    return result

print('====>', test(11))