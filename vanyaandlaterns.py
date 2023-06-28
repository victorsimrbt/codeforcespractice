n,length = map(int,input().split())
lamps = list(map(int,input().split()))
lamps.sort()
# check if area is fully lit
# check if left and right pointers are correct
# repeat until both left and right pointers make area fully lit
 
def fully_lit(r):
    prev_end = 0
    #prev_start = 1000000000000
    for i in range(len(lamps)):
        lamp = lamps[i]
        start,end = lamp-r,lamp+r
        #print("YO",start,end,prev_end)
        if start <= prev_end:
            pass
        else:
            return False
        prev_end = end
        #prev_start = start
    if end < length:
        return False
    return True

# print(fully_lit(200))
l =  0
r = length
while abs(l - r) >= 0.000000001:
    mid = (l+r)/2
    #print(l,r,mid,fully_lit(mid))
    if r == mid or l == mid:
        #print("whoops")
        break
    if fully_lit(mid):
        #print("lit")
        r = mid
    else:
        #print("unlit")
        l = mid
print("{0:.10f}".format(mid))