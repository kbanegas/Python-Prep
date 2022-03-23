class Herramientas:
    def __init__(self, listaNumeros1):
        self.lista=listaNumeros1
    
    def numeroPrimo1(self):
        # valor=(int(input("Digite número")))
        nPrimo=True
        numero=0
        for i in self.lista:
            while numero< i:
                if i%2==0:
                    nPrimo =False
                    break
                numero+=1
                nPrimo=True
            return (nPrimo)

# valor modal
    def Modal (self,Eleccion):
        #listaNumeros2= []
        acumularepetidos=[]
        acumulaveces=[]
        if len(self.lista)==0:
            return None
        nveces=0
        #Numero=int(input("¿Cuantos numeros va digitar?"))
        #for  elem in range(Numero):
            #num1=int(input("Digite un numero"))
            #listaNumeros2.append(num1)
        for n in self.lista:
            if n not in acumularepetidos and  self.lista.count(n)>1 :
                acumularepetidos.append(n)
                nveces=self.lista.count(n)
                acumulaveces.append(nveces)
        if len(acumularepetidos)==0 and len(acumulaveces)==0:
            print("No hay repetidos")
            return None
        else:
            maxvalor=[max(acumularepetidos)]
            maxveces=[max(acumulaveces)]
            minvalor=[min(acumularepetidos)]
            minveces=[min(acumulaveces)]
        #Eleccion=int(input("Digite 1 para el menor y 2 para el mayor"))
        if Eleccion==True or len(acumulaveces!=0):
            print("el valor",minvalor, "se repite", minveces,"veces")
        elif Eleccion==False or len(acumulaveces)!=0:
            print("el valor",maxvalor, "se repite", maxveces,"veces")
        else: 
            print("No hay valores maximos ni minimos")
            maxvalor=0
            maxveces=0
            minvalor=0
            minveces=0
        return(maxvalor,maxveces,minvalor,minveces)            

 # conversion grados
    def convierte(self, origen, destino):
        # valor=float(input("ingrese el valor a convertir"))
        # origen=int(input("De que se trata la medida? digite 1 Celcius,2 Farenheit,3 Kelvin"))
        # destino=int(input("De que se trata la medida? digite 1 Celcius,2 Farenheit,3 Kelvin"))
        for i in self.lista:
            if origen==1 and destino==2:
                valor_destino= (i * (9/5))+32
            elif origen==1 and destino==3:
                valor_destino=i+273.15
            elif origen==1 and destino==1:
                valor_destino=i
            elif origen==2 and destino==1:
                valor_destino=(i-32)*9/5
            elif origen==2 and destino==3:
                valor_auxiliar=(i * (9/5))+32
                valor_destino=valor_auxiliar+273.15
            elif origen==2 and destino==2:
                valor_destino=i
            elif origen==3 and destino==1:
                valor_destino= i-273.15
            elif origen==3 and destino==2:
                valor_auxiliar=i-273.1
                valor_destino= (i * (9/5))+32
            elif origen==3 and destino==3:
                valor_destino==i
            else:
                print("valores incorrectos")
            if origen==1:
                origen= str("Celsios")
            elif origen==2:
                origen= str("Farenheit")
            elif origen==3:
                origen= str("Kelvin")
            
            print(" Convirtiendo", i, origen, "su resultado es", valor_destino)
            return (valor_destino)    


#factorial

    def factoreal(self):
        #valor=int("Digite un numero")
        factorial=1
        for i in self.lista:
            for factor in range(1,i+1):
                factorial*=factor
            return factorial

    #factoreo
    def factoreo (self):
    # n=int("Digite un numero")
        for  i in self.lista:
            if i>0:
                listaMultiplos=[]
                print('Numero ', i, 'Multiplos')
                pr = 2
                primo2 = True
                while (pr <= i):
                    for div in range(2, pr):
                        if (pr % div == 0):
                            primo2 = False
                            break
                    if (primo2):
                        if i==pr:
                            listaMultiplos.append(pr)
                            # print("             ", pr)
                            break
                    while i % pr == 0:
                        i /= pr
                        listaMultiplos.append(pr)
                        # print("             ", pr)
                    # print(n)
                    else:
                        primo2 = True
                        pr += 1           
            else:
                print('Digite un número mayor que cero') 
            return(listaMultiplos)
