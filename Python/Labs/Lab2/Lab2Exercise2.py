#Exercise 2: calculate e up to 10 terms using a factorial function
def factorial(num):
    ans = 1
    for x in range(num):
        ans *= num
        num -= 1
    return ans

e = 1
denominator = 1
for x in range(10):
    print(f'After {x + 1} term(s): e = {e}')
    e += 1/factorial(denominator)
    denominator += 1