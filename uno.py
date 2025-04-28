notas = []

while True:
    print("Este programa calcula el promedio de notas")
    entrada = input("Ingresá 3 notas por lo menos (o escribí 'fin' para terminar): ")

    if entrada.lower() == 'fin':
        if len(notas) >= 3:
            break
        else:
            print("Tenés que ingresar al menos 3 notas antes de terminar.")
            continue

    if entrada.isdigit():
        nota = int(entrada)

        if nota < 1 or nota > 10:
            print("Solo notas del 1 al 10.")
            continue

        notas.append(nota)

    else:
        print("Ingresá un número válido o 'fin'.")

if len(notas) >= 3:
    promedio = sum(notas) / len(notas)
    print(f"El promedio fue {promedio:.2f}")
else:
    print("No se cargaron suficientes notas")

