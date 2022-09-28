from main import *
import pandas as pd
from csv import writer
import csv
import uuid


print(response("ticket"))

 
def input1(A):
    b= response(A)
    return b

 
input1("hi")

 
response("register")

 
response("signin")

   
# ####   read 
# file = open('userDetails.csv')
# print(type(file))
# csvreader = csv.reader(file)
# rows = []
# for row in csvreader:
#         rows.append(row)
# rows

   
# ###   write
# df = pd.read_csv('userDetails.csv')
# 
# print(df) 
# arr = df.to_numpy()
# print(arr)

bot_name = "Hana"

def signUp():
    a=input("Enter your email : ")
    b=input("Enter your phone number : ")
    c=input("Enter your name : ")
    d=input("Enter your password : ")
    List=[a,b,c,d]
    with open('userDetails.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()
    print("Signup done successfully")
#signUP()

 
pd.read_csv('userDetails.csv')

 
def login():
        df = pd.read_csv('userDetails.csv')
        arr = df.to_numpy()
        a1=input("enter you email : ")
        b1=input("enter you password : ")
        for i in range(len(arr)):
                if(a1==arr[i][0]):
                        if(b1==arr[i][3]):
                                print("Login successfull")
                                valid =1
        if(valid==1):
                return 1
        else:
                return 0

#login()

 
def login1(a,b):
        a1=str(a)
        b1=str(b)
        df = pd.read_csv('userDetails.csv')
        arr = df.to_numpy()
        valid=0
        for i in range(len(arr)):
                if(a1==arr[i][0]):
                        if(b1==arr[i][3]):
                                print("Login successfull")
                                valid =1
        if(valid==1):
                return 1
        else:
                return 0
#login1(1,1)

 
# updating the column value/data
#df.loc[1, 'avilability3A'] = 49
#df.to_csv("trainDetails.csv", index=False)

 
def book1(cID,train,cls,nt):
    tic=[uuid.uuid1(),cID,train[0],train[1],train[2],train[3],train[4],train[5],train[6],cls,nt]
    #print(tic)
    with open('bookingDetails.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(tic)
        f_object.close()

 

def book():
    a1=input("Enter your userID : ")
    b1=input("Enter you password : ")
    auth=login1(a1,b1)
    if(auth==1):
        df = pd.read_csv('trainDetails.csv')
        print(df)
        arr = df.to_numpy()
        clas1=0
        valid=0
        valid1=0
        trainId=int(input("Enter the train ID to book : "))
        clas=input("Entert the class (2A, 3A, SL) : ")
        clas=clas.upper()

        nt=int(input("Enter the number of Ticket : "))
        for i in range(len(arr)):
            if(arr[i][0]==trainId):
                valid1=1
                if(clas=="2A"):
                    valid=1
                    clas1=7
                    if(arr[i][clas1]>=nt):
                        update=int(arr[i][clas1])-nt
                        df.loc[i, 'avilability2A'] = update
                        df.to_csv("trainDetails.csv", index=False)
                        print("Ticket booked")
                        book1(a1,arr[i],clas,nt)
                    else:
                        print("ticket not available")
                if(clas=="3A"):
                    valid=1
                    clas1=8
                    if(arr[i][clas1]>=nt):
                        update=int(arr[i][clas1])-nt
                        df.loc[i, 'avilability3A'] = update
                        df.to_csv("trainDetails.csv", index=False)
                        print("Ticket booked")
                        book1(a1,arr[i],clas,nt)
                    else:
                        print("ticket not available")
                if(clas=="SL"):
                    valid=1
                    clas1=9
                    print(arr[i][clas1])
                    if(arr[i][clas1]>=nt):
                        update=int(arr[i][clas1])-nt
                        df.loc[i, 'avilabilitySL'] = update
                        df.to_csv("trainDetails.csv", index=False)
                        print("Ticket booked")
                        book1(a1,arr[i],clas,nt)
                    else:
                        print("ticket not available")
        if(valid==0):
            print("Enter the valid class")
        if(valid1==0):
            print("Enter the vaild train number ")
                
    else:
        print("User ID or password incorret ")
        print("Enter sign up for new user ")
        print("Enter book to book the ticket ")
 
#book()

 
def viewTicket():
    a1=input("Enter your userID : ")
    b1=input("Enter you password : ")
    auth=login1(a1,b1)
    if(auth==1):
        df = pd.read_csv('bookingDetails.csv')
        arr = df.to_numpy()
        for i in range(len(arr)):
            if(arr[i][1]==a1):
                print(df.loc[i])

#viewTicket()

 
def mainChatbot():
    print("Welcome to rail way chatbot service !!!!!")
    print("*****---------*****---------*****")
    print("Enter sign up in case of new user")
    print("To book a ticket enter book")
    print("Enter ticket view to see the booked ticket")
    a=input()
    out=response(a)
    if(out=="signUp"):
        signUp()
    if(out=="book"):
        book()
    if(out=="view"):
        viewTicket()
    if(out==""):
        print("Currently we dont provide this service, sorry for the inconvience")
        print("*****---------*****---------*****")
        print("Enter sign up in case of new user")
        print("To book a ticket enter book")
        print("Enter ticket view to see the booked ticket")
        qus=[a]
        with open('newquestion.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(qus)
            f_object.close()
while True:
    mainChatbot()



