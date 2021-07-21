from collections import Counter

str1 = 'анализ мочи'
str2 = 'мочи анализ общий'

print(set(str1.split()))
print(set(str2.split()))

if set(str1.split()).issubset(set(str2.split())):
    print('yes')
else:
    print('no')
