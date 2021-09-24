n = int(input())
with open('A1_sol.txt','w') as fi:
    for i in range(1,n+1):
        S = input()
        count = [0] * 26
        for s in S:
            count[ord(s)-65] += 1  # count total
        vowel_max = 0
        conso_max = 0
        vowel_total = 0
        conso_total = 0
        for j in range(26):
            if j+65 in {ord('A'),ord('E'),ord('I'),ord('O'),ord('U')}:
                vowel_total += count[j]
                vowel_max = max(vowel_max, count[j])
            else:
                conso_total += count[j]
                conso_max = max(conso_max, count[j])
        result = min( (conso_total-conso_max)*2+vowel_total, (vowel_total-vowel_max)*2+conso_total )
        fi.write(f'Case #{i}: {result}\n')