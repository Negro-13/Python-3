print('Ingrese una tarea:')
tarea = {'Tarea':'', 'Descripcion': '', 'Fecha limite':'', 'Importanica': ''}
name = input()
tareas = []
while name != 'salir':
    tarea['Tarea'] = name

    print('Ingrese una descripcion:')
    descrip = input()
    tarea['Descripcion'] = descrip

    print('Ingrese una fecha limite:')
    fecha = input()
    tarea['Fecha limite'] = fecha

    print('Ingrese la importancia de la tarea:')
    importancia = input()
    tarea['Importanica'] = importancia

    tareas.append(tarea)

    print('Desea agragar mas tareas: si/no')
    option = input()
    if option == 'si':
        print('Ingrese nombre de tarea:')
        name = input()
    else:
        name = 'salir'

print(f'Tu lista de tareas es: {tareas}')
