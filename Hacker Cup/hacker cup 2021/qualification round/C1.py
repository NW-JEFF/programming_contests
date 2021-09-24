import heapq
t = int(input())
with open('C1_sol.txt','w') as fi:
    for i in range(1,t+1):
        n = int(input())
        C = [None]+list(map(int, input().split()))
        D = {j:set() for j in range(1,n+1)}
        for _ in range(n-1):
            tunnel = list(map(int,input().split()))
            D[tunnel[0]].add(tunnel[1])
            D[tunnel[1]].add(tunnel[0])
        
        gold = C[1]
        if not D[1]:
            fi.write(f'Case #{i}: {gold}\n')
        else:
            gold_in_courses = []
            for start in D[1]:
                finished_course = []
                course = [C[start], 1, start]  # course[0] records gold collected so far
                process = [course]
                while process:
                    p = process.pop()
                    bifurcate = D[p[-1]]-set([p[-2]])
                    if not bifurcate:  # the course ends
                        finished_course.append(p)
                        continue
                    for b in bifurcate:
                        new_course = p+[b]
                        new_course[0] += C[b]
                        process.append(new_course)
                max = 0
                for c in finished_course:
                    if c[0] > max:
                        max = c[0]
                gold_in_courses.append(max)
            if len(gold_in_courses) == 1:
                result = gold + gold_in_courses[0]
                fi.write(f'Case #{i}: {result}\n')
            else:
                ans = heapq.nlargest(2, gold_in_courses)
                result = sum(ans) + gold
                fi.write(f'Case #{i}: {result}\n')