
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # for i in range(1:x+1)
    # sum is not equal n
    myList = []
    xList = [0]
    yList = [0]
    zList = [0]

    for i in range(x+1):
        xList.append(i)
        for j in range(y+1):
            yList.append(j)
            for k in range(z+1):
                zList.append(k)
                myList.append([xList[-1],yList[-1],zList[-1]])
                if xList[-1] + yList[-1] + zList[-1] == n:
                    del myList[-1]




  print(myList)