import copy

m, n = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
origin = copy.deepcopy(a)

while(True):
    cnt = cnt + 1
    temp = copy.deepcopy(a)

    for i in range(n):
        for j in range(m):
            if(a[i][j] == 1):
                if(j > 0 and temp[i][j-1] == 0):
                    temp[i][j-1] = temp[i][j-1] + 1
                if(j < m-1 and temp[i][j+1] == 0):
                    temp[i][j+1] = temp[i][j+1] + 1
                if(i > 0 and temp[i-1][j] == 0):
                    temp[i-1][j] = temp[i-1][j] + 1
                if(i < n-1 and temp[i+1][j] == 0):
                    temp[i+1][j] = temp[i+1][j] + 1
    
    check = True
    for i in range(n):
        for j in range(m):
            if(a[i][j] != temp[i][j]):
                check = False
    if(check == True):
        break

    a = copy.deepcopy(temp)

check2 = True
for i in range(n):
    for j in range(m):
        if(a[i][j] == 0):
            check = False
            break;
if(check == True):
    print(cnt-1)
else:
    print(-1)
