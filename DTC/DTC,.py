import os
import time
def reset():
    a=open('list.txt','w')
    a.close()
    a=open('log.txt','w')
    a.close()
    l='all reset'
    pri1(l)
    input('Press Enter to go back')
    ghg
def pri(a):
    s=''
    sa=0
    for i in a:
        os.system('cls')
        s=s+a[sa]
        print(s)
        time.sleep(0.0000001)
        sa=sa+1
def pri1(a):
    s=''
    sa=0
    for i in a:
        os.system('cls')
        s=s+a[sa]
        print(s)
        time.sleep(0.25)
        sa=sa+1

q=''
ans=''
ss=['enter root','Enter starting zone','Enter ending zone','Enter all stands in roots','Enter total time','Enter total distance']
class don:    
    def find(self):
        os.system('cls')
        wee=open('log.txt','r')
        we=input('?Enter root')
        
        w=wee.readlines()
        s=0
        qx=''
        for i in w:
            
            if i==str(we)+'\n':
                se=0
                for j in range(6):
                    qwe=str(ss[se]+':-'+w[s])
                    qx=qx+qwe+'\n'
                    se=se+1
                    s=s+1
                pri(qx)
            else:
                s=s+1
        input(' SERCH IS STOP --Press Enter to main menu')
        ghg
    def creat(self,A):
        f=open('log.txt','a+')
        xc='WELCOM \n'+str(A)
        pri1(xc)
        input('Press Enter to start')
        print('''1|Creating
2|Deleting''')
        ans1=int(input('enter your option'))
        if ans1==1:
            os.system('cls')
            root=''
            input(':---press enter to start creating list')
            root=(input('enter root'))   
            ab=open('list.txt','r')
            aa=ab.readlines()
            ab.close()
            aa.append(root)
            ab=open('list.txt','w')
            for i in aa:
                ab.write(i)
                ab.write('\n')
            ab.close()

            f.write(str(root))
            f.write('\n')
            q1=input('Enter starting zone')
            f.write(str(q1))
            f.write('\n')
            q2=input('Enter ending zone')
            f.write(str(q2))
            f.write('\n')
            q3=input('Enter all stands in roots ')
            f.write(str(q3))
            f.write('\n')
            q4=input('Enter total time ')
            f.write(str(q4))
            f.write('\n')
            q5=input('Enter total distance ')
            f.write(str(q5))
            f.write('\n')
            f.close()
            input('Press Enter to go back')
            huh
        else:
            os.system('cls')
            
            oo=[]
            x=input('enter root')

            d=open('log.txt','a+')
            z=0
            c=d.readlines()
            for i in c:
                if x==i:
                    for l in range(7):
                        c.pop(z)
                    
                else:
                    s=s+1
                    oo.append(i)
            d.close()
            h=open('log.txt','w')
            for i in c:
                h.writelines(i)
                h.write('\n')
            h.close()
            gh
    def up(self):
        
        while True:
            ax=input('Enter your name:--')
            e=input('enter login password or reset password:--')
            if e=='123':
                self.creat(ax)
                break
            elif e=='clsall':
                reset()
            else:
                continue
        
    def goo(self):
        print ('ALL ROOTS RECORDS PRESENT OR NOT PRESENT')
        A=open('list.txt','r')
        aq=A.readlines()
        asd=''
        
        for i in aq:
            asd=asd+str(i)
        A.close()
        pri1(asd)
        input('Press Enter to go back')
        
def home():
    os.system('cls')
    a=('''
DDDDDDDDDDDDDDD  TTTTTTTTTTTTTTTT CCCCCCCCCCCCCCCC
DDDDDDDDDDDDDDD  TTTTTTTTTTTTTTTT CCCCCCCCCCCCCCCC
DD           DD        TTTT       CCC
DD           DD        TTTT       CCC
DD           DD        TTTT       CCC
DD           DD        TTTT       CCC
DDDDDDDDDDDDDDD        TTTT       CCCCCCCCCCCCCCCC
DDDDDDDDDDDDDDD        TTTT       CCCCCCCCCCCCCCCC''')
    

    pri(a)
    print('''
    1|Find  By root
    2|User login
    3|About all recodes''')
    print(q)









aa= don()
home()
while True:
    try:
        ans=int(input('enter your option'))
        if ans in (1,2,3):
            if ans==1:
                aa.find()
            elif ans==3:
                aa.goo()

            else:
                
                aa.up()

        else:
            q=('''"ENTER ONE OF THIS "''')
            home()
            continue 
        break 
    except:
        q=('''"ENTER ONLY INT "''')

        home()
        continue


