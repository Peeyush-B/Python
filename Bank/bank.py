import json
from time import sleep
import os
from getpass import getpass

def get_data():
    fp=open("G://Workspace/Python/Bank/data.db","r+")
    data=json.load(fp)
    fp.close()
    return data

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
    print("\n-.-.-.-.-.-.-.-.-chose an option-.-.-.-.-.-.-.-.-")
    ch=int(input("\n1.Deposite\n2.Withdrawl\n3.Check Balance\n4.New a/c Open\n5.Edit information\n6.Manager Login\n"))
    if ch==1:
        load()
        deposite()
    elif ch==2:
        load()
        withdrawl()
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
    else:
        load()
        print("invalid option".center(50,"*"))
		
def deposite():
    acn=input("\nEnter Your Account Number:-")
    data=get_data()
    if acn not in data.keys():
        print("acount number not available".center(50,"*"))
        return
    amt=int(input("Enter amount to deposite:-"))
    data[acn]['bal']+=amt
    put_data(data)

def withdrawl():
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in data.keys():
        print("acount number not available".center(50,"*"))
        return
    usr_nm=input("Enter user name:-")
    paswd=getpass("Enter password:-")
    data=get_data()
    if usr_nm!=data[acn]['user'] or paswd!=data[acn]['password']:
        print("username or password incorrect".center(50,"*"))
        return
    amt=int(input("Enter amount to withdraw:-"))
    if amt>data[acn]['bal']:
        print("insufficiant balance".center(50,"*"))
        return
    data[acn]['bal']-=amt
    print("transation successful".center(50,"*"))
    put_data(data)

def chk_bal():
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in data.keys():
        print("acount number not available".center(50,"*"))
        return
    print(f"Acount number->{acn}\nholder\'s name->{data[acn]['fname']}\nAvailable balance->{data[acn]['bal']}")    

def new_ac():
    fname=input("enter your first name:-")
    lname=input("enter your last name:-")
    mbn=int(input("enter your mobile numbre:-"))
    adrs=input("enter your permanent address:-")
    dob=input("enter your date of birth(yyyy-mm-dd):-")
    uname=input("enter your user name:-")
    password=getpass("enter your password:-")
    data=get_data()
    ky=data['key']
    data['key']+=1
    d={}
    d.setdefault("fname",fname);d.setdefault("lname",lname);d.setdefault("mobile",mbn)
    d.setdefault("address",adrs);d.setdefault("dob",dob);d.setdefault("user",uname)
    d.setdefault("password",password)
    d.setdefault("bal",0);d.setdefault("loan",0)
    data.setdefault(str(ky),d)
    put_data(data)

def edit_info():
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in data.keys():
        print("acount number not available".center(50,"*"))
        return
    print("-.-.-.-.-.-.-.-.-What you want to edit-.-.-.-.-.-.-.-.-")
    ch=int(input("1.fname\n2.lname\n3.mobilenumber\n4.password\n5.address\n"))
    if ch==1:
        x=input("enter new first name:-")
        data[acn]['fname']=x
    elif ch==2:
        x=input("enter new last name:-")
        data[acn]['lname']=x
    elif ch==3:
        x=input("enter new mobile number:-")
        data[acn]['mobile']=x
    elif ch==4:
        x=input("enter new password:-")
        data[acn]['password']=x
    elif ch==5:
        x=input("enter new address:-")
        data[acn]['address']=x
    else:
        print("invalid option".center(50,"*"))
    put_data(data)

def mgr():
    usr_nm=input("Enter user name:-")
    paswd=getpass("Enter password:-")
    data=get_data()
    if usr_nm!=data['mgr']['user'] or paswd!=data['mgr']['pass']:
        print("username or password incorrect".center(50,"*"))
        return
    acn=input("enter account number to see details:-")
    if acn not in data.keys():
        print("acount number not available".center(50,"*"))
        return
    print("details of given account number".center(50,"*"))
    print(f"account number->{acn}\nfirst name->{data[acn]['fname']}\nlast name->{data[acn]['lname']}\nmobile number->{data[acn]['mobile']}")
    print(f"address->{data[acn]['address']}\nAvailable balance->{data[acn]['bal']}\ngranted loan->{data[acn]['loan']}")



