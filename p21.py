l=[10,20,0,40,0,50,0,50,12,40]
print("*"*40)
num=int(input("Enter your Number:"))#100
for x in l:
    if x==0:
        print("We can not any number with zero")
        continue
    print(num/x)