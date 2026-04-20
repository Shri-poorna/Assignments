n1=float(input("num1="))
n2=float(input("num2="))
def calc1(n1,n2):
    sum1=n1+n2
    dif=n1-n2
    prd=n1*n2
    if(n2!=0):
        div1=n1/n2
        div2=n1//n2
        rem1=n1%n2
    return sum1,dif,prd,div1,div2,rem1
result=calc1(n1,n2)
print(result)
