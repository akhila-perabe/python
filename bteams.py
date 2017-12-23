'''
ID: akhi0508
PROG: bteams
LANG: PYTHON 2.7.6
'''

def checkSum (list, new_list):
    if len(list) == 0:
        sum_arr = []
        for j in range(0,4):
            sum = 0
            for i in range(0,3):
                sum = sum + new_list[j][i]
            sum_arr.append(sum)
        sum_arr.sort()
        return sum_arr[3]-sum_arr[0]
    pos = 0
    while pos < len(new_list):
        if len(new_list[pos]) != 3:
            min = 0
            for i in range(0, 1):
                for j in range(i+1, len(list)):
                    for k in range(j+1, len(list)):
                        x = list[i]
                        y = list[j]
                        z = list[k]
                        new_list[pos].append(x)
                        list.remove(x)
                        new_list[pos].append(y)
                        list.remove(y)
                        new_list[pos].append(z)
                        list.remove(z)
                        diff = checkSum(list, new_list)
                        # Check min here
                        if j==1 and k == 2:
                            min = diff
                        elif diff<min:
                            min = diff
                        list.insert(i,x)
                        new_list[pos].pop()
                        list.insert(j,y)
                        new_list[pos].pop()
                        list.insert(k,z)
                        new_list[pos].pop()
            return min
        else:
            pos = pos+1


list = []
fin = open("bteams.in","r")
list = fin.readlines()
list = map(int, list)

list.sort()
new_list = []
for i in range(0, 4):
    new_list.append([])
print new_list

fout = open("bteams.out", 'w')
fout.write(str(checkSum(list, new_list)))