def loan():
    acn=input("Enter Your Account Number:-")
    data=get_data()
    if acn not in data.keys():
        print("acount number not available".center(50,"*"))
        return
    print("-.-.-.-.-.-.-.-.-Select your Profession-.-.-.-.-.-.-.-.-")
    ch=int(input("1.Govt. employee\n2.Private Employee\n3.Businessman\n4.Student\n5.Unemployeed\n"))
    if ch==1:
        govt(acn)
    if ch==2:
        pvt_emp(acn)
    if ch==3:
        business(acn)
    if ch==4 or ch==5:
        print("loan not granted")
    else:
        print("invalid option".center(50,"*"))


def govt(acn):
    data=get_data()
    if data[acn]['loan']!=0:
        print("Loan is already granted:- ")
        return
    salary=int(input("what is your monthly salary:- "))
    pay_slip=''
    while pay_slip!='yes' and pay_slip!='no':
        pay_slip=input("Do yo have pay slip(Yes/no):- ").strip().lower()
        if pay_slip!='yes' or pay_slip!='no':
            print("  please answer in Yes/No  ")
    if pay_slip=="no":
        print("  Loan can not be granted without pay slip ")
        return
    if salary<20000:
        print("loan can not granted")
    elif salary>=20000 and salary<50000:
        print("A loan of 100000 is granted")
        data[acn]['loan']=100000
        data[acn]['bal']+=100000
    elif salary>=50000 and salary<100000:
        print("A loan of 300000 is granted")
        data[acn]['loan']=200000
        data[acn]['bal']+=200000
    elif salary>=100000 and salary<500000:
        print("A loan of 400000 is granted")
        data[acn]['loan']=400000
        data[acn]['bal']+=400000
    elif salary>=500000:
        print("A loan of 1000000 is granted")
        data[acn]['loan']=1000000
        data[acn]['bal']+=1000000
    put_data(data)


def pvt_emp(acn):
    data=get_data()
    if data[acn]['loan']!=0:
        print("Loan is already granted:- ")
        return
    salary=int(input("what is your monthly salary:- "))
    prop=''
    while prop!='yes' and prop!='no':
        prop=input("Loan can be granted againest property\nAre you agree (Yes/no):- ").strip().lower()
        if prop!='yes' and prop!='no':
            print("  please answer in Yes/No  ")
    if prop=="no":
        print("  Loan can not be granted without property papers ")
        return
    if salary<50000:
        print("loan can not granted")
    elif salary>=50000 and salary<100000:
        print("A loan of 200000 is granted")
        data[acn]['loan']=200000
        data[acn]['bal']+=200000
    elif salary>=100000 and salary<300000:
        print("A loan of 300000 is granted")
        data[acn]['loan']=300000
        data[acn]['bal']+=300000
    elif salary>=300000:
        print("A loan of 500000 is granted")
        data[acn]['loan']=500000
        data[acn]['bal']+=500000
    put_data(data)


def business(acn):
    data=get_data()
    if data[acn]['loan']!=0:
        print("Loan is already granted:- ")
        return
    salary=int(input("what is your monthly salary:- "))
    ITR=''
    while ITR!='yes' and ITR!='no':
        ITR=input("Do you have ITR-V(Income Tax Return Verification) (Yes/no):- ").strip().lower()
        if ITR!='yes' and ITR!='no':
            print("  please answer in Yes/No  ")
    if ITR=="no":
        print("  Loan can not be granted without ITR ")
        return
    if salary<50000:
        print("loan can not granted")
    elif salary>=50000 and salary<100000:
        print("A loan of 50000 is granted")
        data[acn]['loan']=50000
        data[acn]['bal']+=50000
    elif salary>=100000 and salary<300000:
        print("A loan of 120000 is granted")
        data[acn]['loan']=120000
        data[acn]['bal']+=120000
    elif salary>=300000:
        print("A loan of 500000 is granted")
        data[acn]['loan']=500000
        data[acn]['bal']+=500000
    put_data(data)


opt=int(input("-.-.-.-.-.-.-.-.chose option.-.-.-.-.-.-.-.-.-\n1.banking\n2.Loan"))
if opt==1:
    load()
    banking()
elif opt==2:
    load()
    loan()
else:
    print("invalid option".center(50,"*"))