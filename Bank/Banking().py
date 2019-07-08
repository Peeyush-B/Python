from time import sleep
import os
from getpass import getpass
import json

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



def banking():
    clear("banking")
    print("\n\n-.-.-.-.-.-.-.-.-chose an option-.-.-.-.-.-.-.-.-")
    ch=int(input("\n1.Deposite\n2.Withdrawal\n3.Check Balance\n4.New a/c Open\n5.Edit information\n6.Manager Login\n7.Main menu"))
    if ch==1:
        load()
        deposite()
    elif ch==2:
        load()
        withdrawal()
    elif ch==3:
        load()
        chk_bal()
    elif ch==4:
        load()
        new_ac()
    elif ch==5:
        load()
        edit_info()
    elif ch==6:
        load()
        mgr()
    elif ch==7:
        load()
        start()
    else:
        load()
        clear("banking")
        print("invalid option  Try Again".center(120,"*"))
        load()
        banking()

def deposite():
    clear("Deposite")
    acn=input("\nEnter Your Account Number:-")
    data=get_data()
    if acn not in (data.keys()-['mgr','key']):
        print("acount number not available try again".center(120,"*"))
        load()
        deposite()
    amt=int(input("Enter amount to deposite:-"))
    data[acn]['bal']+=amt
    put_data(data)
    clear("Deposite")
    print("Transaction successful".center(120,"~"))
    clear("Deposite")
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()

def withdrawal():
    clear("Withdrawal")
    acn=input("\nEnter Your Account Number:-")
    data=get_data()
    if acn not in (data.keys()-['mgr','key']):
        print("\nacount number not available please try again".center(120,"*"))
        load()
        withdrawal()
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
    while i==1:
        amt=int(input("Enter amount to withdraw:-"))
        if amt>data[acn]['bal']:
            print("insufficiant balance".center(120,"*"))
            load()
        elif amt<0:
            print("--Amount can not be negative try again--")
        else:
            i=0
    data[acn]['bal']-=amt
    load()
    put_data(data)
    clear("Withdrawal")
    print("transation successful".center(120,"*"))
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()

def chk_bal():
    clear("Balance")
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in (data.keys()-['mgr','key']):
        print("acount number not available please try again".center(120,"*"))
        load()
        chk_bal()
    clear("Balance")
    print(f"Acount number->{acn}\nname->{data[acn]['fname']}\nAvailable balance->{data[acn]['bal']}")
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()

def new_ac():
    clear("Creating Account")
    fname=input("enter your first name:-")
    lname=input("enter your last name:-")
    i=0
    while i==0:
        mbn=int(input("enter your mobile numbre:-"))
        if len(str(mbn))!=10:
            print("*-* invalid mobile number please try again *-*")
        else:
            i=1
    adrs=input("enter your permanent address:-")
    while i==1:
        adhr=int((input("enter your AADHAR number:-")))
        if len(str(adhr))!=12:
            print("*-* invalid AADHAR number please try again *-*")
        else:
            i=0
    while i==0:
        dob=input("enter your date of birth(yyyy-mm-dd):-")
        if dob[0:4].isdigit() and dob[4]==dob[7]=='-' and dob[5:7].isdigit() and dob[8:10].isdigit() and len(dob)==10:
            if int(dob[5:7]) in range(1,13):
                if int(dob[5:7]) in [1,3,5,7,8,10,12] and int(dob[8:10]) in range(1,32):
                    i=1
                    break
                elif int(dob[5:7]) in [4,6,9,11] and int(dob[8:10]) in range(1,31):
                    i=1
                    break
                elif int(dob[5:7])==2:
                    x=leap(int(dob[0:4]))
                    if x==1 and int(dob[8:10]) in range(1,30):
                        i=1
                        break
                    elif x==0 and int(dob[8:10]) in range(1,29):
                        i=1
                        break
                    else:print("*-* invalid date please try again *-*")
                else:print("*-* invalid date please try again *-*")
            else:print("*-* invalid date please try again *-*")
    else:print("*-* invalid date please try again *-*")
    uname=input("enter your user name:-")
    
    i=0
    while i==0:
        password=getpass("enter your password:-")
        if len(password)>=5:
            i=1
        else:print("--Password is too short-- \n--Password length must be more than 5 --")
    data=get_data()
    ky=data['key']
    data['key']+=1
    d={}
    d.setdefault("fname",fname);d.setdefault("lname",lname);d.setdefault("mobile",mbn)
    d.setdefault("address",adrs);d.setdefault("aadhar",adhr);d.setdefault("dob",dob);d.setdefault("user",uname)
    d.setdefault("password",password)
    d.setdefault("bal",0);d.setdefault("loan",0)
    data.setdefault(str(ky),d)
    put_data(data)
    clear("Creating Account")
    load()
    print("New account created".center(120,"*"))
    load()
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()
  

def edit_info():
    clear("Edit information")
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in (data.keys()-['mgr','key']):
        print("acount number not available please try again".center(120,"*"))
        load()
        edit_info()
    data=get_data()
    i=0
    while i==0:
        usr_nm=input("Enter user name:-")
        paswd=getpass("Enter password:-")
        if usr_nm!=data[acn]["user"] or paswd!=data[acn]["password"]:
            clear("Edit information")
            print("Transaction Failed".center(120,"*"))
            print("username or password incorrect please try again".center(120,"*"))
        else:
            i=1
    load()
    clear("Edit information")
    print("-.-.-.-.-.-.-.-.-What you want to edit-.-.-.-.-.-.-.-.-")
    ch=int(input("1.fname\n2.lname\n3.mobilenumber\n4.password\n5.address\n"))
    if ch==1:
        x=input("enter new first name:-")
        data[acn]['fname']=x
    elif ch==2:
        x=input("enter new last name:-")
        data[acn]['lname']=x
    elif ch==3:
        i=0
        while i==0:
            x=input("enter new mobile number:-")
            if len(x)==10 and x.isdigit():
                i=1
            else:print("*-* Invalid mobile number *-*")
        data[acn]['mobile']=x
    elif ch==4:
        i=0
        while i==0:
            password=getpass("enter your password:-")
            if len(password)>=5:
                i=1
            else:
                print("--Password is too short-- \n--Password length must be more than 5 --")
        data[acn]['password']=password
    elif ch==5:
        x=input("enter new address:-")
        data[acn]['address']=x
    else:
        print("invalid option try again".center(120,"*"))
        edit_info()
    put_data(data)
    load()
    clear("Edit information")
    print("Change Successful".center(120,"*"))
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()
    

def mgr():
    clear('Manager Login')
    usr_nm=input("Enter user name:-")
    paswd=getpass("Enter password:-")
    data=get_data()
    if usr_nm!=data['mgr']['user'] or paswd!=data['mgr']['pass']:
        clear()
        print("Transaction Failed".center(120,"*"))
        print("username or password incorrect".center(120,"*"))
        load()
        mgr()
    acn=input("enter account number to see details:-")
    while acn not in (data.keys()-['mgr','key']):
        print("acount number not available please try again".center(120,"*"))
        acn=input("enter account number to see details:-")
    clear('Manager Login')
    load()
    print("details of given account number".center(50,"*"))
    print(f"account number->{acn}\nfirst name->{data[acn]['fname']}\nlast name->{data[acn]['lname']}\nmobile number->{data[acn]['mobile']}")
    print(f"AADHAR->{data[acn]['aadhar']}\naddress->{data[acn]['address']}\nAvailable balance->{data[acn]['bal']}\nLoan->{data[acn]['loan']}")
    op=input("DO you want to continue ").strip().lower()
    if op=='yes':
        start()
    else:
        exit()
banking()