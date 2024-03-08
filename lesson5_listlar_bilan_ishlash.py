# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:22:40 2024

@author: Rustamov
"""

#1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga 
#   chiqaring
davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", 
             "AQSh"]
print(davlatlar)

#2. Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#3. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga 
#  chiqaring
print(sorted(davlatlar))

#4. sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

5.#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga
#  teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200,2))

#9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))

#10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va
#    konsolga chiqaring
print(max(sonlar)-min(sonlar))

#11. Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))

#12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga 
#   chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

#13.taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#14.nonushta degan yangi ro'yxatga taomlardan nusxa oling.
nonushta = taomlar[:]

#15.Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va 
#   qo'shimcha 2 ta taom qo'shing.
nonushta.remove('osh')
nonushta.remove('norin')
nonushta.remove('qozonkabob')
nonushta.append('sari yog\'')
nonushta.append('kalbosa')

print(taomlar)
print(nonushta)

#16. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va 
#    nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta) 
nonushta = list(nonushta)     
nonushta[0] = ['qaymoq va non']
print(nonushta)
















