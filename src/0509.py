#15 page 반복문 연습 6번부터

#1
"""
n1 = int(input('첫 수를 입력하세요 : '))
n2 = int(input('끝 수를 입력하세요 : '))
n = int(input('합계를 구하고자 하는 배수를 입력하세요 : '))

sum = 0
i = n1

while i <= n2:
    if i % 3 == 0:
        sum += i
    i += 1
print('%d~%d까지의 정수 중 %d의 배수의 합계 : %d' % (n1, n2, n, sum))
"""

#2
"""
k = int(input('n을 입력하시오 : '))
sum = 0
for i in range(1, k + 1):
    temp = 0
    for j in range(1, i + 1):
        temp += j
    sum += temp
print('수열Sn = ', sum)
"""

#3
"""
max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    current = i * j
    if current > max_value:
        max_value = current
        a = i
        b = j
print('최대가 되는 경우:%d * %d = %d' %(a, b, max_value))
"""

#4
"""
questions = ["s_hool", "compu_er", "deco_ation", "windo_", "hi_tory"]
answers = ["c", "t", "r", "w", "s"]

for i in range(len(questions)):
    q = f"{questions[i]} : 밑 줄에 들어갈 알파벳은? "
    guess = input(q)

    if guess == answers[i]:
        print("정답!")
    else:
        print("틀렸어요!")
"""

#5
"""
import random

questions = ["school", "computer", "decoration", "window", "history"]

cnt = 0
for i in range(len(questions)):
    x = random.randint(0, len(questions[i])-1)
    answer = questions[i][x]
    print("answer=", answer)
    questions[i] = questions[i].replace(answer, '_')
    guess = input(f"{questions[i]} : 밑 줄에 들어갈 알파벳은? ")

    if guess == answer:
        print("정답!")
        cnt += 1
    else:
        print("틀렸어요!")

print('맞춘 개수는 %d개 입니다' % cnt)
"""

#6
"""
n = int(input())
for i in range(n):
    print(" " * i + "**")
"""

#7
"""
import random

fruit = ['banana', 'pear', 'watermelon', 'strawberry', 'apple', 'mango', 'durian', 'lemon', 'orange', 'pineapple']
print(f"{fruit}중에 하나를 맞춰보세요.")

number = random.randint(0, 9)

while True:
    guess = input("Enter word: ")

    for i, f in enumerate(fruit):
        if f == guess:
            if i == number:
                print(f"{guess}가 정답입니다")
                exit()
            elif i < number:
                print("예측한 답보다 더 뒤에 있습니다.")
            else:
                print("예측한 답보다 더 앞에 있습니다.")
"""

#8
"""
from random import randint
again = 'y'
print("주사위 게임을 시작합니다.")

while again == 'y':
    print("주사위를 던졌습니다.")
    me = randint(1, 6)
    you = randint(1, 6)

    print('나 : %d' % me)
    print('당신 : %d' % you)

    if me > you:
        print("나의 승리!")
    elif me < you:
        print("당신의 승리!")
    else:
        print("무승부!")

    again = input('계속하려면 y를 입력하세요!')
"""
