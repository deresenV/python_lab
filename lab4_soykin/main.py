import ctypes

func_c = ctypes.CDLL('calculate.so')


func_c.calculate_primes.argtypes = [ctypes.c_int]
func_c.calculate_primes.restype = ctypes.POINTER(ctypes.c_bool)

def primes(n):
    ptr = func_c.calculate_primes(n)
    primes=[]
    if not ptr:
        print('err')
    for i in range(2, n+1):
        if ptr[i]:
            primes.append(i)
    return primes

def goldbach(primes_array,n,m):
    pass


def main():
    n,m=map(int,input().split())
    prime_array=primes(m)


main()