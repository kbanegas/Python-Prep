class Herramientas:
    def __init__(self, listaNumeros1):
        if type(listaNumeros1) != list:
            self.lista=[0]
            raise ValueError('Se ha creado con un elemento cero, se esperaba una lista de numeros')
        else:
            self.lista=listaNumeros1
    
    '''
    devuelve los valores de la lista 
    que son primos restandole los que no lo son
    acumulados en la lista valores
    
    '''
    def numeroPrimo2(self):
        valores=[]
        #es_primo = True
        for nro in self.lista:
            for i in range(2, nro):
                if nro % i ==0:
                    valores.append(nro)
                    #es_primo = False
                    break                
        # SetA=set(self.lista)
        # SetB=set(valores)
        # acumPrimos=list(SetA-SetB)  
        acumPrimos=[elem for elem in self.lista if elem not in valores]        
        return acumPrimos
    
    def numeroPrimo1(self,nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo 

    def VerificanumeroPrimo1(self):
        lista_primos = []
        for i in self.lista:
            if (self.numeroPrimo1(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos
        

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
            maxvalor=[0]
            maxveces=[0]
            minvalor=[0]
            minveces=[0]
            return(maxvalor,maxveces,minvalor,minveces) 
        else:
            maxvalor=[max(acumularepetidos)]
            maxveces=[max(acumulaveces)]
            minvalor=[min(acumularepetidos)]
            minveces=[min(acumulaveces)] 
        #Eleccion=int(input("Digite 1 para el menor y 2 para el mayor"))
        if Eleccion==True :
            if len(acumulaveces)!=0:
                print("el valor",minvalor, "se repite", minveces,"veces")
        elif Eleccion==False:
            if len(acumulaveces)!=0:
                print("el valor",maxvalor, "se repite", maxveces,"veces")
            
        return(maxvalor,maxveces,minvalor,minveces)            

 # conversion grados
    def convierte(self,i, origen, destino):
        # valor=float(input("ingrese el valor a convertir"))
        # origen=int(input("De que se trata la medida? digite 1 Celcius,2 Farenheit,3 Kelvin"))
        # destino=int(input("De que se trata la medida? digite 1 Celcius,2 Farenheit,3 Kelvin")
        valoresEsperados=[1,2,3]
        lista_vacia=[]
        valor_destino=None
        if origen not in valoresEsperados and destino not in valoresEsperados:
            print("Valor esperado para origen (1 Celsios,2 Farenheit, 3 Kelvin)")
            print("Valores esperados para destino (1 Celsios, 2 Farenheit, 3 Kelvin)")
            return lista_vacia
        elif origen not in valoresEsperados:
            print("Valor esperado para origen (1 Celsios,2 Farenheit, 3 Kelvin)")
            return lista_vacia
        elif destino not in valoresEsperados:
            print("Valores esperados para destino (1 Celsios, 2 Farenheit, 3 Kelvin)")
            return lista_vacia
        if origen==1 and destino==2:
            valor_destino=round((i * (9/5))+32,2)
        elif origen==1 and destino==3:
            valor_destino=round((i+273.15),2)
        elif origen==1 and destino==1:
            valor_destino=round(i,2)
            print("el valor de conversión es igual a el mismo")
        elif origen==2 and destino==1:
            valor_destino=round((i-32)*9/5,2)
        elif origen==2 and destino==3:
            valor_auxiliar=(i * (9/5))+32
            valor_destino=round(valor_auxiliar+273.15,2)
        elif origen==2 and destino==2:
            valor_destino=round(i,2)
            print("el valor de conversión es igual a el mismo")
        elif origen==3 and destino==1:
            valor_destino=round(i-273.15,2)
        elif origen==3 and destino==2:
            valor_auxiliar=i-273.1
            valor_destino= round((i * (9/5))+32,2)
        elif origen==3 and destino==3:
            valor_destino==round(i,2)
            print("el valor de conversión es igual a el mismo")
        else:
            print("valores incorrectos")
        if origen==1:
            origen= str("Celsios")
        elif origen==2:
            origen= str("Farenheit")
        elif origen==3:
            origen= str("Kelvin")
        if destino==1:
            destino= str("Celsios")
        elif destino==2:
            destino= str("Farenheit")
        elif destino==3:
            destino= str("Kelvin")    
        if type(valor_destino)==float:
            print (" Convirtiendo", i, origen,"a",destino, "su resultado es", valor_destino)
            return (valor_destino)
        else:
            return None
   
#para crear una lista de resultados de varios valores ingresados.
    def CTemperturaL(self, origen, destino):
        lista_conversion=[]
        for i in self.lista:
            lista_conversion.append(self.convierte(i,origen,destino))
        return lista_conversion
#factorial

    def __factorial(self, numero):
            if(type(numero) != int):
                return 'El numero debe ser un entero'
            if(numero < 0):
                return 'El numero debe ser pisitivo'
            if (numero > 1):
                numero = numero * self.__factorial(numero - 1)
            return numero
    
    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial

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
