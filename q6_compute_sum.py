n = int(input("Enter your number here: "))
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
print(sum_digits(n))
