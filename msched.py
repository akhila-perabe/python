'''
ID: akhi0508
PROG: crossings
LANG: PYTHON 2.7.6
'''

#Main program
arr = []

fin = open("msched.in", 'r')

n = int(fin.readline())
lines = fin.readlines()
for line in lines:
    line = line.split(' ')
    arr.append((int(line[0]), int(line[1])))

arr.sort(reverse=True)

scheduler = list(map(lambda x: 0, arr))

total_milk = 0
for element in arr:
    deadline = element[1] - 1
    if deadline > n-1:
        deadline = n-1
    while deadline >= 0:
        if scheduler[deadline] == 0:
            scheduler[deadline] = 1
            total_milk = total_milk + element[0]
            break
        else:
            deadline = deadline - 1

fout = open('msched.out', 'w')
fout.write(str(total_milk))

