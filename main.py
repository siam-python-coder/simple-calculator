while True:
    a = float(input("Enter your number:"))
    c = input("enter your Operators(+,-,*,/):")
    b = float(input("Enter your 2 number:"))
    if c=="+":
        print(a,"+",b,"=",a+b)
    elif c=="-":
        print(a,"-",b,"=",a-b)
    elif c=="*":
        print(a,"*",b,'=',a*b)
    elif c=="/":
        print(a,"/",b,"=",a/b)