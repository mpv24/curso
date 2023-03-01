"""boleta = 1

if boleta == 1 :
	print('boleta baja = 100')
elif boleta == 2:
	print('boleta general = 200')
elif boleta == 3:
	print('boleta preferencial = 400')
elif  boleta == 4:
	print('boleta vip = 500')
else:  
   print('error')
   """


#Empresa wc

#Valor hora
empleados = "Cuatro Empleados"
valor_hora_A = 20000
valor_hora_B = 10000
valor_hora_Otros = 5000
horas_laborales = 8

sueldo_A = valor_hora_A * horas_laborales * 30 
sueldo_B = valor_hora_B * horas_laborales * 30 
sueldo_Otros = valor_hora_Otros * horas_laborales * 30
horas_Extras = (valor_hora_Otros * 6/100 + valor_hora_Otros) *3
nuevo_sueldo = sueldo_Otros + horas_Extras

tipo_proyecto = 2

if tipo_proyecto == 1: 
    print ('Tipo de proyecto A, por tanto el valor de la hora es $20000')
    print ('El salario mensual da un total de:', sueldo_A)
    print ('Salario mensual es mayor al tope maximo')
elif tipo_proyecto == 2:
    print ('Tipo de proyecto B, por tanto el valor de la hora es $10000')
    print ('El salario mensual da un total de:', sueldo_B)
    print ('Salario mensual es mayor al tope maximo')
else:
    print ('Tipo de proyecto diferente A y B, por tanto el valor de la hora es $5000')
    print ('El salario mensual da un total de:', sueldo_Otros)
    print ('Nuevo sueldo mensual:', nuevo_sueldo)
