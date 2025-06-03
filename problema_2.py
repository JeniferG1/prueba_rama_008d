num1 = 0
num2 = 0

num1 =  int(input("Ingrese el primer número "))
num2 =  int(input("Ingrese el segundo número "))

if num1 > num2:
   print("ERROR: El número 1  es mayor que el número 2 ")
else:
   punto_medio = (num1+num2) / 2 
   ajuste = (num2 - num1) * 0.2

   aleatorio =  punto_medio + ajuste

   numero = int(input("Ingrese un número "))

   if aleatorio == numero:
      print("Felicidades.  Asertó el número ")
   else:
      if numero >  aleatorio:
         print("El número es mayor que el numero a adivinar")
      else:
         print("El número es menor que el numero a adivinar")
      numero2 =  int(input("Ingrese el número "))
      if aleatorio == numero2:
            print("Felicidades.  Asertó el número ")
      else:
        if numero2 >  aleatorio:
             print("El número es mayor que el numero a adivinar")
        else:
             print("El número es menor que el numero a adivinar")
        print("Otra pista")
        if abs(numero - aleatorio) < abs(numero2 - aleatorio):
            print("El primer número estaba más cerca")
        elif abs(numero - aleatorio) > abs(numero2 - aleatorio): 
            print("El segundo  número estaba más cerca")
        else:
            print("Los números ingresados están a la misma distancia")
      
        numero3 =  int(input("Ingrese el número "))
        if aleatorio == numero3:
            print("Felicidades.  Asertó el número ")
        else:
             print("Fallaste se terminaron las oportunidades")
        