# 두 수가 주어질때 그 두 수 사이의 소수를 모두 골라 
# 합한 값과 그 중 최솟값을 찾아 출력해주는 함수이다!
# 문제 난이도 : 3(살짝 복잡)
def identify_prime(n):
    result = True
    if n == 1:
        return False
    for x in range(2, n):
        if (n % x) == 0:
            result = False
    return result
input_int_1 = int(input())
input_int_2 = int(input())
max_answer = 0
min_answer = 0
for x in range(input_int_1, input_int_2+1):
    if identify_prime(x) == True:
        max_answer += x
        continue
print(max_answer)

for x in range(input_int_1, input_int_2+1):
    if identify_prime(x) == True:
        min_answer += x
        break
print(min_answer)















