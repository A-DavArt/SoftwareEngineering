def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 250
fib_nums = list(fib(n))

print(f"250-е число Фибоначчи: {fib_nums[-1]}")