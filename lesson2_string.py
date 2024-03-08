# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:22:05 2024

@author: Rustamov
"""

#1. 'Hello world' matniga o'zgaruvchi yuklang va print() yordamida konsolga ciq.
salamlash = 'Hello World'
print(salamlash)

#2. xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring,
#   keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "Bugungi yangliklarni kun.uz orqali bilib olsangoz bo'ladi."
print(xabar)
xabar = 'Kun.uz ishonchli axborot manbai.'
print(xabar)

#3.Quyidagi kodni bajaring:
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

#4. Quyidagi mashqlarni bajaring:
kocha="Bog'bon"
mahalla ='Sog\'bon'
tuman = 'Bodomzor'
viloyat = 'Samarqand'
print(kocha +'ko\'chasi ,' + mahalla + 'mahallasi,'+
     tuman + 'tumani,'+ viloyat +'viloyati')  
 
#5.Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini 
#foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
print('Iltimos ,quyidagi malumotlarni kiriting:')
kocha = input('Ko\'changiz:')
mahalla = input('Mahallangiz:')
tuman = input('Tumaningiz:')
viloyat = input('Viloyatiningiz:')
print(kocha +' \nko\'chasi ,' + mahalla + ' \nmahallasi,'+
    tuman + ' \ntumani,'+ viloyat +' \nviloyati')  

#6.Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan
# o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani,\
    {viloyat} viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())












