from collections import defaultdict 


def fibo(n):

    cache=defaultdict(int)
    cache[1]=1

    if n==0:
        return 0
    if cache[n]:
        return cache[n] 
    
    def find_fib(n):
        
        n1=find_fib(n-1)
        n2=find_fib(n-2)
        cache[n]=n1 +n2 
        return cache[n]
    
    return find_fib(n)


if __name__ == '__main__':
    n=int(input("Enter the number :"))
    print(f"Fibonacci({n}) = {fibo(n)}")
    