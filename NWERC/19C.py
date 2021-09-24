"""Contest."""

n = int(input())
canvas = []
neigh = [0 for _ in range(n-1)]

x = -1
for i in range(n):
    l, r = map(int, input().split())
    y = l
    canvas.append([l, r])
    if x == y:
        neigh[i-1] = 1
    x = r

p = int(input())
pegs = list(map(int, input().split())) if p>0 else []


no = []
peg_range = [[] for _ in range(n)]
x = 0
sol = True
pegs.append(-1)
for k, c in enumerate(canvas):
    for i, peg in enumerate(pegs[x:]):
        if not(c[0] <= peg <= c[1]):
            if x > 0 and (c[0] <= pegs[x-1] <= c[1]):
                j = i + 1
                peg_range[k].append(pegs[x-1])
            else:
                j = i
            x += i
            if j > 2: sol = False
            no.append(j)
            break
        peg_range[k].append(peg)

if not sol:
    print('impossible')

else:
    output = []
    for i, num in enumerate(no):
        if num == 1:
            c = canvas[i]
            if i < n-1 and neigh[i] and no[i+1] < 2:
                if c[1] not in peg_range[i]:
                    output.append(str(c[1]))
                    no[i+1] += 1
                else:
                    output.append(str(c[0]+1))

            else:
                out = c[1]-1
                if out in peg_range[i]:
                    out -= 1
                output.append(str(out))

        elif num == 0:
            c = canvas[i]
            if i < n-1 and neigh[i] and no[i+1] < 2:
                output.append(str(c[1]))
                no[i+1] += 1
                output.append(str(c[0]+1))

            else:
                output.append(str(c[1]-1))
                output.append(str(c[0]+1))

    print(len(output))
    print(' '.join(output))
