def calc2(n1,n2):
    list1=[]
    sum1=n1+n2
    prd1=n1*n2
    if(n2!=0):
        div1=n1/n2
        div2=n1//n2
    exp1=n1**n2
    list1.append(sum1)
    list1.append(prd1)
    list1.append(div1)
    list1.append(div2)
    list1.append(exp1)
    return list1

result=calc2(8,4)
print(result)
