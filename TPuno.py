notas = []

while len(notas) < 3: #este while es pra q el usuario ingrese las 3 notas, tipo, hasta no tener las 3, sigue preguntando
    nota = input(f"Ingresá la nota {len(notas)+1} (entre 0 y 10) o escribí 'fin' para terminar: ")

    if nota.lower() == "fin":
        break
    try: #sirve para que el codigo no c rompa si hay un erros (tipo, si en vez de 1 ponees i el try sirve para que el code no se rompa y siga)
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("La nota tiene que estar entre 0 y 10.")
    except ValueError: #una excepcion, cmo hay un error el coso te dice q te equivosta sin q se rompa el programa
        print("Eso no es un número válido.")

def calcula_promedio(lista):
    if len(lista) > 0:
        suma = 0
        for i in lista:
            suma += i
        promedio = suma / len(lista)
        print(f"El promedio de las {len(lista)} notas es {promedio:.2f}")
    else:
        print("No ingresaste ninguna nota.")

calcula_promedio(notas)


