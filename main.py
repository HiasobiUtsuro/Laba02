from decimal import Decimal
from math import factorial
import decimal
# По неизвестной причине простой import decimal не помог избежать ошибки с Decimal, поэтому пришлось импортировать как модуль в целом,
# чтобы использовать округление, так и отдельную функцию

def pi(n):
    P = Decimal(0)
    k = 0
    while k < n:
        P += ((Decimal(-1)**k) * (Decimal(factorial(6 * k))) * (13591409 + 545140134 * k))/((factorial(k)**3) * (factorial(3 * k)) * (640320**(3 * k))*Decimal(640320**3).sqrt())
        k += 1
    P = 12*P
    P = P**(-1)
    return P

n = int(input())
decimal.getcontext().prec = n+1
print (pi(n))
