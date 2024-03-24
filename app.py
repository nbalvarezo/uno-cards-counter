### Contador de cartas UNO ###

def contar_cartas(mano):
    # Creamos un diccionario para llevar la cuenta de las cartas
    conteo_cartas = {
        '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
        'Salta': 0, 'Reversa': 0, 'Roba Dos': 0, 'Comodín': 0, 'Comodín Roba Cuatro': 0
    }
   
    # Recorremos la mano y contamos las cartas
    for carta in mano:
        if carta in conteo_cartas:
            conteo_cartas[carta] += 1
        elif carta == 'Salta':
            conteo_cartas['Salta'] += 1
        elif carta == 'Reversa':
            conteo_cartas['Reversa'] += 1
        elif carta == 'Roba Dos':
            conteo_cartas['Roba Dos'] += 1
        elif carta == 'Comodín':
            conteo_cartas['Comodín'] += 1
        elif carta == 'Comodín Roba Cuatro':
            conteo_cartas['Comodín Roba Cuatro'] += 1
   
    # Devolvemos el diccionario con el conteo
    return conteo_cartas

# Ejemplo de uso de la función
mano_ejemplo = ['5', '3', 'Salta', '9', 'Comodín', '2', '2', 'Roba Dos', 'Comodín Roba Cuatro']
conteo = contar_cartas(mano_ejemplo)
print(conteo)