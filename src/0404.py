#1
"""
aimport datetime
from pytz import timezone

now = datetime.datetime.now(timezone('Asia/Seoul'))

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
"""

#2
"""
import random

print(random.random())


print(random.randrange(1, 7))

print(random.randint(1, 6))

print(random.choice([10, 20, 30]))

"""

#3
"""
import datetime 
from pytz import timezone


now = datetime.datetime.now(timezone('Asia/Seoul'))


if(now.hour > 12) :
  time = "오후"
else :
  time = "오전"

print("현재시간은 ", now.hour, "시 ", now.minute, "분으로 " , time , "입니다.")
"""

#4
"""
import datetime 
from pytz import timezone


now = datetime.datetime.now(timezone('Asia/Seoul'))


if now.month > 8:
  season = "가을"
elif now.month > 5:
  season = "여름"
elif now.month > 2:
  season = "봄"
else:
  season = "겨울"


print("이번 달은 ", now.month, "로 ",season, "입니다.")
"""

#5
"""
import random

hour = random.randrange(0, 24)

sunny = random.choice([True, False])

if hour < 12 :
    print("좋은 아침입니다, 지금 시각은 %d시 입니다. " %(hour))
else :
    print("좋은 오후입니다, 지금 시각은 %d시 입니다. " %(hour))

if sunny :
    print('현재 날씨가 화창합니다.')
    if 6 <= hour <= 8 :
        print('종달새가 노래를 한다')
    else :
        print('종달새가 노래를 하지 않는다')

else :
    print("현재 날씨가 화창하지 않습니다.")
    print('종달새가 노래를 하지 않는다')
"""

#6
"""
x = 0
while x < 3 :
    print('안녕하세요.')
    x += 1
"""

#7
"""
student = 1
while student <= 3:
    print(student, "번 학생의 성적을 처리한다.")
    student += 1
"""

#8
"""
dan = int(input("원하는 단은?"))
i = 1
while i <= 9 :
    print(dan, " * ", i, " = ", dan * i)
    i += 1

"""

#9
"""
num = 1
sum = 0
while num <= 10 :
    sum += num
    print("num의 값 : %d => 합계 : %d" %(num, sum))
    num += 1
"""

#10
"""
sum = 0
num = 150

while num <= 300 :
    if num % 2 == 1 :
        sum += num
    num += 1

print("sum = " ,sum)
"""

#11
"""
c = -5
print('-----------------------')
print('섭씨\t화씨')
print('-----------------------')

while c <= 5 :
    print(c, c * 9.0/5.0 * 32.0, sep='\t')    
    c+= 1
print('-----------------------')

"""

#12
"""
n = 10
fact = 1

while n > 0 :  
  fact *= n
  n -= 1
print('10! = %d' %(fact))
"""

#13
"""
num = 1
while num <= 20 :
  if num % 2 == 0 :
    print(num, end=' ')
  num += 1
"""

#14
"""
num = 10

while num <= 50 :
  if num % 3 != 0 :
    print(num, end=' ')
  num += 1
"""

#15
"""
while True:
  pw = input("암호 입력 : ") 
  if pw == 'python' :
    print('로그인 성공')
    break
"""

#16 
"""
import random

answer = random.randint(1, 100)
print('정답 : ', answer)
print('1부터 100사이의 숫자를 맞추기')

guess = -1
sum = 0

while guess != answer :
    guess = int(input("숫자를 맞춰 보세요 : "))
    if guess < answer :
        print('낮음')
    else :
        print('높음')
    sum += 1
print('축하합니다. 시도횟수 = ', sum)
"""

