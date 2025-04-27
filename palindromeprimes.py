import time
import math

primes = [2]

def sieve_of_eratosthenes(n):
    p = 2
    while p <= int(math.sqrt(n))+1:
        isprime = True
        for i in range(0,len(primes)):
            if p%primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
        p = p + 1

def is_prime(n):
    if n==1:
        return False
    if n in primes:
        return True
    else:
        i=0
        p = primes[i]
        while p*p <= n:
            if n%p == 0:
                return False
            i = i + 1
            if i< len(primes):
                p = primes[i]
            else:
                p=p+1
    return True

def get_first_pallindrome(n):
    str_num = str(n)
    if len(str_num)%2==0:
        return pow(10,len(str_num))+1
    elif n<9:
        return n+1
    elif n==9:
        return 11
    else:
        half = len(str_num)//2
        prefix=str_num[:half+1]
        suffix = prefix[::-1]
        return int(prefix+suffix[1:])


def get_next_palindrome(n):
    str_num = str(n)
    if len(str_num)%2==0:
        return pow(10,len(str_num))+1
    elif n<9:
        return n+1
    elif n==9:
        return 11
    else:
        half = len(str_num)//2
        prefix=str_num[:half+1]
        prefix = str(int(prefix)+1)
        suffix = prefix[::-1]
        r= int(prefix+suffix[1:])
        if prefix[0] in ['2','6','8']:
            r =  (int(prefix[0])+1)*pow(10,len(str(r))-1)+(int(prefix[0])+1)
        elif prefix[0] in ['5']:
            r =  (int(prefix[0])+2)*pow(10,len(str(r))-1)+(int(prefix[0])+2)
        elif prefix[0] in ['4']:
            r =  (int(prefix[0])+3)*pow(10,len(str(r))-1)+(int(prefix[0])+3)
        return r


m = int(input("Enter the smaller number: "))
n = int(input("Enter the larger number: "))
start_time = time.time()
result =[]
sieve_of_eratosthenes(n)
p=m
if str(m) == str(m)[::-1]:
    if is_prime(m):
        result.append(m)
else:
    p = get_first_pallindrome(m)
while p<n:
    p = get_next_palindrome(m)
    if p<=n:
        if is_prime(p):
            result.append(p)
    if p==m:
        break
    m=p
end_time = time.time()
print(f"Total special numbers: {len(result)}")
if len(result)<=6:
    print_result= result
else:
    print_result= result[:3]+result[-3:]
print(f"Special numbers: {print_result}")
print(f"Time taken: {end_time - start_time} seconds")
