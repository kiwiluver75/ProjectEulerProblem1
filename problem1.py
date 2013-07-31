#Python 2.7

count = 0;

for x in range(0,1000):
  if x % 3 == 0 or x % 5 == 0:
    count += x;

print(count)
