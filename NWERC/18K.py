
n = int(input())
s = input()
dp = []
for _ in range(n):
    dp.append([0]*n)
for i in range(n):
    dp[i][i] = 1

for k in range(1,n):  # 斜对角从内向外 第k+1对角线
    for i in range(n-k):  # i从0到n-1-k，j从k到n-1 j=i+k
        j = i+k
        mini = n
        for m in range(i,j):
            mini = min(dp[i][m]+dp[m+1][j], mini)
        string = s[i:j+1]*2
        num = string.find(s[i:j+1],1)
        if num < k+1:
            mini = min(dp[i][i+num-1], mini)
        dp[i][j] = mini

print(dp[0][n-1])
