#1
from funktsioonid import arithmetic

answer=arithmetic(2.5,"+",1.8)
print(answer)
answer=arithmetic(input(),input(),input())
print(answer)

#2
from funktsioonid import is_year_leap

year=is_year_leap(int(input()))
print(year)

#3
from funktsioonid import ruud

answer=ruud(float(input()))
print(answer)

#4
from funktsioonid import season

hooaeg=season(int(input()))
print(hooaeg)

#5
from funktsioonid import bank

Saadud_summa=bank(float(input()),int(input()))
print(round(Saadud_summa,2))

#6
from funktsioonid import is_prime
answer=is_prime(input())
print(answer)