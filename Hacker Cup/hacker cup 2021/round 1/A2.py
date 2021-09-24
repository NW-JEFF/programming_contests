T = int(input())
with open('A2_sol.txt','w') as fi:
    for i in range(1, T+1):
        n = int(input())
        w = input()
        In = []  # key indeces which determine whetehr to switch
        Out = []
        current = -2
        current_index = -2
        result = 0
        for j in range(n):
            if w[j] == 'F':
                continue
            else:
                if current == -2:
                    current = w[j]
                    current_index = j
                else:
                    if w[j] == current:
                        current_index = j
                    else:
                        In.append(current_index)
                        Out.append(j)
                        current = w[j]
                        current_index = j
        
        if not Out:
            fi.write(f'Case #{i}: 0\n')
            continue
        
        l = len(In)
        In = [-1] + In
        Out = Out + [n]

        diff_out = []
        now = -1
        for o in Out:
            if now == -1:
                now = o
            else:
                diff_out.append(o-now)
                now = o
        
        In_num = []
        now = -2
        for o in In:
            if now == -2:
                now = o
            else:
                In_num.append(o-now)
                now = o

        multipliers = []
        total = 0
        for k in range(l-1,-1,-1):
            total += diff_out[k]
            multipliers.append(total)
        for k in range(1,l):
            multipliers[k] += multipliers[k-1]

        
        result = 0
        for p in range(l):
            result += In_num[p] * multipliers[l-1-p]
        result %= 1000000007
        fi.write(f'Case #{i}: {result}\n')