def list_print(two_list):
    for l1 in two_list: 
        for i in l1: 
            print(i, end = ' ')
        print()
def list_position(n, t):
    for x in range(len(t)):
        for i in range(len(t[x])):
            if t[x][i] == n:
                return [x, i]


n = int(input())
position = int(input())
xmin = 0
ymin = 0
xmax = n-1 
ymax = n-1
list1 = [0 for k in range(n)]
two_list = [list(list1) for k in range(n)]
k = n*n
while k > 0:
    for x in range(xmin, xmax+1):
        two_list[x][ymin] = k
        k -= 1
    ymin += 1
    for y in range(ymin, ymax+1):
        two_list[xmax][y] = k
        k -= 1
    xmax -= 1
    for x in range(xmax, xmin-1, -1):
        two_list[x][ymax] = k
        k -= 1
    ymax -= 1
    for y in range(ymax, ymin-1, -1):
        two_list[xmin][y] = k
        k -= 1
    xmin += 1


list_print(two_list)

x, i = list_position(position, two_list)
print(x+1, i+1)

