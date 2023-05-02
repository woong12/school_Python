#1
"""
for dan in range(2, 10):
  print(dan, '단')
  for hang in range(2, 10):
    print(dan, "*", hang, "=", dan * hang)
  print()
"""

#2
"""
dan = 2
while dan < 10:
    print(dan, '단')
    hang = 2
    while hang < 10:
        print(dan, "*", hang, "=", dan * hang)
        hang += 1
    dan += 1
    print()
"""

#3
"""
for i in range(1, 6):
  for j in range(i):
    print("*", end="")
  print()
"""

#4
"""
for i in range(7):
    for j in range(7):
        if i == j or i + j == 7 - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
"""

#5
"""
n = int(input('어떤 수 : '))
for i in range(2, n):
  if n % i == 0 :
    print('소수 아님')
    break
"""

#6
"""
n = int(input('수 입력 : '))
count = 0
for i in range(2, n+1):
  prime = True
  for j in range(2, i):
   if i % j == 0 :
     prime =False
     break

  if prime :
    print('%5d' %(i), end=' ')
    count += 1
    if count % 5 == 0:
      print()
"""

#7
"""
number = input('숫자를 입력하세요 : ')
total = 0
for n in number:
    if int(n) % 2 != 0:
        total += 1

print("'입력된 숫자 중 홀수의 개수 : %d개" % total)
"""

#8
"""
for i in range(1, 6):
  for j in range(1, 11):
    print("*", end=' ')
  print()
"""

#9
"""
for i in range(1, 5):
  for j in range(i):
    print("*", end="")
  print()
"""

#10
"""
for i in range(1, 6):
  for j in range(5-i):
    print(" ", end="")
  for k in range(i):
    print("*", end="")
  print()
"""

#11
"""
for i in range(5, 0, -1):
  for j in range(i):
    print(i, end=" ")
  print()
"""