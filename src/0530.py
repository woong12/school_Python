# 1
"""
score = []
for i in range(5):
  score.append(int(input('성적 입력 : ')))
sum = 0
for s in score:
  sum += s
print(score)
print('총점은 %d이고 평균은 %.1f입니다.' %(sum, sum / 5))
"""

# 2
"""
numbers = [[10, 20, 30],[40, 50, 60]]
for i in numbers:
  print(i)
for i in numbers[0]:
  print(i, end=" ")
print()
for i in numbers[1]:
  print(i, end=" ")

print(numbers[0])
print(numbers[1])
print(numbers[0][0])
print(numbers[0][1])

"""

# 3
"""
numbers = [[10, 20, 30],[40, 50, 60, 70, 80]]

for i in numbers[0]:
  print(i, end=" ")
print()
for i in numbers[1]:
  print(i, end=" ")


"""

# 4
"""
for sub in numbers:
  for i in sub:
    print(i, end=" ")
  print()

"""

# 5
"""
data = [[10, 20], [30, 40], [50, 60], [70, 80]]
for i in range(4) :
  for j in range(2):
    print("data[%d][%d] = %d" %(i, j, data[i][j] ))
"""

# 6
"""
strings = [['원두커피', "라떼", "콜라"], [ '우동', '국수', '피자', '파스타']]

for i in range(2):
  for j in  range(len(strings[i])):
    print("%s"%strings[i][j], end=" ")
  print()
"""

# 7
"""

"""

# 8
"""

"""

# 9
"""

"""

# 10
"""

"""

# 11
"""
data = [[10, 20, 30,], [40, 50], [60, 70, 80, 90]]
print(data)

for i in range(len(data)):
  print(data[i][0])
"""

# 12
"""
[2 * n for n in range(1,11)]
"""

# 13
"""
even1 = [2 * n for n in range(1, 51)]
even2 = [n for n in range(1,101) if n % 2 == 0]
print(even1)
print(even2)
"""

# 14
"""
li = []
for n in range(1, 10):
  if n % 3 == 0:
    li.append(n * n)
print(li)
"""

# 15
"""
numbers = [1,2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
"""

# 16
"""
v = [17, 92, 18, 33, 58, 7, 33, 42]

max = v[0]
for i in range(len(v)):
  if max < v[i]:
    max = v[i]

print("최대값 = %d" %(max))
"""

# 17
"""
for i in [1, 2, 3]:
  for j in ['a', 'b', 'c']:
    print(j* i, end=' ')
"""

# 18
"""
list_a = ["I", "study", "python", "language", "!"]

for i in range(len(list_a)) :
  if(len(list_a[i]) >= 3):
    print(list_a[i])
"""

# 19
"""
s = "python"
print(s[0])
print(s[-1])
"""

# 20
"""
s = "python"
print(s[10])
"""

# 21
"""
a = input('첫번째 문자열 : ')
b = input('두번째 문자열 : ')
c = input('세번째 문자열 : ')
if a[-1] == b[0] and b[-1] == c[0] and c[-1] == a[0]:
  print('good')
else :
  print('bad')
"""

# 22
"""
s = "python"
for c in s:
  print(c, end=",")
print()
"""

# 23
"""
number = input("하이픈(-)을 포함한 휴대번호를 입력하세요: ")

for i in number:
  if i!='-':
    print(i, end='')
"""

# 24
"""
s = 'python'
print(len(s))
n = '여섯글자이다'
print(len(n))
"""

# 25
"""
sentence = input('문자열 입력: ')

for i in range(len(sentence)):
  if sentence[i] == 't':
    print(i + 1, end= '')
"""

# 26
"""
sentence = input("문장을 입력해 주세요 : ")

i = len(sentence) - 1
while  i >= 0 :
  if sentence[i] == " ":
    print("-", end="")
  else:
    print(sentence[i], end="")
  i -= 1
"""

# 27
"""
data = input('문자열 입력:')

for i in range(len(data) - 1):
  print(data[i], data[i + 1], sep="")
"""

# 28
"""
s = 'python'
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])
print(s[-2:])
"""

# 29
"""
s = "차종: 코란도C, 제조사:쌍용, 배기량: 1998"
print(s[14:16])
"""

# 30
"""
file = "20210505-104830.jpg"
print("촬영 날짜: " + file[4:6] + "월" + file[6:8] + "일")
print("촬영 날짜: " + file[9:11] + "시" + file[11:13] + "")
print("확장자:" + file[16:19])
"""

# 31
"""
yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])
"""

# 32
"""
jumin = "901231-1914983"
year = jumin[:2]
if int(jumin[7]) % 2 == 0:
    gender = "여자"
else:
    gender = "남자"
print("{}년생 {}입니다.".format(year, gender))
"""
