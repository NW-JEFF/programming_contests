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
                    local_mins.append((i,j))
            elif j == n-1:
                if height_map[0][-2]>ele and height_map[1][-1]>ele:
                    local_mins.append((i,j))
            else:
                if height_map[0][j-1]>ele and height_map[0][j+1]>ele \
                    and height_map[1][j]>ele:
                    local_mins.append((i,j))
        elif i == m-1:
            if j == 0:
                if height_map[-1][1]>ele and height_map[-2][0]>ele:
                    local_mins.append((i,j))
            elif j == n-1:
                if height_map[-1][-2]>ele and height_map[-2][-1]>ele:
                    local_mins.append((i,j))
            else:
                if height_map[-1][j-1]>ele and height_map[-1][j+1]>ele \
                    and height_map[-2][j]>ele:
                    local_mins.append((i,j))
        else:
            if j == 0:
                if height_map[i][1]>ele and height_map[i-1][0]>ele \
                    and height_map[i+1][0]>ele:
                    local_mins.append((i,j))
            elif j == n-1:
                if height_map[i][-2]>ele and height_map[i-1][-1]>ele \
                    and height_map[i+1][-1]>ele:
                    local_mins.append((i,j))
            else:
                if height_map[i][j-1]>ele and height_map[i][j+1]>ele \
                    and height_map[i-1][j]>ele and height_map[i+1][j]>ele:
                    local_mins.append((i,j))

def search_neighbor(coord,visited):
    """within bound, unvisited, not 9."""
    x,y = coord[0],coord[1]
    if 0<x<m-1 and 0<y<n-1:
        neighbors = set([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
    elif x==0 and 0<y<n-1:
        neighbors = set([(x+1,y),(x,y-1),(x,y+1)])
    elif x==m-1 and 0<y<n-1:
        neighbors = set([(x-1,y),(x,y-1),(x,y+1)])
    elif 0<x<m-1 and y==0:
        neighbors = set([(x-1,y),(x+1,y),(x,y+1)])
    elif 0<x<m-1 and y==n-1:
        neighbors = set([(x-1,y),(x+1,y),(x,y-1)])
    elif x==0 and y==0:
        neighbors = set([(x+1,y),(x,y+1)])
    elif x==0 and y==n-1:
        neighbors = set([(x+1,y),(x,y-1)])
    elif x==m-1 and y==0:
        neighbors = set([(x-1,y),(x,y+1)])
    else:  # x==m-1 and y==n-1
        neighbors = set([(x-1,y),(x,y-1)])

    result = []
    neighbors = neighbors-visited
    for nei in neighbors:
        if height_map[nei[0]][nei[1]] != 9:
            result.append(nei)
    return result


basins = []
local_mins = set(local_mins)
while local_mins:
    now = local_mins.pop()
    visited = set()
    stk = [now]  # dfs
    visited.add(now)
    while stk:
        res = search_neighbor(stk.pop(),visited)
        if res:
            stk.extend(res)
            visited=visited|set(res)
    local_mins = local_mins-visited
    basins.append(len(visited))

basins.sort()
print(basins[-1]*basins[-2]*basins[-3])