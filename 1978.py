# n개의 숫자가 들어오면 그 중 소수의 개수를 찾는 문제이다!
# 선생님과 함께 풀어보자!
# 문제 난이도 : 2(평범)
# 소수의 기준 : 
def identify_prime(n):
    result = True
    if n == 1:
        return False
    for x in range(2, n):
        if (n % x) == 0:
            result = False
    return result
answer = 0
n = int(input())
n_2 = input().split()
for x in range(len(n_2)):
    n_2[x] = int(n_2[x])
for i in n_2:
    if identify_prime(i) == True:
        answer += 1
print(answer)


















