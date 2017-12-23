'''
ID: akhi0508
PROG: crossings
LANG: PYTHON 2.7.6
'''

fin = open("crossings.in",'r')
n = int(fin.readline())

a = []
b = []
for i in range(0,n):
    line = fin.readline().split(' ')
    a.append(int(line[0]))
    b.append(int(line[1]))

t_list = list(map(lambda x,y:(x,y), a,b))
t_list.sort()

count = 0
unSafeArr = list(map(lambda x: 0, a))

max_y = []
for i in range(0, n):
    if i == 0:
        max_y.append((t_list[0][1], 0))
    elif t_list[i][1] <= max_y[-1][0]:
        unSafeArr[i] = 1
        j = 0
        while j < len(max_y) and t_list[i][1] <= max_y[-1-j][0]:
            unSafeArr[max_y[-1-j][1]] = 1
            j = j+1
    else:
        max_y.append((t_list[i][1], i))

for i in range(0, n):
    if unSafeArr[i] == 0:
        count = count+1

fout = open('crossings.out', 'w')
fout.write(str(count))
