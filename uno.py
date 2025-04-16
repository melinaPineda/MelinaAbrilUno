notas= []

while True:
    print("Este programa calcula el promedio de notas")
    nums = input("Ingresá 3 notas por lo menos (o escribí 'fin' para terminar): ")

    if nums.lower() == 'fin':
        break

    try:
        nota = int(nums)

        if nota < 0 or nota > 10:
            print("Solo notas del 1 al 10.")
            continue

        notas.append(nota)

        if len(notas) < 3:
            print("Tenés que ingresar al menos 3 notas.")
            continue

    except ValueError:
        print("Ingresá un número válido o poné 'fin'.")

    if len(notas) >= 3:
      promedio = sum(notas) / len(notas)
    print(f"El promedio fue {promedio}")
else:
    print("Minimo 3 notas para sacar el promedio.")
