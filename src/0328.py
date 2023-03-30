# 1
"""
name = input("이름을 입력하세요: ")
work = int(input("일주일간 일할 시간을 입력하세요: "))
if work > 40 :
  over = work - 40
  print("초과 시간: ", over)
  print(name, "님의 주급은 ", 12000 * 40 + over * 12000 * 1.5 ,"입니다.")
else : 
  print(name, "님의 주급은", 12000 * work, "입니다.")
"""

# 2
"""
print((3 == 3) and (4 != 3))
print((3 == 3) or (4 != 3))
print(not (4 != 3))
"""

# 3
"""
a = int(input("a입력"))
b = int(input("b입력"))
if a == 3 and b == 4:
  print("OK")
if a == 3 and b == 4:
  print("OKay")
"""

#4
"""
x = int(input("숫자 입력: "))
if x > 10 and x % 2 == 0:
  print("10 초과 짝수")
"""

#5
"""
score1 = int(input("필기성적을 입력하세요: "))
score2 = int(input("실기성적을 입력하세요: "))
if score1 > 80 and score2 > 80 :
  print("합격!0")
else :
  print("불합격!")
"""

#6
"""
age = int(input("몇 살이세요?: "))
if age > 65 or age < 7 and age >= 0 :
  print("입장료는 무료입니다")
else :
  print("입장료는 3000원 입니다.")
"""

#7
"""
age = int(input("나이: "))
tall = int(input("키: "))
if age > 10 and tall > 150 :
  print("놀이기구를 탈 수 있다")
else :
  print("놀이기구를 탈 수 없다")
"""

#8
"""
id = input("아이디를 입력하세요: ")
level = int(input("회원 레벨을 입력하세요: "))
if id == "admin" or level == 1 :
  print("관리자 입니다.")
else :
  print("관리자가 아닙니다.")
"""

#9
"""
num = int(input("정수를 입력하세요: "))
if num >= 1 and num <=100 :
  print(num, "은(는) 1~100 사이에 있다")
else :
  print(num, "은(는) 1~100 사이에 없다")
"""

#10
"""
month = int(input('몇 월?'))
if 3 <= month <= 5 :
  print('봄입니다')
elif 6 <= month <= 8 :
  print('봄입니다')
elif 3 <= month <= 5 :
  print('봄입니다')
elif:
  print('봄입니다')
"""

#11
"""
price = int(input("구매금액: "))
if  price < 20000 :
  print("새벽배송이 불가능합니다.")
elif price >= 50000 :
  print("무료배송입니다")
else :
  print("배송비 2500원리 추가됩니다")
"""

#12
"""
score = int(input("점수를 입력하세요:"))
if score >= 90 :
  print("A등급 입니다.")
elif score >= 80 :
  print("B등급 입니다.")
elif score >= 70 :
  print("C등급 입니다.")
else :
  print("F등급 입니다.")
"""

#13
"""
a = int(input("첫 번째 수 "))
b = int(input("두 번째 수 "))
c = int(input("세 번째 수 "))

if a > b :
  over = a
elif c > a :
  over = c
elif b > a :
  over = b


print("가장 큰 수는 " , over " 입니다")
"""

#14
"""
tem = int(input("온도를 입력하세요 :"))
if tem < 0 :
  print("고체")
elif 0 <= tem < 100 :
  print("액체")
"""

#15
"""
math = int(input("수학시험 점수를 입력하세여: "))
eng = int(input("영어시험 점수를 입력하세여: "))

if math >= 80 and eng >= 80 :
  print("합격")
elif math >= 80 or eng >= 80 :
  print("재시험 기회 제공")
else :
  print("탈락")
"""

#16
"""
price = int(input('물건의 구매가를 입력하세여: '))
print("구매가:", price, '원')
if 10000<= price <50000:
  disc = 5.0
elif 50000 <= price < 300000:
  disc = 7.5
elif 300000 <= price :
  disc = 10.0
else :
  disc = 0.0
print("할인율: ", disc)
print("할인금액: ", price * disc / 100, '원')
print("지불금액: ", price -  (price * disc / 100), '원')
"""

#17
"""
x = 17
if x > 10 :
  if x % 2 == 0:
    print("10초과 짝수")
  else :
    print("10초과 홀수")
else :
  print("10 이하")
"""

#18
"""
userid = input("아이디를 입력하세요: ")
level = int(input("회원 레벨을 입력해 주세요 : "))
if userid == "admin" :
  print("모든 콘텐츠 이용 가능")
elif 2 <= level <= 7 :
  print("일부 콘텐츠 이용 가능")
"""

#19
"""
year = int(input("현재년을 입력해 주새요: "))
month = int(input("현재월을 입력해 주새요: "))
day = int(input("현재일을 입력해 주새요: "))
birthYear = int(input("출생년을 입력해 주새요: "))
birthMonth = int(input("출생월을 입력해 주새요: "))
birthDay = int(input("출생일을 입력해 주새요: "))

if birthMonth < month :
  age = year - birthYear

if birthMonth == month :
  if birthDay < day :
    age = year - birthYear
  else :
    age = year - birthYear - 1
else :
  age = year - birthYear - 1
  
print("---------------------------------")

print("오늘 날짜 : ", year, "년 ", month , " 월", day , "일")
print("생년 월일 : ", birthYear ,"년 ", birthMonth , " 월", birthDay , "일")

print("---------------------------------")

print("만 나이 : ", age, "세")
"""

#20
"""
menu = int(input("메뉴를 선택하세요 : "))
if menu == 1:
    prise = int(input(("당신은 떡볶이를 선택하셨군요!\n몇인분 : "))) * 3000
    print("총 가격: ", prise)
elif menu == 2:
    prise = int(input(("당신은 김밥를 선택하셨군요!\n몇인분 : "))) * 2500
    print("총 가격: ", prise)
elif menu == 3:
    prise = int(input(("당신은 튀김를 선택하셨군요!\n몇인분 : "))) * 3500
    print("총 가격: ", prise)
else:
    print("1 2 3중에 선택하세요")
"""

#21
"""
weghit = int(input("몸무게를 입력하세요 : "))
height = int(input("키를 입력하세요 : "))
age = int(input("나이를 입력하세요 : "))
sex = input("성별를 입력하세요 : 남자/여자")
if sex == "남자":
    print(f"당신의 기초 대사량은 {66.47 + (13.75 * weghit) + (5 * height) - (6.76 * age)}")
else:
    print(f"당신의 기초 대사량은 {655.1 + (9.56 * weghit) + (1.85 * height) - (4.68 * age)}")
"""

#22
"""
kg = int(input("체중을 입력하세요: "))
height = float(input("키를 입력하세요: "))
bmi = kg / (height ** 2)

if 0 <= bmi <= 15 :
  status = "정상"
elif 15 <= bmi <= 25 :
  status = "과체중"
else :
  status = "비만"

print("당신의 bmi 지수는" , bmi , "이며", status , "입니다." )
"""