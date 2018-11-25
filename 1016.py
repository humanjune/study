def is_square_nono(x):
    answer = True
    for i in range(2, x+1):
        if x % (i*i) == 0:
            answer = False
            break
    return answer
m, mx = input().split()
m = int(m)
mx = int(mx)
answer = 0
for x in range(m, mx+1):   
    if is_square_nono(x):
        answer += 1
print(answer)   