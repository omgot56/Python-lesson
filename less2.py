def odometer(N):
    oksana = 0
    now_time = 0
    for i in range (len(N)):
        if i == 0:
            now_time = N[i+1]
            oksana += now_time*N[i]
        elif i > 1 and i % 2 == 0:
            now_time = N[i-1]
            now_time =  N[i+1] - now_time
            oksana += now_time * N[i]
    return(oksana)
