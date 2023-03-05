import itertools
soz = str(input())
teris_str = ''.join(reversed(soz))
if teris_str == soz:
    print("YES")
else:
    print("NO")