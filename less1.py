def squirrel (N):
    m = 1
    for i in range(1, N+1):
        m *= i
    return int(str(m)[0])
