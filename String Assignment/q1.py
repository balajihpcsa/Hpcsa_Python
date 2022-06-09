''''''
'''
1. Given a string of odd length greater than 7, return a new string made of the middle three 
characters of a given String
Given:
str1 = "RakeshzipPetabb"
Output
 zip
str2 = "JazzbonAyxx"
Output
bon
'''
str1 = "RakeshzipPetabb"
str2 = "JazzbonAyxx"
lstr1 = len(str1)
lstr2 = len(str2)
print(str1[lstr1 // 2 - 1:lstr1 // 2 + 2])
print(str2[lstr2 // 2 - 1:lstr2 // 2 + 2])