a = string(input())
d = string(input())
c\ = string(input())
bool m = 0
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
