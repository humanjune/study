int1,int2,int3 = input().split()
int1 = int(int1)
int2 = int(int2)
int3 = int(int3)
answer = 0
if int1 > int2 and int2 > int3:
    answer += int2
elif int2 > int1 and int1 > int3:
    answer += int1
elif int1 > int3 and int3 > int2:
    answer += int3
elif int3 > int2 and int2 > int1:
    answer += int2
elif int3 > int1 and int1 > int2:
    answer += int1
elif int2 > int3 and int3 > int1:
    answer += int3
elif int1 == int2 and int2 == int3:
    answer += int2
elif int3 > int2 and int2 == int1:
    answer += int2
elif int2 > int1 and int1 == int3:
    answer += int1
elif int1 == int2 and int2 > int3:
    answer += int2
elif int1 == int3 and int3 > int2:
    answer += int3
elif int2 == int3 and int3 > int1:
    answer += int2 
elif int1 > int2 and int2 == int3:
    answer += int2
elif int2 > int3 and int3 == int2:
    answer += int2
elif int3 > int2 and int2 == int1:
    answer += int2
print(answer)
