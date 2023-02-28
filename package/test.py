# import calc.fibo
# calc.fibo.fib(1000)
# print(calc.fibo.fib2(1000))

# from calc.fibo import fib, fib2 
# # from fib import * でもimportできるが非推奨
# fib(1000)
# print(fib2(1000))

# import calc
# calc.fibo.fib(1000)
# print(calc.fibo.fib2(1000))
# print(calc.rand.get_random_number(1, 30))

# from calc import rand, fibo
from calc import *
print(rand.get_random_number(1, 30))
fibo.fib(1000)
print(fibo.fib2(1000))

from calc.op import sum
print(sum.summary(1, 2, 3, 4, 5))