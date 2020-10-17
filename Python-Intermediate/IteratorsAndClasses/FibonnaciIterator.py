class PapayaWhip:  
    pass           

import fibonacci2
from fibonacci2 import Fib

fib = fibonacci2.Fib(100)          
print (fib)                        
#<fibonacci2.Fib object at 0x7f7594e75ba8>

print (fib.__class__)              
#<class 'fibonacci2.Fib'>

print (fib.__doc__ )               
#iterator that yields numbers in the Fibonacci sequence

fib1 = fibonacci2.Fib(100)
fib2 = fibonacci2.Fib(200)

print (fib1.max)
#100
print (fib2.max)
#200

for n in Fib(1000):
     print(n, end=' ')
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987