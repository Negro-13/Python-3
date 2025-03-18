print('Ingrese palabras, cuando termine ponga "fin" :')
palabra = input()
palabras = []
def countwords(palabra):
    count = 0
    while palabra.lower() != 'fin':
        print('Ingrese otra palabra')
        count += 1
        palabras.append(palabra)
        palabra = input()
    return count

print(f'Tienes una lista de: {countwords(palabra)} palabras')
print(f'Su lista es: {palabras}')