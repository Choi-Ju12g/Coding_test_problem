s = input()
answer = len(s)

# 1 ~ 절반 길이까지 모두 검사 최소값
for cut_size in range(1,len(s)//2+1):
    cutStr = ''
    target = s[0:cut_size]
    count = 1
    for i in range(cut_size, len(s), cut_size):
        if s[i:i+cut_size] == target:
            count += 1
        else:
            cutStr += str(count) + target if count>1 else target
            target = s[i:i+cut_size]
            count = 1
    cutStr += str(count) + target if count > 1 else target
    answer = min(answer, len(cutStr))

print(answer)