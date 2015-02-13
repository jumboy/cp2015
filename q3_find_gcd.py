def gcd(m,n):
    if m%n == 0:
        return "The greatest common divisor is: " + str(n)
    else:
        return gcd(n,m%n)
print(gcd(24,16))
print(gcd(255,25))
