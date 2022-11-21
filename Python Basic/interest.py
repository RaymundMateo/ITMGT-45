import math

def interest(principal, rate, periods):
    if rate >= 1:
        rate = rate / 100
    return math.floor(((rate * periods) * principal) + principal)

print(interest(10000, 10, 6))