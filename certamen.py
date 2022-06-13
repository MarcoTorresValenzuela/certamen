numero_bultos=0
peso_avion=0
costo=0
ingreso=0
numero_equipaje=0
suma=0
pesomax=0
while peso_avion<=2000:
  peso = int(input("peso de equipaje: "))
  if peso >0 and peso <=500:
    peso_avion=peso_avion+peso
    if peso_avion<=2000:
      if peso<=25:
        costo=peso*1000
        ingreso=costo+ingreso
        numero_equipaje=numero_equipaje+1
        suma=peso+suma
        if pesomax<=peso:
           pesomax=peso
        print("hola su costo es de",costo,"pesos")
      elif peso>25 and peso<=300:
        costo=peso*1500
        ingreso=costo+ingreso
        numero_equipaje=numero_equipaje+1
        suma=peso+suma
        if pesomax<=peso:
           pesomax=peso
        print("hola su costo es de",costo,"pesos")
      else :
        costo=peso*2000
        ingreso=costo+ingreso
        numero_equipaje=numero_equipaje+1
        suma=peso+suma
        if pesomax<=peso:
           pesomax=peso
        print("hola su costo es de",costo,"pesos")
    else :
        print("el peso ya a sido sobrepasado no se aceptan mas equipajes")
  else :
      print("hola el peso de equipaje no debe superar los 500kg y tampoco ser un valor negativo porfavor ingrese otro equipaje con peso entre 0 y 500kg55")

peso_avion = peso_avion-peso
promedio = suma/numero_equipaje
bulto_mas_pesado = pesomax

print("el ingreso total :",ingreso,"pesos")
print("el peso total es de : ",peso_avion,"kg")
print("total de equipajes: ",numero_equipaje)
print("promedio: ",promedio,"kg")
print("bulto mas pesado : ",bulto_mas_pesado,"kg")
