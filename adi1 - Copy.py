s=int(input("Input:"))
S=s
e=10**(len(str(s))-1)
rev=0
for i in range(len(str(s))):
    d=s%10
    s=s//10
    #print(d)
    rev+=(d*e)
    e=e/10
print(int(rev))
