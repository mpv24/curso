moneda_destino="peso colombiano"
dolar= "el valor del dolar es:"
valor_dolar= 4785.34
euro= "el valor del euro es:"
valor_euro= 5090
mexicano= "el valor del mexicano es:"
valor_mexicano= 265.94
sol= "el valor del sol es:"
valor_sol= 1272.44
wones= "el valor del wones es:"
valor_wones= 3.68

print ("ingresa tu nombre")
nombre= input ()

print('ingresa tu documento')
documento =  input ()

print('ingresa moneda de origen')
moneda_origen = input ()

print('ingresa cantidad de cambio:')
cantidad_cambio = input()

print('ingresa moneda de destino')
moneda_destino = input()

if moneda_origen == "dolar":
    porcentaje1 = valor_dolar * 0.07 
    print (porcentaje1)

elif moneda_origen =="euro":
   porcentaje2 = valor_euro * 0.10
   respuesta= input("desea continuar con el cambio: ")
   if respuesta =="si" : print("El usuario: " , nombre,", Con documento: " , documento,", Moneda de origen: " , moneda_origen, ", A moneda destino: ", moneda_destino,",   total: " , cantidad_cambio)
   if respuesta == "no" : print("cancelar cambio")

elif moneda_origen =="mexicano":
    porcentaje3 = valor_mexicano * 0.05 
    print (porcentaje3)

elif moneda_origen =="sol":
    porcentaje4 = valor_sol * 0.03
    print (porcentaje4)

elif moneda_origen =="wones":
  porcentaje5 = valor_wones * 0.02
  print (porcentaje5)

else:
 print("error, no existe la moneda")
