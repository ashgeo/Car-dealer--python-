#!/usr/bin/python

#Program to save all details in a text file(sales.txt)

# Additional bonus rates saved in additionalBonusRates.txt

# Program calculate total sales, bonus rates additional bonus rates of each car

# Proram reads datas from sales.txt file and display as out put

import sys

def compute(sale,persent): #function to compute bonus

 return(sale*persent/100)

def calculateadditionalbonus(bonus,extra): #function to calculate additional 

bonus

 return (bonus*extra)

def total_additional_bonus(xn,yn,zn): #calculating total additional bonus 

 t_n = xn +yn + zn

 print ("Total Adiitional Bonus is",t_n)

 return t_n

def calculate_total_bonus(bonus,t_n): #calculating total bonus distributed 

by ABC

 bonus_n=bonus+t_n

 print ("Total Bonus distributed is",bonus_n)

# function to enter all details of car and saves in a file called sales .txt

def addi(): 

 try:

 orig_stdout = sys.stdout

 f = file('sales.txt', 'a')#File with appending mode

 sys.stdout = f

 print ("Enter Year")

 sys.stdout =orig_stdout

 print ("Enter Year")

 sys.stdout = f

 year = int(raw_input())

 print year

 print ("Enter Sales Price For Toyata $")

 sys.stdout =orig_stdout

 print ("Enter Sales Price For Toyata $")

 sys.stdout = f

 toyota=int(input())

 print ("Enter Sales Price For Nissan $")

 sys.stdout =orig_stdout

 print ("Enter Sales Price For Nissan $")

 sys.stdout = f

 nissan=int(input())

 print ("Enter Sales Price For Ford $")

 sys.stdout =orig_stdout

 print ("Enter Sales Price For Ford $")

 sys.stdout = f

 ford=int(input())

 print ("Enter Number Of Sales For Toyata")

 sys.stdout =orig_stdout

 print ("Enter Number Of Sales For Toyata")

 sys.stdout = f

 to=int(input())

 print ("Enter Number of Sales For Nissan")

 sys.stdout =orig_stdout

 print ("Enter Number of Sales For Nissan")

 sys.stdout = f

 ni=int(input())

 print ("Enter Number Of Sales For Ford")

 sys.stdout =orig_stdout

 print ("Enter Number Of Sales For Ford")

 sys.stdout = f

 fo=int(input())

 #f=open('sales.txt','w') # file open for writing data to file

 except ValueError:

 print ("Enter An Integer")

 sys.exit()

 sales= ((toyota*to)+(nissan*ni)+(ford*fo)) #calculating total sales of abc

 ct=(toyota*to) # total sells toyata

 cn=(nissan*ni) # total sells nissan

 cf=(ford*fo) # total sells toyata

 print ("Contribution Of Toyota $",ct,"in Total Sales")# display contribution 

amount of toayota kluger

 print ("Contribution Of Nissan $",cn,"in Total Sales")# display contribution 

amount of Nissan patrol

 print ("Contribution Of Ford $",cf,"in Total Sales")# display contribution 

amount of ford territory

 print ("Total Sales for ABC",sales)

 #calculating bonus from different category 

 if sales <= 500000:

 bonus=compute(sales,0.1)

 elif sales >=500001 and sales <=1000000:

 bonus=compute(sales,0.2)+500

 elif sales >=1000001 and sales <=5000000:

 bonus=compute(sales,0.3)+1500

 elif sales >=500001 and sales <=10000000:

 bonus=compute(sales,0.4)+13500

 elif sales >10000000:

 bonus=compute(sales,0.5)+33500

 print ("Total Bonus\n",bonus) #print total bonus

 cty=(ct*bonus)/sales #bonus contribution toyata

 cny=(cn*bonus)/sales #bonus contribution nissan

 cfy=(cf*bonus)/sales #bonus contribution toyata

 print ("Contribution Of Toyota $",cty,"in Total Bonus")

 print ("Contribution Of Nissan $",cny,"in Total Bonus")

 print ("Contribution Of Ford $",cfy,"in Total Bonus")

 stack=[]

 f1=open('additionalBonusRates.txt','r')# file open with reading mode

 for mn in f1:

 stack.append(mn)

 #print ("Input the Additional bonus for toyota in %")

 x=float(stack[1])

 #print ("Input the Additional bonus for Nissan in %")

 y=float(stack[1])

 #print ("Input the Additional bonus for Ford in %")

 z=float(stack[2])

 #Passing values

 xn= calculateadditionalbonus(bonus,x)

 yn= calculateadditionalbonus(bonus,y)

 zn= calculateadditionalbonus(bonus,z)

 print("Additional Bonus for toyota Kluger",xn)# printing additional bonus from 

Toyota kluger

 print("Additional Bonus for nissan Patrol",yn) #printing additional bonus from 

Nisan Patrol

 print("Additional Bonus for ford Territoary",zn)#printing additional bonus from 

Ford Territory

 tn=total_additional_bonus(xn,yn,zn)

 calculate_total_bonus(bonus,tn)

 sys.stdout = orig_stdout

 f.close()# file closing 

#Search the data for year user entered

def search(): 

 f=open('sales.txt','r')# Open file for reading

 lines=f.readlines()

 i=0

 print ("Enter Year ")# enter Year for search

 sr=raw_input()

 #print list

 while(1):

 if i%21==1:

 ty=lines[i]

 ty=ty[0:-1]

 if ty == sr:

 for j in range(i,i+20):# print out put as per the year entered

 print lines[j]

 i=i+1

 if i >= len(lines):

 break

 f.close()

# Delete data from file 

def delete(): 

 f = open('sales.txt','r')# Open File sales.txt for reading

 lines=f.readlines()

 i=0

 print ("Enter Year ")#ENter year to delete datas for that year

 sr=raw_input()

 while(1):

 if i%21==1:

 ty=lines[i]

 ty=ty[0:-1]

 if ty == sr: 

 f = open('sales.txt', 'w').writelines(lines[i,i+20])#Deleting datas line by line

 i=i+1

 if i >= len(lines):

 break

 f.close()

 print ("Sucessfully deleted")# data sucessfully deleted form the file

while(1):

 print (" Press A to add S to search D to Delete Q to quit")#Input mode for 

diffeent operations.

 pin= raw_input()

 if pin =='A':

 addi()

 elif pin =='S':

 search()

 elif pin=='D':

 delete()

 elif pin =='Q':

 exit()

 print ("Enter Y to Calculate for another Year or N to Exit")

 var= raw_input()

 if var == 'Y':

 addi()

 elif var == 'N':

 pass