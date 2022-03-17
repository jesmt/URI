n = int(input())
for i in range(n):
    s = input().split()
    c = len(s)
    sum = 0

    for j in range(1, c):
        sum += int(s[j])
    #print("sum", sum)

    media = sum / (c-1)
    #print("media", media)

    count = 0
    for z in range(1, c):
        if int(s[z]) > media:
            count += 1
    """
    c - 1    ------>   100%
    count    ------>   x %
    """
    x = (count * 100) / (c - 1)

    print("%.3f%%" %x)

