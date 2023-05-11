import random
intentos = 8
nombre = str(input("Ingrese su nombre: "))
print(f'¡Bienvenido al Adivinador {nombre}!')
numero1 = int(random.randint(1, 100))
while intentos != 0:
 numero = float(input("Ingrese un numero del 1 al 100, tienes 8 intentos: "))
 if numero == (float):
  print("El numero ingresado no es un entero")
  continue
 elif numero < numero1:
  print("El Numero a adivinar es mayor")
  intentos -=1
  print (f'Intentos que le quedan: {intentos}')
  continue
 elif numero > numero1:
  print("el numero a adivinar es menor")
  intentos -=1
  print (f'Intentos que le quedan: {intentos}')
  continue
 elif numero == numero1:
  print(f"El numero es correcto!!! Lo pudiste hace en el intento:{intentos}")
  break
 elif numero != numero1:
  print ("Numero erroneo")
  intentos -= 1
  print (f'Intentos que le quedan: {intentos}')
  continue
else:
 print("Se te acabaron los intentos, lamentablemente no haz acertado :(")



