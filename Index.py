# -*- coding: utf-8 -*-
"""
Created on Fri May  4 11:02:25 2018

@author: ADITYA
"""

import customer,admin
a=customer.acc_query()
ad=admin.admin()

while 1:

    print("\n\n**** WELCOME TO PUPPO BANK **** \n \n\t1-->Login \n\t2-->Sign up \n\t3-->Admin Login \n\t4-->Admin Sign up \n\t5-->Exit")
    ch=int(input("Enter your choice :"))
    
    if ch == 1:
       a.login()
    elif ch == 2:
        a.write_rec()
    elif ch == 3:
        ad.login()
    elif ch == 4:
        ad.write_rec()
    elif ch == 5:
        break
    else:
        print("\n Invalid option \n Please Try again")


