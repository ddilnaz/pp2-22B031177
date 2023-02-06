def ounces(chislo):
    return 28.3495231 * chislo

grams = int(input())
ingredient = ounces(grams)
print( ingredient)  