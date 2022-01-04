from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    a,b,c,d = 0,0,0,0  # 10,01,11,00
    for i in range(n):
        if s1[i] == "1":
            if s2[i] == "0":
                a += 1
            else:
                c += 1
        else:
            if s2[i] == "1":
                b += 1
            else:
                d += 1
    start = (a,b,c,d)
    if a == 0 and b == 0:
        print(0)
    else:
        solved = False
        visited = set([start])
        bfs = deque([start])
        dist = {start:0}
        while bfs:
            now = bfs.popleft()
            if now[0] > 0:
                new = (now[3]+1,now[2],now[1],now[0]-1)
                if not new in visited:
                    dist[new] = dist[now]+1
                    bfs.append(new)
                    visited.add(new)
                    if new[0] == 0 and new[1] == 0:
                        print(dist[new])
                        solved = True
                        break
            if now[2] > 0:
                new = (now[3],now[2]-1,now[1]+1,now[0])
                if not new in visited:
                    dist[new] = dist[now]+1
                    bfs.append(new)
                    visited.add(new)
                    if new[0] == 0 and new[1] == 0:
                        print(dist[new])
                        solved = True
                        break
        if not solved:
            print(-1)