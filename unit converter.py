# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:34:14 2021

@author: trupti
"""


x=input("Enter the unit you want to convert from: ")
y=input("Enetr the unit you want to convert to: ")

z=float(input("Enter the value: "))

if x=="cm" and y=="m":
   a=float(z)/100
   print(a)
   
if x=="m" and y=="cm":
    a=float(z)*100
    print(a)
    
if x=="mm" and  y=="cm":
    a=float(z)/10
    print(a)
    
if x=="cm" and y=="mm":
   a=float(z)*10
   print(a)

if x=="mm" and y=="m":
   a=float(z)/1000
   print(a)

if x=="m" and y=="mm":
   a=float(z)*1000
   print(a)


if x=="m" and y=="km":
   a=float(z)/1000  
   print(a)


if x=="km" and y=="m":
    a=float(z)*1000 
    print(a)
    
if x=="mm" and y=="km":
   a=float(z)/1000000  
   print(a)


if x=="ft" and y=="inches":
    a=float(z)*12
    print(a)
    
if x=="ft" and y=="cm":
   a=float(z)*30.48
   print(a)

if x=="inch" and y=="cm":
   a=float(z)*2.54
   print(a)

if x=="inch" and y=="mm":
   a=float(z)*25.4
   print(a)

    
   
   
