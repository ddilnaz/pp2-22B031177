from time import sleep
from math import sqrt
san = int(input())
uakyt = int(input())
sleep(uakyt/1000)
print(f'Square root of {san} after {uakyt} miliseconds is {sqrt(san)}'.format(san,uakyt))