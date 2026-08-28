#a)
def catalan(n):
    if n ==0:
        return 1
    else:
        return (4*n - 2) * catalan(n-1) // (n+1)
#b)
c_100 = catalan(100)
print(c_100)
#c)
def g(m,n):
    if n == 0:
        return m
    else:
        return g( n, m % n )
#d)
print( g(108,192))
