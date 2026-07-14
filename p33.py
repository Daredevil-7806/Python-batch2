def calc():
    print("=====Simple calculator=====")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter Second number:"))
    op=input("Enter your operator:")
    if op=="+":
      res=num1+num2
      print("="*20)
      print("Sum is:", res)
      print("="*20)
    elif op=="-":
       res=num1-num2
       print("="*20)
       print("Sub is:",res)
       print("="*20)
    elif op=="*":
       res=num1*num2
       print("="*20)
       print("Multiplication is:",res)
       print("="*20) 
    elif op=="/":
       res=num1/num2
       print("="*20)
       print("div is:",res)
       print("="*20)  
    else:
       print("="*20)
       print("Please enter your valid operator..",res)
       print("="*20) 
for x in range(5):
   calc()         