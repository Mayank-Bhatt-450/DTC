import os
import random
import time
def cls():
    os.system('cls')
    print '-------------------------------------------------------------------------------'
    print '  ENCRYPT-DECRYPT                                  '
    print '-------------------------------------------------------------------------------'
    print
    print
l=[]
for i in range(65,91):
    l.append(chr(i))
l.append('-')
l.append('@')
l.append('?')
l.append('!')
for i in range(97,123):
    l.append(chr(i))
for i in range(48,58):
    l.append(chr(i))
def code(x):
    x=str(x)
    for i in range(11,77):
        if x==l[i-11]:
            x=str(i)  
    return x

def decode(x):
    try :
        x=int(x)
        return l[x-11]
    except :
        return x
ch=['123456','123546','123645','132456','132546','132645','142356','142536','142635','152346','152436','152634','162345','162435','162534']
a1=l[:11]
a2=l[11:22]
a3=l[22:33]
a4=l[33:44]
a5=l[44:55]
a6=l[55:66]
a=[a1,a2,a3,a4,a5,a6]
mll=['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l']
def enc(z):
    z=str(z)
    ft=random.randint(0,14)
    f=ch[ft]
    t=''
    for i in f :
        t=t+str(int(i)-1)
    fa=t[:2]
    fb=t[2:4]
    fc=t[4:]
    k=''
    for i in z :
        if i in a[int(fa[0])] :
            m=0
            for j in a[int(fa[0])] :
                if i==j :
                    i=a[int(fa[1])][m]
                    break
                m=m+1
        elif i in a[int(fb[0])] :
            m=0
            for j in a[int(fb[0])] :
                if i==j :
                    i=a[int(fb[1])][m]
                    break
                m=m+1
        elif i in a[int(fc[0])] :
            m=0
            for j in a[int(fc[0])] :
                if i==j :
                    i=a[int(fc[1])][m]
                    break
                m=m+1
        elif i in a[int(fa[1])] :
            m=0
            for j in a[int(fa[1])] :
                if i==j :
                    i=a[int(fa[0])][m]
                    break
                m=m+1
        elif i in a[int(fb[1])] :
            m=0
            for j in a[int(fb[1])] :
                if i==j :
                    i=a[int(fb[0])][m]
                    break
                m=m+1
        elif i in a[int(fc[1])] :
            m=0
            for j in a[int(fc[1])] :
                if i==j :
                    i=a[int(fc[0])][m]
                    break
                m=m+1
        k=k+i
    ft=mll[ft]
    k=ft+k
    return k
  
                
        
    
    
def dec(z):
    ft=z[0]
    z=z[1:]
    tem=0
    for i in mll :
        if ft==i :
            ft=tem
            break
        tem=tem+1
    f=ch[ft]
    t=''
    for i in f :
        t=t+str(int(i)-1)
    fa=t[:2]
    fb=t[2:4]
    fc=t[4:]
    k=''
    for i in z :
        if i in a[int(fa[0])] :
            m=0
            for j in a[int(fa[0])] :
                if i==j :
                    i=a[int(fa[1])][m]
                    break
                m=m+1
        elif i in a[int(fb[0])] :
            m=0
            for j in a[int(fb[0])] :
                if i==j :
                    i=a[int(fb[1])][m]
                    break
                m=m+1
        elif i in a[int(fc[0])] :
            m=0
            for j in a[int(fc[0])] :
                if i==j :
                    i=a[int(fc[1])][m]
                    break
                m=m+1
        elif i in a[int(fa[1])] :
            m=0
            for j in a[int(fa[1])] :
                if i==j :
                    i=a[int(fa[0])][m]
                    break
                m=m+1
        elif i in a[int(fb[1])] :
            m=0
            for j in a[int(fb[1])] :
                if i==j :
                    i=a[int(fb[0])][m]
                    break
                m=m+1
        elif i in a[int(fc[1])] :
            m=0
            for j in a[int(fc[1])] :
                if i==j :
                    i=a[int(fc[0])][m]
                    break
                m=m+1
        k=k+i
    return k

cls()
while True :
    cls()
    print '  Choose An Option From Below -----'
    print
    print
    print'''
    1. Encrypt

    2. Decrypt
'''
    while True :
        print
        ask=raw_input('  Enter Your Choice Number  :  ')
        if ask=='1' or ask=='2' :
            break
    cls()
    if ask=='1' :
        print '  Data Encryptor -----'
        print
        while True :
            print
            data=raw_input('  Enter The Data To Encrypt  :  ')
            sp=' '*len(data)
            if data!='' or sp!=data :
                break
        print
        print
        print '  Encrypting Data ',
        for i in range(5) :
            time.sleep(0.4)
            print '.',
        ed=enc(data)
        print
        print
        print
        print '  Encypted Data  :  ',
        print ed
    if ask=='2' :
        print '  Data Decryptor -----'
        print
        while True :
            print
            data=raw_input('  Enter The Data To Decrypt  :  ')
            sp=' '*len(data)
            if data!='' or sp!=data :
                break
        print
        print
        print '  Decrypting Data ',
        for i in range(5) :
            time.sleep(0.4)
            print '.',
        print
        print
        try :
            dd=dec(data)
            print 
            print '  Encypted Data  :  ',
            print dd
        except :
            print
            print '  Error While Decrypting Data'
            print
            print '  *** Incorrect Data Form ***'
    print
    print
    print '  Press Enter For Home ',
    raw_input()     
    
