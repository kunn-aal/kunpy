
def great(*numero):
    s=numero[0]
    for i in range(1,len(numero)):
        if numero[i]>s:
            s=numero[i]

    print(s,"is the greatest")
great(1,2,3,10,5,6)
