import json
from time import sleep
import os
from getpass import getpass

def dec1(str):
    print("*"*120)
    print(("--"+str+"--").center(120))
    print("*"*120)
    print("\n")


def clear(str):
    os.system("cls")
    dec1(str)


def get_data():
    fp=open("G://Workspace/Python/Bank/data.db","r+")
    data=json.load(fp)
    fp.close()
    return data

def leap(a):
    if a%4==0 and a%100==0:
        if a%400==0:
            return 1
        else:
            return 0
    elif a%4==0:
        return 1
    else:
        return 0

def put_data(data):
    fp=open("G://Workspace/Python/Bank/data.db","w")
    json.dump(data,fp)
    fp.close()

def load():
    
    print("Loading",end='')
    
    for var in range(6):
        sleep(0.4)
        print('.',end='')

def loan():
    clear("Loan ")
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in (data.keys()-['mgr','key']):
        clear("Loan")
        print("acount number not available please try again".center(120,"*"))
        load()
        loan()
    i=0
    while i==0:
        usr_nm=input("Enter user name:-")
        paswd=getpass("Enter password:-")
        data=get_data()
        if usr_nm!=data[acn]['user'] or paswd!=data[acn]['password']:
            clear("Withdrawal")
            print("Transaction Failed".center(120,"*"))
            print("username or password incorrect please try again".center(120,"*"))
        else:
            i=1
    clear("Loan")
    print("-.-.-.-.-.-.-.-.-Select your Profession-.-.-.-.-.-.-.-.-")
    ch=int(input("1.Govt. employee\n2.Private Employee\n3.Businessman\n4.Student\n5.Unemployeed\n"))
    if ch==1:
        load()
        govt(acn)
    if ch==2:
        load()
        pvt_emp(acn)
    if ch==3:
        load()
        business(acn)
    if ch==4 or ch==5:
        load()
        clear("Loan")
        print("You are Not Eligible for loan")
    else:
        clear()
        print("invalid option Try Again".center(120,"*"))
        loan()
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()



def govt(acn):
    clear("Loan")
    data=get_data()
    if data[acn]['loan']!=0:
        load()
        clear("Loan")
        print("Loan is already granted:- ".center(120,"*"))
        start()
    clear("loan")
    salary=int(input("what is your monthly salary:- "))
    pay_slip=''
    while pay_slip!='yes' and pay_slip!='no':
        pay_slip=input("Do yo have pay slip(Yes/no):- ").strip().lower()
        if pay_slip!='yes' and pay_slip!='no':
            print("  please answer in Yes/No  ")
    load()
    clear("Loan")
    if pay_slip=="no":
        clear("Loan")
        print("  You are not eligible for a loan without pay slip ")
        load()
        load()
        start()
    if salary<20000:
        clear("Loan")
        print("  You are not eligible for a loan  ")
    elif salary>=20000 and salary<50000:
        print("A loan of 100000 is Approved")
        data[acn]['loan']=100000
        data[acn]['bal']+=100000
    elif salary>=50000 and salary<100000:
        print("A loan of 300000 is Approved")
        data[acn]['loan']=200000
        data[acn]['bal']+=200000
    elif salary>=100000 and salary<500000:
        print("A loan of 400000 is Approved")
        data[acn]['loan']=400000
        data[acn]['bal']+=400000
    elif salary>=500000:
        print("A loan of 1000000 is Approved")
        data[acn]['loan']=1000000
        data[acn]['bal']+=1000000
    put_data(data)
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()


def pvt_emp(acn):
    clear("Loan")
    data=get_data()
    if data[acn]['loan']!=0:
        load()
        clear("Loan")
        print("A Loan is already Approved to you:- ")
        start()
    salary=int(input("what is your monthly salary:- "))
    prop=''
    while prop!='yes' and prop!='no':
        clear("Loan")
        prop=input("Loan can be granted againest property\nAre you agree (Yes/no):- ").strip().lower()
        if prop!='yes' and prop!='no':
            print("  please answer in Yes/No  ")
    if prop=="no":
        clear("Loan")
        print("  Loan can not be Approved without property papers ")
        load()
        load()
        start()
    load()
    clear("Loan")
    if salary<50000:
        print("You are not Eligible for loan")
    elif salary>=50000 and salary<100000:
        print("A loan of 200000 is Approved")
        data[acn]['loan']=200000
        data[acn]['bal']+=200000
    elif salary>=100000 and salary<300000:
        print("A loan of 300000 is Approved")
        data[acn]['loan']=300000
        data[acn]['bal']+=300000
    elif salary>=300000:
        print("A loan of 500000 is Approved")
        data[acn]['loan']=500000
        data[acn]['bal']+=500000
    put_data(data)
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()


def business(acn):
    clear("Loan")
    data=get_data()
    if data[acn]['loan']!=0:
        load()
        clear("Loan")
        print("Loan is already Approved to you:- ")
        load()
        load()
        start()
    salary=int(input("what is your monthly salary:- "))
    ITR=''
    while ITR!='yes' and ITR!='no':
        ITR=input("Do you have GST number (Yes/no):- ").strip().lower()
        if ITR!='yes' and ITR!='no':
            print("  please answer in Yes/No  ")
    if ITR=="no":
        load()
        clear("Loan")
        print("Loan can not be Approved without GST Number")
    else:
        clear("Loan")
        if salary<50000:
            print("You are not Eligible for Loan")
        elif salary>=50000 and salary<100000:
            print("A loan of 50000 is Approved")
            data[acn]['loan']=50000
            data[acn]['bal']+=50000
        elif salary>=100000 and salary<300000:
            print("A loan of 120000 is Approved")
            data[acn]['loan']=120000
            data[acn]['bal']+=120000
        elif salary>=300000:
            print("A loan of 500000 is Approved")
            data[acn]['loan']=500000
            data[acn]['bal']+=500000
        put_data(data)
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()

def start():
    loan()
start()