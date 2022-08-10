#Sual:1.(Asan) Girilən ədədin faktorialını tapan kod hazırlayın.
#Cavab:
# number = int (input("Faktoryalini tapmaq istediyiniz ededi daxil edin...\n"))
# factorial = 1
# i=1
# if number >= 0:
#   while i <= number:
#       factorial*=i
#       i+=1
#   print("Daxil etdiyiniz ededin faktoriyali:",factorial)
# else:
#   print ("Menfi ededin faktoriyali yoxdur!")
#==================================================

#Sual:2.(Orta) İstifadəçinin girdiyi cümlədə neçə heca olduğunu deyən program hazırlayın. Hecaların sayını tapmaq üçün saitlərdən istifadə edin.
#Cavab:
# cumle = input("cumleni daxil edin: ")
# result = ''
# saitler = 'aioue'
# for char in cumle:
#     if char in saitler:
#         result += char

# print(str(len(result)))
# Sual:3.İstifadəçidən nömrə istəyən bir program hazırlayın. Nömrələr +994 ilə başlamalı və uzunluğu 13 ədəddən ibarət olmalıdı. İlk characteri olan + çıxmaq şərtilə ancaq ədədlərdən ibarət olmalıdır. Əgər istifadəçi səhv yazarsa istifadəçiyə səhfini bildirib, yenidən soruşun. Bunu etmək üçün while istifadə edin. İstifadəçi düzgün yazdıqda isə break edib, ardından məlumatın düzgün olduğunu bildirin. Əgər istifadəçi məlumatı girən zaman sağda solda boşluq buraxarsa həmin boşlquqları silin.
# Cavab:

# import re
# nomre = input('Nomre girin: ')

# match = re.match('^\+994(50|51|70|77|55)\d{7}$', nomre)
# while match:
#     print('Nomre duzgundur!')

# else:
#     print('Nomre sehvdir!!!')
#==================================================

#Cavab:4
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# while a:
#     print(a.pop(), 'saniye')
# else:
#     end=print("Vaxt Bitdi!\n")
#==================================================

#Cavab:5
# from __future__ import division
# import math
# eded = int(input("Ededi daxil edin : "))

# for eded in range(eded + 1):
#    if eded > 1:
#        for i in range(2,eded):
#            if (eded % i) == 0:
#                break
#        else:
#            print(eded)
#===============================================

#Cavab:6
# fibolar = int(input("Ededi daxil edin: "))
# n_1 = 0  
# n_2 = 1  
# count = 0

# while count < fibolar:  
#         print(n_1)  
#         nth = n_1 + n_2
#         n_1 = n_2  
#         n_2 = nth  
#         count += 1