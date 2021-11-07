x, y = map(int, input().split())
r = int(input())

print(x-r, y+r)  # 左上角开始顺时针
print(x+r, y+r)
print(x+r, y-r)
print(x-r, y-r)

