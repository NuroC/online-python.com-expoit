import os
import shutil
import socket
import subprocess
import math
if os.path.exists('/tmp/lol.py'):
    os.system('ps')
    print('already jammed!')
    print(socket.gethostname())
    quit()
denied = []
code = []
def get_size(start_path = '.'):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du','-sh', start_path]).split()[0].decode('utf-8')
    return(total_size)
def bytemake(a):
    if a > 1000:
        a = a/1000
        a = math.floor(a*100)/100
        if a > 1000:
            a=a/1000
            a = math.floor(a*100)/100
            if a > 1000:
                a=a/1000
                a = math.floor(a*100)/100
                return(str(a)+' GB')
            return(str(a)+' MB')
        return(str(a)+' KB')
    return(str(a)+' B')
def dircheck(path,h,i,a,end):
    try:
        os.scandir(path+'/'+a[i])
        if h == i:
            print('##>',a[i],' --- DIR  '+get_size(path+'/'+a[i]),end=end)
        else:
            print('   ',a[i],' --- DIR  ',end=end)
    except NotADirectoryError:
        if h == i:
            print('##>',a[i],'  '+get_size(path+'/'+a[i]),end=end)
        else:
            print('   ',a[i],'  ',end=end)
    except PermissionError:
        if h == i:
            print('##>',a[i],' -X- DIR #LOCKED#',end=end)
        else:
            print('   ',a[i],' -X- DIR',end=end)
    except:
        if h == i:
            print('##>',a[i],' ???',end=end)
        else:
            print('   ',a[i],' ???',end=end)
flag = 0
num = 0
path = '/'
def cls():
    print('\n'*20)
h = 0
while 1:
    cls()
    try:
        entries = os.scandir(path)
    except NotADirectoryError:
        print('ERR DIR NOT FOUND')
        ret = path[path.rfind('/')+1:]
        if not path == '/':
            path = path[:path.rfind('/')]
        entries = os.scandir(path)
        a = []
        for entry in entries:
                a.append(entry.name)
        print(a)
        try:
            h = a.index(ret)
        except ValueError:
            h = 0
            print('h')
        entries = os.scandir(path)
    except PermissionError:
        denied.append(path)
        print('ERR UNAUTHORIZED')
        ret = path[path.rfind('/')+1:]
        if not path == '/':
            path = path[:path.rfind('/')]
        entries = os.scandir(path)
        a = []
        for entry in entries:
                a.append(entry.name)
        print(a)
        try:
            h = a.index(ret)
        except ValueError:
            h = 0
            print('h')
        entries = os.scandir(path)
    except FileNotFoundError:
        print('ERR SESSION_EXPIRED')
        ret = path[path.rfind('/')+1:]
        if not path == '/':
            path = path[:path.rfind('/')]
        entries = os.scandir(path)
        a = []
        for entry in entries:
                a.append(entry.name)
        #print(a)
        try:
            h = a.index(ret)
        except ValueError:
            h = 0
            print('h')
        entries = os.scandir(path)
    a = []
    for entry in entries:
            a.append(entry.name)
            #print(entry.name,end=', ')
            #print(entry)
    if flag == 1:
        print('file captured!')
    elif flag == -1:
        print('file unavailable...')
    elif flag == 2:
        print(code)
    flag=0
    print('Prim file Nav 1.1')
    print(path,'\n')
    i = 0
    if len(a) < 50:
        if len(a) < 30:
            end = '\n'
        else:
            end = ' '
        while i < len(a):
            dircheck(path,h,i,a,end)
            i+=1
            if len(a) > 30:
                if end == ' ':
                    end = '  '
                elif end == '  ':
                    end = '\n'
                else:
                    end = ' '
    else:
        print('Item '+str((h+1))+' of '+str(len(a))+'.')
        dircheck(path,h,h-1,a,end)
        dircheck(path,h,h,a,end)
        dircheck(path,h,h+1,a,end)
    go = input()
    if go == '':
        go = ' '
    if go == 's':
        if h >= len(a)-1:
            h = 0
        else:
            h+=1
    elif go == 'w':
        if h <= 0:
            h = len(a)-1
        else:
            h-=1
    elif go == 'd':
            path+='/'+a[h]
            h = 0
    elif go == 'a':
        ret = path[path.rfind('/')+1:]
        if not path == '/':
            path = path[:path.rfind('/')]
        entries = os.scandir(path)
        a = []
        for entry in entries:
                a.append(entry.name)
        print(a)
        try:
            h = a.index(ret)
        except ValueError:
            h = 0
            print('h')
    elif go == 'x':
        print(denied)
    elif go == 'r':
        try:
            ftemp = open(path+'/'+a[h],'r')
            code.append([line.split(',')for line in ftemp.readlines()])
            ftemp.close()
        except FileNotFoundError:
            flag = -1
        else:
            flag = 1
    elif go == 'p':
        flag = 2
    elif go == 'c':
        code = []
    elif go == 't':
            i = 0
            while 1:
                try:
                    f = open(path+'/'+'LOL'+str(i)+'.txt','x')
                except:
                    print('ERR at file no. '+str(i))
                    break
                if i%1000 == 0:
                    print(i)
                i+=1
    elif go == 'q':
        statvfs = os.statvfs('/')
        print('File system size:  '+str(statvfs.f_frsize * statvfs.f_blocks)+'bytes with '+str(statvfs.f_frsize * statvfs.f_bfree)+' free')
    elif go[0] == 'i':
        name = go[1:]
        try:
            os.mkdir(path+'/'+name)
        except:
            print('Whoops')
    elif go == 'o':
        print('1/8')
        if not os.path.exists(path+'/'+a[h]+'_1'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_1')
        print('2/8')
        if not os.path.exists(path+'/'+a[h]+'_2'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_2')
        print('3/8')
        if not os.path.exists(path+'/'+a[h]+'_3'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_3')
        print('4/8')
        if not os.path.exists(path+'/'+a[h]+'_4'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_4')
        print('5/8')
        if not os.path.exists(path+'/'+a[h]+'_5'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_5')
        print('6/8')
        if not os.path.exists(path+'/'+a[h]+'_6'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_6')
        print('7/8')
        if not os.path.exists(path+'/'+a[h]+'_7'):
            shutil.copytree(path+'/'+a[h],path+'/'+a[h]+'_7')
        print('8/8 Done!')
    elif go[0]=='m':
        name = go[1:]
        try:
            shutil.move(path+'/'+a[h],path+'/'+name+'/'+a[h])
        except:
            print('Whoops')
    elif go=='l':
        shutil.rmtree(path+'/'+a[h])
    elif go == 'y':
        file = open(path+'/'+'lol.py','x')
        file = open(path+'/'+'lol.py','a')
        file.write('i = 0\n')
        #file.write('print("hi")\n')
        file.write('while 1:\n')
        file.write('    file = open("lol"+str(i)+".txt","x")\n')
        #file.write(' file.close()\n')
        file.write('    i = i + 1\n')
        file.close()
    elif go[0] == '?':
        os.system(go[1:])
        contin = input()
        while contin[0]=='?':
            os.system(contin[1:])
            contin = input()
    elif go == 'e':
        os.system('python3 '+path+'/lol.py')
        path = '/'
        h = 0
    elif go[0] == '!':
        exec(go[1:])
        contin = input()
        while contin[0]=='!':
            exec(contin[1:])
            contin = input()
