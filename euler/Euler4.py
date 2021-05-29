
def isPalindrome(n: int) -> bool:
    if len(str(n)) == 1: return True
    res = True
    num = str(n)
    limit = int(len(num)/2)
    for j in range(0,limit):
        if num[j] != num[len(num) - (j + 1)]:
            return False
    return True

limit: int = 1000
def palindromes(limit: int) -> list:
    ret: lst = []
    for j in range(1,limit):
        for k in range(1,limit):
            if isPalindrome(j*k):
                ret.append(j*k)
            else: continue
    return ret

pals = palindromes(1000)
print('palindromes', pals)
print('max palindrome is', max(pals))
