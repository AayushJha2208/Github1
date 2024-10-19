print("----------------Diffrentiating a polynomial----------------")
print("\n")
print("Use the following instructions to write a polynomial")
print("1. Avoid spaces or unecessary symbols while writing the polynomial")
print("2. Write 'x' instead of writing 'x^1'")
print("3. Write polynomial in a single line")
print("4. The polynomial must be in 'x' and not in any other variable")
print("\n")
print("Sample format:")
print("-5x^6+3x^2-7x+8")
print("\n")
poly=input("Enter the polynomial here: ")
def diffrentiate(pol):
    a=[]
    l=pol.split("+")
    for el in l:
        if "-" in el:
            nel=el.split("-")
            nel[0]="+"+str(nel[0])
            for i in range(1,len(nel)):
                nel[i]="-"+str(nel[i])
            a.extend(nel)
        else:
            a.append("+"+str(el))
    if a[0]=="+":
        a.remove("+")
    nbl=[]
    for b in a:
        if 'x' not in b:
            nb=""
            nbl.append(nb)
        elif b=="+x":
            nbl.append("1")
        elif b=="-x":
            nbl.append("-1")
        elif b.endswith('x'):
            nb=b[0:-1]
            nbl.append(nb)
        else:
            lb= b.split("x^")
            s=lb[0]
            if len(s)==1:
                n1=1
            else:
                n1=int(s[1:])
            n2=int(lb[1])
            nn1=n1*n2
            nn2=n2-1
            if b.endswith('2'):
                nb=str(s[0])+str(nn1)+'x'
            elif 'x^1' in b:
                if b=="x^1":
                    nb=str(s[0])+str(1)
                else:
                    nb=b[0:-3]
                
            else:
                nb=str(s[0])+str(nn1)+'x^'+str(nn2)
            nbl.append(nb)
    dr=""
    for f in nbl:
        dr+=f
    if dr.startswith("+"):
        dr=dr[1:]
    if dr=="":
        dr="0"
    return dr        
print("\n")
r=diffrentiate(poly)
print("derivative of the polynomial is: ",r)
print("\n")
print("Thank you")
