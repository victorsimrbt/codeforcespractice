'''
greedy algorithm, take away nine until num left is equal to numbers of spaces left or remainder
if former, fill with 1s 
otherwise, put remainder


'''
memo = {}
def max_num(n,length):
    ans = ""
    if (n,length) in memo:
        #print("memod")
        return memo[(n,length)]
    if length == 1:
        if n <= 9:
            ans += str(n)
            return ans
        else:
            return -1
    if length == 0:
        return -1
    for digit in range(9,0,-1):
        next_digit = int(max_num(n-digit,length-1))
        if next_digit >= 0:
            ans += str(digit)
            ans += str(next_digit)
            memo[(n,length)] = ans
            return ans
    return -1

def min_num(max_num):
    nums = list(map(int,list(max_num)))
    nums = nums[::-1]
    minimum = []
    zeros = 0
    for num in nums:
        if num != 0:
            minimum.append(str(num))
        else:
            zeros += 1
    for i in range(zeros):
        minimum.insert(1,"0")
    return ''.join(minimum)
        

m,s = map(int,input().split())
maximum = max_num(s,m)
if maximum == -1:
    print(-1,-1)
    exit()
minimum = min_num(maximum)
print(minimum,maximum)