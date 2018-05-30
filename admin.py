# -*- coding: utf-8 -*-
"""
Created on Fri May  4 22:53:00 2018

@author: ADITYA
"""

import customer
buffer=""
a=customer.acc_query()
class admin():
    def __init__(self):
        self.fname=""
        self.lname=""
        self.empid=""
        self.dept=""
        self.passw=""
        self.emplist=list()
    
    def update_emplist(self):
        global buffer
        file=open("admin.txt","r")
        for buffer in file:
            self.unpack()
            self.emplist.append(self.empid)
            
    def write_rec(self):
        global buffer
        self.update_emplist()
        self.empid=input("Enter Employee Id:")
        self.empid=self.empid.upper()
        if self.empid not in self.emplist:
            self.emplist.append(self.empid)
            self.f_name=input("Enter first name:")
            self.l_name=input("Enter last name:")
            self.dept=input("Enter department:")
            self.passw=self.x3()
            self.pack()
            file=open("admin.txt","a+")
            file.write(buffer)
            file.close()
            print("Admin "+self.f_name+" with Employee Id = "+self.empid+" Registered") 
        else:
            print("\nThis employee is already registered.\nPlease Try again\n")
            
    def x3(self):
        pass1=input("Password(8-Digit):")
        t=len(pass1)
        if(t>=8):
            return pass1
        else:
            print("invalid password(too short)")
            x=self.x3()
            return x
        
    def pack(self):
        global buffer
        buffer=self.empid+"|"+self.f_name+"|"+self.l_name+"|"+self.dept+"|"+self.passw+"|\n"
            
    def unpack(self):
        x=buffer.split("|")
        self.empid=x[0]
        self.f_name=x[1]
        self.l_name=x[2]
        self.dept=x[3]
        self.passw=x[4]
        
    def login(self):
        global buffer
        x,flag=0,0
        file=open("admin.txt")
        while x<3:
            file.seek(0,0)
            acc=input("Employee Id:")
            acc=acc.upper()
            pass1=input("Password:")
            for line in file:
                buffer=line
                self.unpack()
                if self.empid==acc and self.passw == pass1:
                    flag=1
                    print("Admin Login Successfull \n")
                    self.submenu()
                    return
                else:
                    continue
            if flag==0:                
                print("\nInvalid Account No--Password combination\nPlease try again!\n")
                x+=1
                if x>0 : print(3-x,"Attempts remaining")
        if(x==3) : print("3 Incorrect Attempts!\nExiting...")
 
    def submenu(self):
        while(1):
            print("\n\n----WELCOME "+self.f_name.upper()+"----",end='\n')
            print("\n\n****ACCOUNT INFORMATION SYSTEM****",end='\n')
            print("\nSelect one option below ")
            print("\n\t1-->Show customer records")
            print("\n\t2-->Search a customer Record")
            print("\n\t3-->Update a customer Record")
            print("\n\t4-->Delete a customer Record")
            print("\n\t5-->Quit")
            choice=int(input("Enter your choice:"))
            
            if choice==1:
                a.display()
                
            elif choice==2:
                key=int(input("\nEnter the Account No. to be searched \n"))
                a.search(key)
                
            elif choice==3:
                key=int(input("\nEnter the Account No. who's record you wish to modify \n"))
                a.update(key)
                
            elif choice==4:
                key=int(input("\nEnter the Account No. who's record you wish to delete \n"))
                a.delete(key)
        
            elif choice==5:
                break
            
            elif choice==9:
                a.create_pri_index()
                print("\n\n",a.acc_list,"\n\n",a.addr_list,"\n\n",a.count,"\n\n",a.acc_no,"\n\n")
            
            else:
                print("\n Invalid option \n Please Try again")