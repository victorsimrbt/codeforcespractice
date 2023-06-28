def len_substrings(string_len,min_substring_len):
    ans = 0
    for substring_len in range(min_substring_len,string_len+1):
        #print(string_len,substring_len,string_len-(substring_len-1))
        ans += string_len-(substring_len-1)
    return ans

print(len_substrings(3,1))

testcases = int(input())
for i in range(testcases):
    n,k,q = map(int,input().split())
    len_holiday = {i:0 for i in range(-1,n)}
    temps = list(map(int,input().split()))
    for x in range(n):
        if temps[x] <= q:
            len_holiday[x] = len_holiday[x-1] + 1
    values = list(len_holiday.values())
    #print(values)
    vals = [values[i] for i in range(len(values)) if values[i] != 0 and (i == len(values)-1 or values[i+1] == 0)]
    #print(vals)
    ans = 0
    for consecutive in vals:
        ans += len_substrings(consecutive,k)
    print(ans)