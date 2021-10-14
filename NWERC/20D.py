from random import randint
n = int(input())
found = 0
while found < n:
    print(0, 0, flush=True)
    d1 = int(input())
    if d1 == 0:
        found += 1
    else:
        print(1, 0, flush=True)
        d2 = int(input())
        if d2 == 0:
            found += 1
        else:
            if d2 >= d1:  # 在0头顶
                print(0, int(d1**0.5), flush=True)
                goal = int(input())
                found += 1
            else:  # 在右边
                x = (d1 - d2 + 1)//2
                if x <= 10**6:
                    print(int(x), 0, flush=True)
                    y0 = int(input())
                    if y0 == 0:
                        found += 1
                        continue
                    print(int(x), int(y0**0.5), flush=True)
                    goal = int(input())
                else:
                    goal = 1
                domain = [1, 10**6-1]
                while goal != 0:
                    x = randint(domain[0], domain[1])
                    print(int(x), 0, flush=True)
                    d1 = int(input())
                    if d1 == 0:
                        break
                    else:
                        print(int(x-1), 0, flush=True)
                        d2 = int(input())
                        if d2 == 0:
                            break
                        else:
                            print(int(x+1), 0, flush=True)
                            d3 = int(input())
                            if d3 == 0:
                                break
                            else:
                                if d2 == d3:  # 在x头顶
                                    print(x, int(d1**0.5), flush=True)
                                    goal = int(input())
                                elif d2 > d1:  # 在右边
                                    domain[0] = x
                                    z = (d2 - d1 - 1)//2
                                    if x + z > 10**6:
                                        continue
                                    print(int(x+z), 0, flush=True)
                                    y = int(input())
                                    if y == 0:
                                        break
                                    print(int(x+z), int(y**0.5), flush=True)
                                    goal = int(input())
                                elif d3 > d1:  # 在左边
                                    domain[1] = x
                                    z = (d3 - d1 - 1)//2
                                    if x - z < 0:
                                        continue
                                    print(int(x-z), 0, flush=True)
                                    y = int(input())
                                    if y == 0:
                                        break
                                    print(int(x-z), int(y**0.5), flush=True)
                                    goal = int(input())
                                else:
                                    continue
                found += 1