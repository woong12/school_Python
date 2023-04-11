#1
"""
for i in [1, 2, 3] :
    print("안녕하세요")
"""

#2
"""
for i in range(10) : # range(시작값(0), 끝값, 중간값(+1))
    print(i, end=" ")
"""

#3
"""
for i in range(1, 11) : # range(시작값(0), 끝값, 중간값(+1))
    print(i, end=" ")
"""

#4
"""
for i in range(1, 10, 2) : # range(시작값(0), 끝값, 중간값(+1))
    print(i, end=" ") # 1 3 5 7 9
"""

#5
"""
for i in range(20, 0, -2) : # range(시작값(0), 끝값, 중간값(+1))
    print(i, end=" ") # 20 18 16 ... 2
"""

#6
"""
for i in range(0, 3, 1) : 
    print("안녕하세요")
"""

#7
"""
a = 10
for num in range(1, 5, 2) : # num = 1, 3
    a += num # a = 14
print(a, end=" ")
"""

#8
"""
for i in range(1, 4) :
    print(i, "번째 학생의 성적 처리")
"""

#9
"""
for i in range(2, 22, 2) :
    print(i, end=" ")
"""

#10
"""
for i in range(1, 10, 1) :
    print("2 x", i, "=", i*2 )
"""

#11
"""
a = 0
for i in range(1, 11, 1) :
    a += i
    print("i의 값 :", i , "=> 합계 :", a)
"""

#12
"""
sum = 0
for i in range(2, 101, 2) :
    sum += i
print(sum)
"""

#13
"""
sum = 1
num = int(input("숫자입력 : "))
for i in range(num, 0, -1) :
    sum *= i
print(sum)
"""

#14
"""
cnt = 0
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=' ')
        cnt += 1
        if cnt % 7 == 0 :
            print()
"""

#15
"""
n = int(input("정수를 입력하세요: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
"""

#16
"""
a, b = 0, 1
print(a, end=' ')
for i in range(19):
    print(b, end=' ')
    a, b = b, a + b
"""

#17
"""
for i in range(40):
    if i % 10 == 9:
        print('+', end='')
    else:
        print('-', end='')
"""

#18
"""
i = 0
while i < 40:
    if i % 10 == 9:
        print('+', end='')
    else:
        print('-', end='')
    i += 1
"""

#19
"""
for i in range(40):
    if i % 5 == 0 and i % 2 != 0:
        print('+', end='')
    else:
        print('-', end='')
"""

#20
"""
cm = int(input("cm를 입력하세요 : "))
print('-----------------------------------')
print("센치(cm) 인치(inch) 피트(ft) 야드(yd)")
print('-----------------------------------')
for i in range(cm, 101, cm) :
    inch = i * 0.393701
    ft = i * 0.032808
    yd = i * 0.010936
    print(round(i, 1),"\t",round(inch, 1),"\t",round(ft, 1),"\t",round(yd, 1))
print('-----------------------------------')
"""

#21
"""
for i in range(1, 1001) :
    print(i, end=' ')
    if i == 10 :
        break
"""

#22
"""
score = [92, 86, 68, 120, 56, 72] 
for s in score :
    if ( s < 0 or s > 100) :
        break
    print(s)
print("성적 처리 끝")
"""

#23
"""
score = [92, 86, 68, 120, 56, 72] 
for s in score :
    if ( s < 0 or s > 100) :
        continue
    print(s)
print("성적 처리 끝")
"""

#24
"""
print("3 + 4?")
while True :
    a = int(input("정답을 입력하세요 : "))
    if a == 7 :
        print("참 잘했어요")
        break
"""

#25
"""
while True :
    color = input("신호등 색상 입력 : ")
    if color == 'green' :
        print("길을 건너세요")
        break
"""

#26
"""
total =0
n = 1
while True:
    total += n
    if total > 50:
        print("합이 50보다 커지는 수는", n, "이고 합은", total, "이다.")
        break
    n += 1
"""

#27
"""
for dan in range(2, 10) :
    print(dan, "단")
    for hang in range(2, 10) :
        print(dan, "*", hang, "=", dan * hang)
    print()
"""

#28
"""
dan = int(input("원하는 단은?"))
i = 1
while i < 10 :
    print(dan, "*", i, "=", dan * i)
    i += 1
"""