T = int(input())
with open('C1_sol.txt','w') as fi:
    for i in range(1, T+1):
        r, c, k = map(int, input().split())
        up_down = [0] * c
        row_x = [0] * (r+2)
        record = []
        for j in range(1, r+1):
            if j > k:
                up = 0
                for _ in up_down:
                    if _ < j-k:
                        up += 1
                row_x[j-1] += up + j - k
            row = input()
            record.append(row)
            for n, p in enumerate(row):
                if p == 'X':
                    row_x[j-1] += 1
                elif p == '.':
                    up_down[n] += 1
            if j == k and row_x[j-1] == 0:
                fi.write(f'Case #{i}: 0\n')
                continue
        for _ in up_down:
            up = 0
            if _ < r+1-k:
                up += 1
        row_x[r] += up + r + 1 - k

        up_down = [0] * c
        for j in range(r, 0, -1):
            if j < k:
                down = 0
                for _ in up_down:
                    if _ < k-j:
                        down += 1
                row_x[j-1] += down + k - j
            for n, p in enumerate(reversed(record)):
                if p == '.':
                    up_down[n] += 1
        for _ in up_down:
            down = 0
            if _ < k:
                down += 1
        row_x[r+1] += down + k

        result = min(row_x)
        fi.write(f'Case #{i}: {result}\n')

