memo = {}
memo[1] = 2
def pyramid(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = pyramid(n-1)+2*n+n-1
        return memo[n]

testcases = int(input())
for i in range(testcases):
    n = int(input())
    h = 0
    pyramids = 0
    while True:
        h += 1
        if pyramid(h) <= n < pyramid(h+1):
            n -= pyramid(h)
            h = 0
            pyramids += 1
        if n < 2:
            break
    print(pyramids)
        