from math import*
from datetime import date, datetime
#1
def arithmetic(a1:int,sym:str,a2:int):
    """Lihtne kalkulator
    + - liitmine, - lahutamine, * korrutamine, / jagamine
    :param float a1: Esimine arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :trype: var Määramata tüüp
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+sym+str(a2))
    else:
        vas="Tundmatu tehe!"
    return vas

#2
def is_year_leap(year:int)->bool:
    """
    Leap year or not
    :param int year: Aasta number
    :rtype: bool Funktsiooi vastus loogilises formadis
    """
    if year==int(year) and year>0:
        if year%4==0:
            t=True
        else:
            t=False
        return t
    else:
        print("Aasta peab olema täisarv ja positiivne arv")

#3
def ruud(a:float)->float:
    """
    P ruudu ümbermõõt, S ruudu pindala, d ruudu diagonaal
    :param float a: ruudu külg
    :rtype: float ruudu ümbermõõt
    :rtype: float ruudu pindala
    :rtype: float ruudu diagonaal
    """
    if a>=0:
        P=a*4
        S=a**2
        d=a*sqrt(2)
        return P,S,d
    else:
        print("Ruudu külg ei saa olla negatiivne")

#4
def season(kuu:int)->str:
    """
    Hooaeg
    :param int kuu: kuu arv
    :rtype: str Hooaeg nimetus
    """
    if kuu in range(3,6):
        hooaeg="kevad"
    elif kuu in range(6,9):
        hooaeg="suvi"
    elif kuu in range(9,12):
        hooaeg="sügis"
    elif kuu==12 or kuu==1 or kuu==2:
        hooaeg="talv"
    else:
        hooaeg="Aastas on ainult 12 kuud"
    return hooaeg

#5
def bank(a:float,years:int)->float:
    """
    Vklad v bank
    :param a float: Rahasumma
    :param years int: kestus
    :rtype: float Rahasumma
    """
    if a==float(a):
        if years==int(years):
            S=a*(1+0.1)**years 
            return S
        else:
            print("Tähtaeg ainult terved aastad")
    else:
        print("Summa viga")

#6
def is_prime(a:float)->bool:
    """
    Liht- või kompleksarv
    :param a float: arv 0 kuni 1000
    :rtype: bool Funktsiooni vastus loogilises formadis 
    """
    if a in range(0,1001):
        if a < 2:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True
    else:
        print("Arv ei ole vahemikus")

#7
def date(d:int,m:int,y:int)->bool:
    """
    Õige kuupäev
    :param d int: päev
    :param m int: kuu
    :paran y int: aasta
    :rtype: bool Funktsiooni vastus loogilises formadis 
    """
    try:
        datetime(y,m,d)
        return True
    except ValueError:
        return False

#8
def XOR_cipher(string, key):
    return ''.join([chr(ord(c)^key) for c in string])

def XOR_uncipher(string, key):
    return XOR_cipher(string, key)
    