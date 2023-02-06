def logic( chislo_golov , chislo_nogi ):
    NO = 'ERROR'
    for i in range (chislo_golov + 1):
        k = chislo_golov - i
        if 2 * i + 4 * k == chislo_nogi:
            return i , k
    return NO,NO
chislo_golov = 34
chislo_nogi = 95
otvet = logic(chislo_golov , chislo_nogi)
print(otvet)
