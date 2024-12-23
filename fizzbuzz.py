#Primero se establece el rango de numeros
for i in range(1, 101):
#Usamos la condicionales de if para verificar si cumple las condiciones que queremos.
    if i % 3 == 0:
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    if i % 5 == 0:
        print("buzz")
#usamos el "AND" dentro de la condicional para que nos imprima si se cumple las dos condicionales a la vez
    if i % 3 != 0 and i % 5 != 0:
        print("fizzbuzz")
    else:
        print(i)
