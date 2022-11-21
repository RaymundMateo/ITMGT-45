import math

def savings(gross_pay, tax_rate, expenses):
    if (tax_rate >= 1):
        tax_rate = tax_rate / 100
    return gross_pay - (math.floor(gross_pay * tax_rate) + expenses)
    
print(savings(20000, 10, 5000))