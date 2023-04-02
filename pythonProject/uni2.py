a = int(input())
b = int(input())
c = int(input())
string m = 0
m = a+b+c
if a*b+c > m:
    m = a*b+c
if a*(b+c) > m:
    m = a*(b+c)
if a+b*c > m:
    m = a+b*c
if (a+b)*c > m:
    m = (a+b)*c
if a*b*c > m:
    m = a*b*c
print(m)
