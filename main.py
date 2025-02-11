import random as rn
def choose():
    uc = input("enter number choose the following\n 1.odd\n 2.even\n")
    if(uc=='1'):
        print('you choose odd')
        cc='2'
    else:
        print('you choose even')
        cc=1
    toss(uc,cc)

def toss(uc,cc):
    score = 0
    cscore = 0
    ut = int(input("enter any random number between 1-6: "))
    if (ut>6 or ut<1):
        print("invalid input")
        toss(uc,cc)
    ct = rn.randint(1,6)
    print(ct)
    s = ut+ct
    lis = ['1','2']
    if(s%2==0):
        print("IT'S EVEN")
        if(uc=='2'):
            print("you won the toss\n")
            tuc = input("select what you want to opt\n1.batting\n 2.balling")
            if(tuc=='1'):
                firstBatting()
            else:
                firstcBatting()
        else:
            print("you lost the toss ")
            tcc=rn.choice(lis)
            if(tcc=='1'):
                print("computer is batting first")
                firstcBatting()
            else:
                print("computer choose to ball first")
                firstBatting()
    else:
        print("IT'S ODD")
        if(uc=='1'):
            print("you won the toss\n")
            tuc = input("select what you want to opt\n1.batting\n 2.balling")
            if(tuc=='1'):
                firstBatting()
            else:
                firstcBatting(cscore)    
        else:
            print("you lost the toss ")
            tcc=rn.choice(lis)
            if(tcc=='1'):
                print("computer is batting first")
                firstcBatting()
            else:
                print("computer choose to ball first")
                firstBatting()


def firstBatting():
    score = 0
    while True:
        ru = int(input())
        if(ru>6 or ru<1):
            print("invalid input")
            pass
        chu = rn.randint(1,6)
        print(ru,chu)
        if(ru==chu):
            print("your score\n",score)
            print("you are balling now\n")
            break
        score = score + ru
    secondcBatting(score)

def secondcBatting(score):
    cscore = 0
    while True:
        cr = int(input())
        if(cr>6 or cr<1):
            print("invalid input")
            pass
        cha = rn.randint(1,6)
        print(cr,cha)
        if(cr==cha):
            print("computer score",cscore)
            break
        cscore = cscore + cha
        if(cscore>score):
            print("computer won")
            break
    if(cscore<score):
        print("you won by",score-cscore,"runs")
    else:
        print("computer won by",cscore-score,"runs")        


def firstcBatting():
    cscore = 0
    while True:
        rq = int(input())
        if(rq>6 or rq<1):
            print("invalid input")
            pass
        che = rn.randint(1,6)
        print(rq,che)
        if(rq==che):        
            print("computer score",cscore)
            print("now it's your turn")
            break
        cscore = cscore + che
    secondBatting(cscore)
        
def secondBatting(cscore):
    score = 0   
    while True:
        r = int(input())
        if(r>6 or r<1):
            print("invalid input")
            pass
        ch = rn.randint(1,6)
        print(r,ch)
        if(r==ch):
            print("your score",score)
            break
        score = score + r
        if(score>cscore):
            print("you won")
            break

choose()
