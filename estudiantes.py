# Ejercicio 1 --pagina 6

#Datos de entrada

nombre_estudiante = input("Nombre del estudiante ")
id_estudiante = input ("Id del estudiante  ")
nota1, nota2, nota3 = input ("Ingrese nota de los 3 talleres con espacios "). split()
eval1, eval2 = input ("Ingrese nota de las 2 evaluaciones con espacios ").split()
nota_trabajo, sustentacion = input ("Ingrese notas de trabajo y sutentacion con espacios ").split()

#convertir de string a float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
eval1 = float(eval1)
eval2 = float(eval2)
nota_trabajo = float (nota_trabajo)
sustentacion = float(sustentacion)

#calculos de porcentajes
nota_talleres = (((nota1 + nota2 + nota3)/3) * 0.3)
nota_evaluaciones = (((eval1 + eval2)/2) * 0.3)
nota_trabajo_fin = (((nota_trabajo + sustentacion)/2) * 0.4)

nota_definitiva = nota_talleres + nota_evaluaciones + nota_trabajo_fin
print (f"La nota definitiva del estudiante {nombre_estudiante} es {nota_definitiva}:.2f")
