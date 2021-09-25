T = int(input())
with open('A_sol.txt','w') as fi:
    for i in range(1, T+1):
        n, m = map(int, input().split())
        models = input().split()
        change = {}
        all_changed = False
        current = {}
        for model in models:
            if not current.get(model):
                current[model] = 1
                change[model] = 1
            else:
                current[model] += 1
                change[model] += 1

        count = 0
        change2 = {}
        for _ in range(n):
            line = input().split()
            for l in line:
                if current.get(l):
                    current[l] -= 1
                elif current.get(l) == 0:
                    count += 1
                    del current[l]
                else:
                    count += 1
            
            if not all_changed:
                for c in current:
                    if change[c] - current[c] <= 0:
                        count -= change[c]
                        change[c] = 0
                    else:
                        change[c] -= current[c]
                        count -= current[c]

            goal = {}
            for l in line:
                if not goal.get(l):
                    goal[l] = 1
                else:
                    goal[l] += 1
            current = goal
