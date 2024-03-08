# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:18:26 2024

@author: Rustamov
"""

#1. Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har 
#   bir ismga takrorlanuvchi xabar yozing.
ismlar = ['Bobur','Sulaymon','Norboy','Farruh','Tursunbek']
for ism in ismlar:
    print(f' Assalomu alaykum {ism}. Sahifamga xush kelibsiz.')
    
#2. Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan
#   xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print('Kod', len(ismlar),'marta takrorlandai.')        

#3. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir
#   elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(f'{son} ning kubi = ', son**3)
    
#4. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar
#   degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
print('5 ta eng sevimli kinongizni kiriting.')
kinolar = []
for n in range(5):
    kinolar.append(input(f'{n+1} - kino nomini kiriting:'))
    print(kinolar)

#5.Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) 
#  so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga
#  yozing. Ro'yxatni konsolga chiqaring.
n = int(input('Bugun nechta odam bilan suhbatlashdingiz?')) 
ismlar = []
for m in range(n):
    ismlar.append(input(f'{m+1}- odamning ismini kiriting '))
    print(ismlar)