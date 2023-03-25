a=0
while a==0:
    opcion=int(input(''' Ingresa una opcion
    
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    Que opcion elijes'''))
    
    while opcion>0 and opcion<5:
        numero1=int(input('ingrese el primer numero'))
        numero2=int(input('ingrese el segundo numero'))
        
        if opcion==1:
            result=numero1+numero2
        
        elif opcion==2:
            result=numero1-numero2
        
        elif opcion==3:
            result=numero1*numero2
        
        else:
            result=numero1/numero2
        
        print("el resultado es :", result)
        
        opcion=int(input(''' Ingresa una opcion
        
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        
        Que opcion elijes'''))


print('Por favor ingresa una opcion valida')