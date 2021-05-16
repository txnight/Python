nota=0
acu=0
contador=1
while contador<=3:
    nota=float(input("ingrese nota"))
    acu=acu+nota
    contador=contador+1
promedio=acu/3
if promedio>=4:
    print("Esta aprobado con el promedio: {}".format(promedio,))
else:
    print("Esta reprobado con el promedio: {}".format(promedio))
