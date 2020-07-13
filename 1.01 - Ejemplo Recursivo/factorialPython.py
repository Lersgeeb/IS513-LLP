#Comment by line
'''

Comment Multiple Line

'''

def factorial(n):
    if n < 2: return 1
    return n * factorial(n-1)

n=5
print('el factorial de %d es %d'%(n,factorial(n)))