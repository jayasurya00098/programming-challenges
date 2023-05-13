T = int(input())

for i in range(1, T + 1) :
    N = int(input())
    count = 0
    if N == 0 :
        count = 1
    else :
        while N > 0 :
            N = N//10
            count += 1
    
    print(count)