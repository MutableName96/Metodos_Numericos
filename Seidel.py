print("------------ Seidel ------------")

def solicitar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.replace('.', '', 1).replace('-', '', 1).isdigit() or (entrada[0] == '-' and entrada[1:].replace('.', '', 1).isdigit()):  
            return float(entrada) 
        else:
            print("Por favor, ingrese solo valores numéricos.")
print("Ingrese los valores de La Matriz Determinante")

a11=solicitar_numero("A[1,1]: ")
a12=solicitar_numero("A[1,2]: ")
a13=solicitar_numero("A[1,3]: ")
r1=solicitar_numero("C1: ")

a21=solicitar_numero("A[2,1]: ")
a22=solicitar_numero("A[2,2]: ")
a23=solicitar_numero("A[2,3]: ")
r2=solicitar_numero("C2: ")

a31=solicitar_numero("A[3,1]: ")
a32=solicitar_numero("A[3,2]: ")
a33=solicitar_numero("A[3,3]: ")
r3=solicitar_numero("C3: ")

x1=solicitar_numero("Introduce X: ")
y1=solicitar_numero("Introdice Y: ")
z1=solicitar_numero("Introduce Z: ")
j=1
relaj=1
contador = 0
while j == 1:
    i=0
    pin=1
    for i in range(5):
        contador+=1

        x2=x1
        x1=round((r1-a12*y1-a13*z1)/a11,4) 
        
        y2=y1
        y1=round((r2-a21*x1-a23*z1)/a22,4)

        z2=z1
        z1=round((r3-a31*x1-a32*y1)/a33,4)
        print(contador)
        x1=round(relaj*x1+(1-relaj)*x2,4)
        print("x= "+str(x1))
        y1=round(relaj*y1+(1-relaj)*y2,4)
        print("y= "+str(y1))
        z1=round(relaj*z1+(1-relaj)*z2,4)
        print("z= "+str(z1))
        if x1==x2 and y1==y2 and z1==z2:
            print("____________________________________________")
            print("____________________________________________")
            print("Las soluciones aproximadas son:  x   = "+str(x1)+"   y   = "+str(y1)+"   z   = "+str(z1))
            pin=2
            j=2
            break
        i+=1
        print("____________________________________________")
    
    while pin==1:
        print("¿Desea agregar un valor de ralajacion?, actualmente la relajacion es de "+str(relaj))
        print("1.-Si    2.-No")    
        res=int(input())
        if res!=1 and res!=2:
            print("Introduce 1 o 2")
        else:
            pin2=1
            if res==1:
                while pin2==1:
                    print("Cual sera la relajacion?: ")
                    relaj=float(input())
                    if relaj<=2 and relaj>0:
                        pin=2
                        pin2=2
                    else:
                        print("Ingrese una relajacion entre 0 y 2")
            if res==2:
                print("Procesando")
                pin=2
    
