height_map = []
local_mins = []

from pathlib import Path
d = Path(__file__).resolve().parents[1]/ "2021" / "9.input.txt"

with d.open() as f:
    for l in f.readlines():
        height_map.append(list(map(int,list(l)[:-1])))

m = len(height_map)  # num of rows
n = len(height_map[0])  # num of cols

for i,row in enumerate(height_map):
    for j,ele in enumerate(row):
        if i == 0:
            if j == 0:
                if height_map[0][1]>ele and height_map[1][0]>ele:
                    local_mins.append(ele)
            elif j == n-1:
                if height_map[0][-2]>ele and height_map[1][-1]>ele:
                    local_mins.append(ele)
            else:
                if height_map[0][j-1]>ele and height_map[0][j+1]>ele \
                    and height_map[1][j]>ele:
                    local_mins.append(ele)
        elif i == m-1:
            if j == 0:
                if height_map[-1][1]>ele and height_map[-2][0]>ele:
                    local_mins.append(ele)
            elif j == n-1:
                if height_map[-1][-2]>ele and height_map[-2][-1]>ele:
                    local_mins.append(ele)
            else:
                if height_map[-1][j-1]>ele and height_map[-1][j+1]>ele \
                    and height_map[-2][j]>ele:
                    local_mins.append(ele)
        else:
            if j == 0:
                if height_map[i][1]>ele and height_map[i-1][0]>ele \
                    and height_map[i+1][0]>ele:
                    local_mins.append(ele)
            elif j == n-1:
                if height_map[i][-2]>ele and height_map[i-1][-1]>ele \
                    and height_map[i+1][-1]>ele:
                    local_mins.append(ele)
            else:
                if height_map[i][j-1]>ele and height_map[i][j+1]>ele \
                    and height_map[i-1][j]>ele and height_map[i+1][j]>ele:
                    local_mins.append(ele)

print(sum(local_mins)+len(local_mins))