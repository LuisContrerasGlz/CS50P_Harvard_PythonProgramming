def area_rectangulo(an,al):
    return an*al

def area_triangulo(ba,al):
    return (ba*al)/2

def area_circulo(radio):
    return (3.1416*radio*radio)

def area_paralelogramo(base,altura):
    return (base*altura)

def area_trapecio(base1,base2,altura):
    return ((base1+base2)/2)*altura

def area_elipse(eje_may,eje_men):
    return (3.1416*eje_may*eje_men)

def main():
    opc=""
    while (opc!="S"):
        print("Que figura quieres calcular ")
        print("<R>ectangulo ")
        print("<T>riangulo ")
        print("<C>irculo ")
        print("<P>aralelogramo ")
        print("<TR>apecio ")
        print("<E>lipse ")
        print("<S>alir ")
        opc=input().upper()
        if (opc=="R"):
            an=int(input("base "))
            al=int(input("alto "))
            area=area_rectangulo(an,al)
            print("Area ",area)
        elif (opc=="T"):
            ba=int(input("base "))
            al=int(input("alto "))
            area=area_triangulo(ba,al)
            print("Area ",area)   
        elif (opc=="C"):
            radio=int(input("radio "))
            area=area_circulo(radio)
            print("Area ",area)
        if (opc=="P"):
            base=int(input("base "))
            altura=int(input("alto "))
            area=area_paralelogramo(base,altura)
            print("Area ",area)
        if (opc=="TR"):
            base1=int(input("base1 "))
            base2=int(input("base2 "))
            altura=int(input("alto "))
            area=area_trapecio(base1,base2,altura)
            print("Area ",area)
        if (opc=="E"):
            eje_may=int(input("Eje mayor "))
            eje_men=int(input("Eje menor "))
            area=area_elipse(eje_may,eje_men)
            print("Area ",area)


    