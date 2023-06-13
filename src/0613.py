# 1
"""
data = input('문자열 입력: ')
for i in range(0, len(data)-1):
  print(data[i], data[i + 1], sep="")
"""

# 2
"""
yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])
"""

# 3
"""
a = "10 20 30 40 50"
b = "나는 서울로봇고 2학년이야"
c = "a:b:c:d"


print(a.split())
print(b.split())
print(c.split(":"))
"""

# 4
"""
s = "python programming"

print("문자열 s의 길이 =", len(s))
print()
print("문자열 s에서 o의 인덱스 =", s.find('o'))
print("문자열 없는 인덱스를 검색 =", s.find('A'))
print("o를 뒤에서부터 검색한 인덱스 =", s.rfind('o'))
print()
print("문자열 s에서 r의 인덱스 =", s.index('r'))
print("문자열 s에서 n의 개수 =", s.count('n'))
print()
print("문자열 s에서 gram의 인덱스 =", s.find('gram'))
print("문자열 s에서 gram의 개수 =", s.index('gram'))
print("문자열 s에서 gram의 개수 =", s.count('gram'))
"""

# 5
"""
s = "python programming"
print("a" in s)
print("z" in s)
print("pro" in s)
print("x" not in s)
"""

# 6
"""
height = input('키를 입력하세요: ')
if(height.isnumeric()) : 
  print(height)
else:
  print("숫자로 입력하세요")
"""

# 7
"""
s = "good morning. MyLove Kim"

print("문자열:",s)
print("대문자로 변경:",s.upper())
print("소문자로 변경:",s.lower())

print("대소문자 반대로 변경:",s.swapcase())
print("첫 글자만 반대로 변경:",s.capitalize())
print("모든 단어의 첫글자를 대문자로 변경:",s.title())
"""

# 8
"""
s = "a:b:c:d"
s = s.replace(':', '#')

print(s)
"""

# 9
"""
s = '  angel  '
print(s+'님')
print(s.lstrip()+'님')
print(s.rstrip()+'님')
print(s.strip()+'님')
"""
