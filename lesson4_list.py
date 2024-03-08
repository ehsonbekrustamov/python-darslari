# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 03:32:15 2024

@author: Rustamov
"""
#1.mashq
ismlar = ['Ehsonbek' ,' Bobur' ,' Sulaymon'] 

print( 'Salom', ismlar[0] ,'bugun dars qilasanmi?')
print('Salom', ismlar[1] , 'bugun dars qildingmi?')
print('Salom' , ismlar[2] , 'bugun kursga boramizmi?')


#2.mashq

sonlar = [12 , 23 , -45 , 89 , -47 , 77 ,-34 , -21]

print(sonlar[5]+ sonlar[0])

sonlar.append(65)
print(sonlar)

sonlar.insert(5, 66)
print(sonlar)

sonlar.remove(-45)
print(sonlar)

del sonlar [1]
print(sonlar)


#3.mashq 
t_shaxslar =['Jaloliddin Manguberdi','Najmiddin Kubro','Al Xorazmiy']

z_shaxslar =['Islom Karimoov', 'Stiv Jobs', 'Bill Getes']

print('Men tarixiy shaxslardan', t_shaxslar.pop(2), 'bilan suxbat qurishni \
istardim')
      
print('Men zamonaviy shaxslardan',z_shaxslar.pop(0), 'bilan suxbat qurishni \
istarddim')      








