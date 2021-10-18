s=int(input("Input:"))
truth=0
for i in range(2, s):
    if s%i!=0:
        truth=1
    elif s%1==0:
        truth=0
if truth==1:
    print("Prime")
if truth==0:
    print("Not Prime")
