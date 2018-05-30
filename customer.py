# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:39:34 2018

@author: ADITYA
"""

buffer=""
list_of_acc=range(1001,2000)
class acc_query():
   
    def __init__(self):
        self.acc_no=1000
        self.f_name=""
        self.l_name=""
        self.addr=""
        self.acc_typ=""
        self.phone=0
        self.email=""
        self.t_balance=0.0
        self.passw=""
        self.acc_list=list()
        self.addr_list=list()
        self.count=-1
        
    def sort_pri_index(self):
        for i in range(self.count+1):
            for j in range(i+1,self.count+1):
                if(self.acc_list[i]>self.acc_list[j]):
                    temp=self.acc_list[i]
                    self.acc_list[i]=self.acc_list[j]
                    self.acc_list[j]=temp
                    
                    temp_a=self.addr_list[i]
                    self.addr_list[i]=self.addr_list[j]
                    self.addr_list[j]=temp_a
   
    def create_pri_index(self):
        global buffer
        self.__init__()
        pos=0
        file=open("record.txt","r+")
        self.count=-1
        for line in file:
            buffer=line
            if buffer=="\n":
                return
            x=buffer.split("|")
            acc=int(x[0])
            self.count+=1
            self.acc_list.append(None)
            self.addr_list.append(None)
            self.acc_list[self.count]=acc        
            self.addr_list[self.count]=pos
            pos+=len(line)+1
        file.close()
        self.sort_pri_index()       
    
    def read_data(self):
        print("ENTER INFORMATION:")
        self.acc_no=self.setacc()
        self.f_name=input("Enter first name:")
        self.l_name=input("Enter last name:")
        self.phone=self.x1()
        self.email=input("Enter your valid email address:")
        self.addr=input("Enter your permanent address:")
        self.acc_typ=self.x2()
        self.passw=self.x3()
        self.t_balance=self.x4(self.acc_typ)
        
    def setacc(self):
        global list_of_acc
        for i in list_of_acc:
            if i not in self.acc_list:
                return i
        
    def x1(self):
        ph=input("Enter valid Phone no:")
        if ph.isdigit() and len(ph)==10:
            return ph
        else :
            print("\nInvalid Phone number entered \nPlease try again")
            x=self.x1()
            return x

    def x2(self):
        type1=input("Type of account (SA,CA):")
        type1=type1.upper()
        if type1!="SA" and type1!="CA":
            print("Invalid entry")
            x=self.x2()
            return x
        else:
            return type1

    def x3(self):
        pass1=input("Password(8-Digit):")
        t=len(pass1)
        if(t>=8):
            return pass1
        else:
            print("invalid password(too short)")
            x=self.x3()
            return x

    def x4(self,type1):
        if type1=="CA":
            bal=5000.0
        else:
            bal=0.0
        return bal
    
    def show_data(self):
            print("\n")
            print("Account Number:",self.acc_no)
            print("First Name:",self.f_name)
            print("Last Name:",self.l_name)
            print("Phone:",self.phone)
            print("Email:",self.email)
            print("Address:",self.addr)
            print("Account Type::",self.acc_typ)
            print("Current Balance:Rs.",self.t_balance)
            
    def login(self):
        global buffer
        x=0
        self.create_pri_index()
        file=open("record.txt")
        while x<3:
            acc=int(input("Account number:"))
            if acc not in self.acc_list:
                 print("\nInvalid Account No\nPlease try again!")
                 x+=1
                 continue
            pass1=input("Password:")
            pos=self.search_pi(acc)
            addr=self.addr_list[pos]
            file.seek(addr)
            buffer=file.readline()
            self.unpack()
            if self.passw == pass1:
                print("Successfull login \n")
                self.submenu(self.acc_no)
                return
            else:
                print("\nInvalid Account No--Password combination\nPlease try again!")
                x+=1
                if x>0 : print(3-x,"Attempts remaining")
        if(x==3) : print("3 Incorrect Attempts!\nExiting...")
             
    def display(self):
        global buffer
        file=open("record.txt","r")
        for line in file:
            buffer=line
            if buffer == "":
                print("The file is empty")
            self.unpack()
            self.show_data()
        file.close()
           
    def write_rec(self):
        global buffer
        self.create_pri_index()
        file= open("record.txt","a+")
        self.read_data()
        if self.acc_no not in self.acc_list:
            self.pack()
            pos=file.tell()
            file.write(buffer)
            file.close()
            self.count+=1
            self.acc_list.append(None)
            self.addr_list.append(None)
            self.acc_list[self.count]=self.acc_no        
            self.addr_list[self.count]=pos 
            self.sort_pri_index() 
            print(self.f_name+" with Account Number = "+str(self.acc_no)+" Registered\nLogin To Continue\n")
        else:
            print("\nThe account number is already registered.\n")
            return
        
    def pack(self):
        global buffer
        buffer=str(self.acc_no)+"|"+self.f_name+"|"+self.l_name+"|"+self.phone+"|"+self.email+"|"+self.addr+"|"+self.acc_typ+"|"+str(self.t_balance)+"|"+self.passw+"|"+"\n"
        
    def unpack(self):
        global buffer
        p=buffer.split("|")
        self.acc_no=int(p[0])
        self.f_name=p[1]
        self.l_name=p[2]
        self.phone=p[3]
        self.email=p[4]
        self.addr=p[5]
        self.acc_typ=p[6]
        self.t_balance=float(p[7])
        self.passw=p[8]
    
    def search(self,key):
        global buffer
        file=open("record.txt","r")
        flag=0
        for line in file:
            buffer=line
            self.unpack()
            if self.acc_no==key:
                flag=1
                self.show_data()
                break
        if flag==1:return
        elif flag==0:
            print("\nNo such account number registered")
            return

        
    def search_pi(self,key):
        self.create_pri_index()
        low,high,mid,flag=0,self.count,0,0
        while(low<=high):
            mid=int((low+high)/2)
            if self.acc_list[mid]==key:
                flag=1
                break
            elif self.acc_list[mid]>key:
                high=mid-1
            else:
                low=mid+1
        if flag==1:
            return mid 
        else:
            return -1
      
    def delete(self,key):
        global buffer
        pos=self.search_pi(key)
        if pos>=0:
            file=open("record.txt","r")
            lines=file.readlines()
            file.close()
            file=open("record.txt","w")
            for line in lines:
                if not line.startswith(str(key)):
                    file.write(line)
            file.close()
            self.create_pri_index()
            print("\nRecord Deleted!\n")
            file.close()
            return
        else:
            print("\nNo such account number registered")
            return
    
    def deposit(self,acc):
        global buffer
        addr=self.addr_list[self.search_pi(acc)]
        file=open("record.txt","r")
        lines=file.readlines()
        file.close()
        file=open("record.txt","w")
        for line in lines:
            buffer=line
            self.unpack()
            if self.acc_no==acc:
                print("Your current account balance is = ",self.t_balance)
                amount=float(input("Enter the amount you wish to deposit : Rs."))
                self.t_balance+=amount
                self.pack()
                file.write(buffer)
                print("Rs.",amount,"deposited successfully\nYour updated balance = Rs.",self.t_balance)
            else: file.write(buffer)
        file.close()
        file=open("record.txt","r")
        file.seek(addr)
        buffer=file.readline()
        self.unpack()
        file.close()
        return
    
    def withdraw(self,acc):
        global buffer
        
        if self.t_balance <= 0:
            print("Your account balance is Rs",self.t_balance,"\nIt is too low to make a withdrawal\nPlease deposit money in your account")
            return
        
        amount=float(input("Enter the amount you wish to withdraw : Rs."))
        if amount == self.t_balance:
            print("Your current account balance is = Rs.",self.t_balance)
            ch=input("Do you really wish to empty your account? (y/n) ")
            if ch=='n':
                print("Cancelling deposit....")
                return
            elif ch=='y':
                pass
        elif amount>self.t_balance:
            print("ERROR : Your current account balance Rs",self.t_balance,"is too low for this transaction request.\nPlease try again")
            return
        addr=self.addr_list[self.search_pi(acc)]
        file=open("record.txt","r")
        lines=file.readlines()
        file.close()
        file=open("record.txt","w")
        for line in lines:
            buffer=line
            self.unpack()
            if self.acc_no==acc:
                print("Your current account balance is = Rs.",self.t_balance)
                self.t_balance-=amount
                self.pack()
                file.write(buffer)
                print("Rs.",amount,"withdrawn successfully\nYour updated balance = Rs.",self.t_balance)
            else: file.write(buffer)
        
        file.close()
        file=open("record.txt","r")
        file.seek(addr)
        buffer=file.readline()
        self.unpack()
        file.close()
        return

    def update(self,key):
        global buffer
        flag=0
        curbal=self.t_balance
        file=open("record.txt","r")
        lines=file.readlines()
        file.close()
        file=open("record.txt","w")
        for line in lines:
            buffer=line
            self.unpack()
            if self.acc_no == key:
                flag=1
                print("\nThe current details for account number = "+str(self.acc_no)+" are:")
                self.show_data()
                print("\nEnter the new details :")
                self.read_data()
                self.acc_no=key
                self.t_balance=curbal
                self.pack()
                file.write(buffer)
                print("\nRecord Updated\n")
            else:
                file.write(line)
        self.create_pri_index()
        if flag==0: print("\nNo such account number registered")
        file.close()
        
    def submenu(self,acc):
        while(1):
            print("\n\n****WELCOME "+self.f_name.upper()+"****",end='\n')
            print("\nSelect one option below ")
            print("\n\t1-->Deposit")
            print("\n\t2-->Withdrawal")
            print("\n\t3-->View Profile")
            print("\n\t4-->Update Profile")
            print("\n\t5-->Close Account")
            print("\n\t6-->Logout")
            ch=int(input("Enter your choice:"))
            
            if ch==1:
                self.deposit(acc)
                
            elif ch==2:
                self.withdraw(acc)
            
            elif ch==3:
                print("\nYour profile")
                self.search(acc)
            
            elif ch==4:
                self.update(acc)
                print("Login to Continue")
                break
            
            elif ch==5:
                yn=input("Do you readly wish to close your account ?(y/n)")
                if yn=='y':
                    self.delete(acc)
                    break
                else: print("We're Glad to hear that.\nContinue your session\n")
            
            elif ch==6:
                break

            
            else:
                print("\n Invalid option \n Please Try again")
def main():
    
    a=acc_query()
    a.create_pri_index()
    
    while(1):
        print("\n\n****ACCOUNT INFORMATION SYSTEM****",end='\n')
        print("\nSelect one option below ")
        print("\n\t1-->Add record to file")
        print("\n\t2-->Show record from file")
        print("\n\t3-->Search Record from file")
        print("\n\t4-->Update Record")
        print("\n\t5-->Delete Record")
        print("\n\t6-->Quit")
        choice=int(input("Enter your choice:"))
        
        if choice==1:
            a.write_rec()
            
        elif choice==2:
            a.display()
            
        elif choice==3:
            key=int(input("\nEnter the Account No. to be searched \n"))
            a.search(key)
            
        elif choice==4:
            key=int(input("\nEnter the Account No. who's record you wish to modify \n"))
            a.update(key)
            
        elif choice==5:
            key=int(input("\nEnter the Account No. who's record you wish to delete \n"))
            a.delete(key)
    
        elif choice==9:
            a.create_pri_index()
            print("\n\n",a.acc_list,"\n\n",a.addr_list,"\n\n",a.count,"\n\n",a.acc_no,"\n\n")
    
        elif(choice==6):
            break

if __name__ == "__main__":
    main()
    
