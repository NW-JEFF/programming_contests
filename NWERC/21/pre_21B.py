atts = {}
events = {}

n, k = map(int, input().split())
for _ in range(n):
    name, s = input().split()
    atts[name] = int(s)

l = int(input())
for _ in range(l):
    name, t = input().split()
    if not events.get(name):
        events[name] = [int(t), 1, 0]  # max, num_max, num_rest
    else:
        att = events[name]
        if int(t) > att[0]:
            att[0], att[1], att[2] = int(t), 1, att[1]+att[2]
        elif int(t) == att[0]:
            att[1] += 1
        else:
            att[2] += 1

min_pass = 0
base_point = 0
greedy = []
for n, m in events.items():
    total = m[1] + m[2]
    if m[0] - atts[n] >= 0:  # 需要拉到最低门槛
        min_pass += m[0] - atts[n]
        base_point += m[2] * m[0]
        greedy.append([m[0]*m[1]+total, 0])
        greedy.append([total, 1])
    else:  # 已超最低门槛
        base_point += total * atts[n]
        greedy.append([total, 1])
    

if k < min_pass:  # 无法过关
    print(0)
else:
    point = k - min_pass
    result = base_point
    if point > 0:
        greedy.sort()
        i = -1
        while (not greedy[i][1]) and point > 0:
            result += greedy[i][0]
            i -= 1
            point -= 1
        result += point * greedy[i][0]
    print(result)