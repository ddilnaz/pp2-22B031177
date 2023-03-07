from datetime import datetime, timedelta
now=datetime.now().replace(microsecond=0)
n = int(input())
t = now - timedelta(n)
difference = now - t
print(difference.total_seconds())
