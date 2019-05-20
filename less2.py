def odometer (N):
    oksana = 0
    for i in range (len(N)):
        if i == 0 or i%2 == 0:
            oksana += N[i]
    return oksana
