## Система імпорту
Код Python в одному _модулі_ отримує доступ до коду в іншому _модулі_.

#### ПРИКЛАД

В даннму рядку імпортується something_we_want
> import something_we_want 

В даннму рядку імпортується something_we_want, як sww 
> import something_we_want as sww

В даннму рядку з something_we_want імпортується лише something
> from something_we_want import something

В данному рядку з something_we_want імпортируеться something, як s
> from something_we_want import something as s

Синтаксис as дозволяє звертатися до імпортованого модуля по новому імені 

---

Наприклад імпорт модуля __OS__. Цей модуль забезпечує портативний спосіб використання залежних від операційної системи функцій.

> import os

_очистка консолі в операційній системі Windows_
<pre>
os.system('cls')
</pre>
_очистка консолі в операційній системі Linux_
<pre>
os.system('clear')
</pre>


## Оператор __IF__

Оператор if використовується для перевірки умови: якщо умова виконується, ми виконуємо блок операторів (званий блоком if), інакше ми обробляємо інший блок операторів (званий блоком else).  

Слово __else__ необов'язкове.

<pre>
if x < 0:    
    print('Негативне число')
</pre>

<pre>
if x < 0:    
    print('Негативне число')    
elif x == 0:
    print('Нуль')
</pre>

Повна констукція:

<pre>
if x < 0:
    print('Негативне число')
elif x == 0:
    print('Нуль')
elif x == 1:
   print('Один')
else:
   print('Більше одного')
</pre>

## Заокруглення числа
Функція __round()__

> round(number, ndigits=None)

<pre>
number = 13.46
r = round(13.46, 1)
print(r)
</pre>

виведе: 13.5  
