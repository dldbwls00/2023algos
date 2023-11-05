import sys
input = sys.stdin.readline
N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AandB = []
for a in A:
    for b in B:
        AandB.append(a+b)
AandB.sort()

CandD = []
for c in C:
    for d in D:
        CandD.append(c+d)
CandD.sort()

result = 0
left, right = 0, len(CandD)-1
sum = 0
while 0 <= right and left < len(AandB):
    sum = AandB[left] + CandD[right]
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        x = 1
        for i in range(left+1, len(AandB)):
            if AandB[left] == AandB[i]:
                x += 1
            else:
                break
        y = 1
        for i in range(right-1, -1, -1):
            if CandD[right] == CandD[i]:
                y += 1
            else:
                break
        result += x*y
        left += x
        right -= y

print(result)

# 출처: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-7453%EB%B2%88-%ED%95%A9%EC%9D%B4-0%EC%9D%B8-%EB%84%A4-%EC%A0%95%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
