for i in range(1,101):
    # print(i)
    if (str(i).find('7') is -1) and (i % 7 !=0):
        print(i)
        i = i + 1
