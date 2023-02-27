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


#valor hora
a  = 5000
b = 10000
c = 20000
salario_tope = 1500000

print('el valor de la hora de trabajo en el proyecto a')
print(a)

print('el valor de la hora de trabajo en el proyecto b')
print(b)

print('el valor de la hora de trabajo en el proyecto c')
print(c)

#salario mensual
salario_1 = (a*8)*30
print('el salario mensual del proyecto A')
print(salario_1)

salario_2 = (b*8)*30
print('el salario mensual del proyecto B')
print(salario_2)

salario_3 = (c*8)*30
print('el salario mensual del proyecto C')
print(salario_3)

if salario_3 > salario_tope:
    print('Salario es mayor a tope máximo')
else:
    print('pagarle al empleado por concepto de hora extra el valor de la hora día incrementada en un 6%')
