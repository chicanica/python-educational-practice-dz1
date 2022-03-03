# ex1
name = 'Вероника'
print(name)

# ex2
age = 20
message = 'Привет, меня зовут ' + name + '. Мне ' + str(age) + ' лет.'
print(message)

# ex3
name5 = name*5
print(name5)

# ex4
print('Привет, как тебя зовут?')
userName = input()
print('И сколько тебе лет?')
userAge = input()
userMessage = 'Привет, ' + userName + '! Тебе уже ' + userAge + ' лет?! Это так круто!'
print(userMessage)

# ex5
userAge = int(userAge)
if userAge < 18:
    ageMessage = 'Ты не достиг еще совершеннолетия, возращайся позже'
else:
    ageMessage = 'Ты уже достаточно взрослый, присоединяйся к нам!'
print(ageMessage)

# ex6
print(userName[1:-1])
print(userName[::-1])
print(userName[-3:])
print(userName[0:5])

# ex7
print('Кол-во букв в имени: ' + str(len(userName)))
import math
ageNum1 = math.floor(userAge / 10)
ageNum2 = userAge % 10
sum = ageNum1 + ageNum2
print('Сумма цифр возраста: ' + str(sum))
if ageNum1 < 1:
    comp = ageNum2
else:
    comp = ageNum1 * ageNum2
print('Произведение цифр возраста: ' + str(comp))

# ex8
print(userName.upper())
print(userName.lower())
print(userName.capitalize())

# ex9
if " " in userName:
    print('Error userName value')
if (userAge < 0) or (userAge > 150):
    print('Error userAge value')

# ex10
print('Сколько будет 8+2*3?')
answer = input()
answer = int(answer)
if answer == 14:
    print('Правильно!')
else:
    print('Неверно!')

