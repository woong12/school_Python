score = []

for i in range(5):
    num = int(input("성적 입력: "))
    score.append(num)

print(score)

sum = 0
for s in score:
    sum += s

print("총점은 %d이고 평균은 %.1f입니다." % (sum, sum / len(score)))
