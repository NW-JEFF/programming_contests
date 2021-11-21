
# from random import randint



def union(arr):
         
        # Sorting based on the increasing order
        # of the start intervals
        arr.sort(key = lambda x: x[0])
         
        # array to hold the merged intervals
        m = []
        s = -10000
        max = -100000
        for i in range(len(arr)):
            a = arr[i]
            if a[0] > max:
                if i != 0:
                    m.append([s,max])
                max = a[1]
                s = a[0]
            else:
                if a[1] >= max:
                    max = a[1]
         
        #'max' value gives the last point of
        # that particular interval
        # 's' gives the starting point of that interval
        # 'm' array contains the list of all merged intervals
 
        if max != -100000 and [s, max] not in m:
            m.append([s, max])
        return(m)


n = 4
seq = [130, -130, 30, -180]

"""with open('21J_test.txt', 'w') as f:
    f.write(f'{n}\n')
    for i in range(n):
        coor = randint(-179, 179)
        f.write('0 '+str(coor)+'\n')
        seq.append(coor)"""

seq.append(seq[0])
ans = [[seq[0],seq[0]]]
for i in range(n):
    y, now = seq[i+1], seq[i]
    if abs(y - now) == 180:
        ans = 'yes'
        break
    elif abs(y - now) < 180:
        if y - now >= 0:
            ans.append([now,y])
            ans = union(ans)
        else:
            ans.append([y,now])
            ans = union(ans)
    else:
        if y - now > 0:
            ans.append([-180,now])
            ans.append([y,180])
            ans = union(ans)
        else:
            ans.append([-180,y])
            ans.append([now,180])
            ans = union(ans)

print(seq)
print(ans)
if ans == [[-180,180]]:
    print('yes')
else:
    print(ans)





