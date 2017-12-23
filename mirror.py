'''
ID: akhi0508
PROG: crossings
LANG: PYTHON 2.7.6
'''


dict = {}
n = 0
m = 0

#Function getReflection
def getReflections(dict, start_x, start_y, start_dir):
    x, y, dir = start_x, start_y, start_dir
    count = 0
    visited = []
    while x in range(0, n) and y in range(0, m):
        # Check if the path is a cycle, if the mirror was already in path
        if visited.__contains__((x, y, dir)):
            count = -1
            break
        else:
            visited.append((x, y, dir))
        count = count + 1
        (x, y, dir) = dict[(x, y)][dir+1]
    return count


# Main program starts here
fin = open("mirror.in", 'r')
n, m = map(int, fin.readline().split(' '))

j = 0
for line in fin.readlines():
    l = []
    for i in range(0, m):
        dict[(j, i)] = [line[i]]
        if line[i] == '\\':
            dict[(j, i)] = [line[i], (j+1, i, 2), (j-1, i, 3), (j, i+1, 0), (j, i-1, 1)]
        else:
            dict[(j, i)] = [line[i], (j-1, i, 3), (j+1, i, 2), (j, i-1, 1), (j, i+1, 0)]
    j = j+1

max_count = 0

# For each row side
for i in range(0, n):
    c = getReflections(dict, i, 0, 0)
    if c == -1:
        max_count = -1
        break;
    max_count = max(max_count, c)

if max_count != -1:
    # For each column side
    for i in range(0, m):
        c = getReflections(dict, 0, i, 2)
        if c == -1:
            max_count = -1
            break;
        max_count = max(max_count, c)

if max_count != -1:
    # For each row side
    for i in range(0, n):
        c = getReflections(dict, i, m-1, 1)
        if c == -1:
            max_count = -1
            break;
        max_count = max(max_count, c)

if max_count != -1:
    # For each column side
    for i in range(0, m):
        c = getReflections(dict, n-1, i, 3)
        if c == -1:
            max_count = -1
            break;
        max_count = max(max_count, c)

fout = open('mirror.out', 'w')
fout.write(str(max_count))
