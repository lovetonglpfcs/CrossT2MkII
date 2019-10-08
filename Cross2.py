from random import randint
from os import system

#Set ค่า 0
def init(CT,N):
    for r in range(5):
        CT.append([])
        N.append([])
        for c in range(5):
            CT[r].append([])
            CT[r][c]=0
            N[r].append([])
            N[r][c]=0
    menu()

#เลือกเมนูเพื่อลง R C
def menu():
    global Option1,Option2
    system('cls') #cmd only.
    print("="*27)
    print(" 0.To Exit Program.")
    print(" 1.Sex")
    print(" 2.Pay-type")
    print(" 3.Education")
    print(" 4.Age group")
    print("="*27)
    Option1 = 6
    while not(Option1 > -1 and Option1) < 5:
        Option1 = int(input("Enter Option1 : "))
    Option2 = Option1
    while Option1 != 0 and (Option1 == Option2 or Option2 < 0 or Option2 > 4):
        Option2 = int(input("Enter Option2 : "))
    

def enter(A):
    for r in range(55):
        A.append([])
        for c in range(5):
            A[r].append([])
            #A[r][c]=int(input("Enter data : ")) เนื่องจากมีจำนวนเยอะ ใส่ค่าไม่ไหว
            if c == 0: #Sex
                A[r][c]=randint(0,1)
            elif c == 1: #Pay-type
                A[r][c]=randint(0,2)
            elif c == 2: #Education
                A[r][c]=randint(0,4)
            elif c == 3: #Age Group 
                A[r][c]=randint(20,60)
                if A[r][c] < 30:
                    A[r][c]=0
                elif A[r][c] < 50:
                    A[r][c]=1
                else:
                    A[r][c]=2
            elif c == 4: # of day Absent
                A[r][c]=randint(0,30)
            

def calc(CT,N):
    global Option1,Option2,RMAX,CMAX
    for r in range(55):
        ROW = A[r][Option1]
        COL = A[r][Option2]
        CT[ROW][COL]=CT[ROW][COL]+A[r][4]
        N[ROW][COL]=N[ROW][COL]+1
        if ROW+1 > RMAX:
            RMAX = ROW+1
        if COL+1 > CMAX:
            CMAX = COL+1
    for r in range(RMAX):
        for c in range(CMAX):
            if CT[r][c] > 0:
                CT[r][c]=CT[r][c]//N[r][c]

def report(CT):
    global Option1,Option2,RMAX,CMAX
    print("\nAverage of days absent.")
    print("="*((CMAX*5)+11))
    print(f"|{Heading[Option2]:>9}|",end="")
    for c in range(CMAX):
        print(f"{c+1:>4}|",end="")
    print()
    print(f"|{Heading[Option1]:>9}|",end="")
    for c in range(CMAX):
        print(f"{' ':>4}|",end="")
    print()
    print("="*((CMAX*5)+11))
    for r in range(RMAX):
        print(f"|{r+1:>9}|",end="")
        for c in range(CMAX):
            print(f"{CT[r][c]:>4}|",end="")
        print()
    print("="*((CMAX*5)+11))
    print("\nStaff Number.") # ตาราง 2
    print("="*((CMAX*5)+11))
    print(f"|{Heading[Option2]:>9}|",end="")
    for c in range(CMAX):
        print(f"{c+1:>4}|",end="")
    print()
    print(f"|{Heading[Option1]:>9}|",end="")
    for c in range(CMAX):
        print(f"{' ':>4}|",end="")
    print()
    print("="*((CMAX*5)+11))
    for r in range(RMAX):
        print(f"|{r+1:>9}|",end="")
        for c in range(CMAX):
            print(f"{N[r][c]:>4}|",end="")
        print()
    print("="*((CMAX*5)+11))
    system('pause') #cmd only.
    
#main
Option1 = 6
Option2 = 6
Heading=['Sex','Pay-type','Education','age group']
A = []
CT = []
N = []
init(CT,N)
enter(A)
while Option1 > 0:
    Option1 -= 1
    Option2 -= 1
    RMAX=0 # รีเซ็ตขอบเขต
    CMAX=0
    calc(CT,N)
    report(CT)
    init(CT,N)
print("Exit Program.")
system('cls')
