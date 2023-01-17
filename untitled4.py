import subprocess
def isint(a):
    try:
        int(a)
        return(True)
    except:
        return(False)
def pidlist():
    o = subprocess.check_output("ps")
    o = o.decode()
    o = o.split('\n')
    a = []
    i = 1
    while i < len(o):
        a.append(o[i])
        i+=1
    i = 0
    o = []
    while i < len(a):
        h = 0
        b = 0
        o.append(0)
        while h < len(a[i]):
            if isint(a[i][h]):
                o[i]=(o[i]*10)+int(a[i][h])
                b = 1
            elif b == 1 and a[i][h]==' ':
                #print('hi')
                break
            h+=1
        i+=1
    o.pop()
    return(o)
