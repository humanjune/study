x, y = input().split()
x = int(x)
y = int(y)
answer = 0
for i in range(1, x):
    if i == 2:
        answer += 28
    elif (i==4) or (i==6) or (i==9) or (i==11):
        answer += 30
    else:
        answer += 31
answer += y

if (answer % 7) == 0:
    print('SUN')
elif (answer % 7) == 1:
    print('MON')
elif (answer % 7) == 2:
    print('TUE')
elif (answer % 7) == 3:
    print('WED')
elif (answer % 7) == 4:
    print('THU')
elif (answer % 7) == 5:
    print('FRI')
elif (answer % 7) == 6:
    print('SAT')