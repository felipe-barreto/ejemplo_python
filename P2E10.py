imagenes = ['im1','im2','im3']
lista = [ [ [] , [(),(),()] ] , [ [] , [(),(),()] ] , [ [] , [(),(),()] ] ]
lista[0][0] = imagenes[0]
lista[1][0] = imagenes[1]
lista[2][0] = imagenes[2]
for i in range(3):
    print("Ingrese x1")
    x1 = input()
    print("Ingrese y1")
    y1 = input()
    repetir = True
    while(repetir):
        print("Ingrese x2")
        x2 = input()
        print("Ingrese y2")
        y2 = input()
        if ((x1 != x2) or (y1 != y2)):
            repetir = False
        else:
            print("Coordenada repetida")
    repetir1 = True
    while(repetir1):
        print("Ingrese x3")
        x3 = input()
        print("Ingrese y3")
        y3 = input()
        if (((x3 != x1) or (y3 != y1)) and ((x3 != x2) or (y3 != y2))):
            repetir1 = False
        else:
            print("Coordenada repetida")
    lista[i][1][0] = (x1,y1)
    lista[i][1][1] = (x2,y2)
    lista[i][1][2] = (x3,y3)
print(lista)
