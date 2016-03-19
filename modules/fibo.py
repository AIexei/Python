def fibo(value):
    current, next = 0, 1

    for i in range(value):
        yield current
        current, next = next, current + next