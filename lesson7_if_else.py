# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:10:46 2024

@author: Rustamov
"""

#1. Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat 
#   tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga 
#   chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
  
#2. Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
for car in cars:
    if car != 'gm':
       print(car.title())
    else:
        print(car.upper())
        
#3.Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz,
#  Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring
f_ismi = input('Ismingizni kiriting:')
if f_ismi.lower() == 'admin':
    print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yhatini ko\'rasizmi:')
else:
   print(f"Xush kelibsiz {f_ismi.title()}")    
   
#4.Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng 
#  bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1 = int(input('1-sonni kiriting:'))
son2 = int(input('2-sonni kiriting'))
if son1 == son2 :
    print('sonlar teng ekan.')
    
#5.Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa 
#konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

son = float(input('Istalgan son kiriting:')) 
if son >= 0:
    print(f"{son} bu son musbat")
else:
    print(f"{son} bu son manfiy")
    
#6. Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning 
# ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son 
# kiriting" degan xabarni chiqaring. 
son = float(input('Istalgan son kiriting:'))
print(son**(1/2)) if son >= 0 else print(input('Musbat son kiriting:'))

















    


    
