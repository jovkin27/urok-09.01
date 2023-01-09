from math import*
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
    year=int(year)
    if year%4==0:
        t=True
    else:
        t=False
    return t

#3
def ruud(a:float)->float:
    """
    P ruudu ümbermõõt, S ruudu pindala, d ruudu diagonaal
    :param float a: ruudu külg
    :rtype: float ruudu ümbermõõt
    :rtype: float ruudu pindala
    :rtype: float ruudu diagonaal
    """
    P=a*4
    S=a**2
    d=a*sqrt(2)
    return P,S,d

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
    S=a*(1+0.1)**years 
    return S

#6
def is_prime(a:float)->bool:
    """
    Liht- või kompleksarv
    :param a float: arv 0 kuni 1000
    :rtype: bool Funktsiooni vastus loogilises formadis 
    """
    if a <= 2:
        vas=False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            vas=True
    return vas


    #if a in range(0,1001):
    #    if a%a==1 and a/1==a:
    ##        vas=True
    ##    else:
    ##        vas=False
    ##else:
    ##    vas="lahjem kui 0 või surem kui 1000"
    ##return vas