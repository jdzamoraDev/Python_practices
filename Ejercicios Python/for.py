print("********************************************************************")
print("Este es un algoritmo para calcular las notas de los estudiantes.")
x = int(input("Para cuántos alumnos desea calcular las notas?: "))

for i in range(1,x + 1 ,1):
    nombre = input(f"Dame el nombre del estudiante #{i}: ")
    print("Dame las notas en porcentajes!")
    ex1 = int(input("Nota I examen de 20%:"))
    ex2 = int(input("Nota II examen de 40%:"))
    proy = int(input("Nota proyecto de 30%:"))
    tarea = int(input("Nota Tareas de 10%:"))
    nota = ex1 + ex2 + proy + tarea

    print("El estudiante ",nombre,"tiene una nota de",nota)
    print("********************************************************************")
    print(" ")
    
print("*********************")
print("* Fin del programa. *")
print("*********************")
