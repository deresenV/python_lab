import ctypes

func_c = ctypes.CDLL('calculate.so')


func_c.calculate_primes.argtypes = [ctypes.c_int]
func_c.calculate_primes.restype = ctypes.POINTER(ctypes.c_bool)

def primes(n):
    ptr = func_c.calculate_primes(n)
    if not ptr:
        print('err')
    primes_bool=[ptr[i] for i in range(n + 1)]
    return primes_bool

def goldbach(primes_array,n,m):
    for k in range(n,m+1):
        finish_x, finish_y = 0, 0
        if k%2==0:
            count=0
            for x in range(2,m//2+1):
                for y in range(2,m+1):
                    if (primes_array[x] and primes_array[y]) and x+y==k:
                        count+=1
                        if count==1:
                            finish_x = x
                            finish_y = y
            print(k,count,finish_x,finish_y)

def main():
    n,m=map(int,input().split())
    prime_array=primes(m)
    goldbach(prime_array,n,m)


main()