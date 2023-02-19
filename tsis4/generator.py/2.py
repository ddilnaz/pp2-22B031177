def even(san):
    i = 0
    while i <= san:
        if (i % 2 == 0):
            yield i
        i+=1
san = int(input())
for i in Even(n):
  if i < san - 1:
    print(i, end = ',' )
  else:
    print(i)