# Hola mundo con python
# Salida por consola

'''
    print("Hola mundo, soy Andrés")
    print('Hola mundo, soy Andrés')

'''

# Entradas
# Datos primitivos
dato     = None
nombre   = 'Andrés'
edad     = 26
estatura = 1.78
estaVivo = True

# Salida por teclado
print( 'Hola, soy', nombre, 'y tengo', edad )
print( f'Hola, soy { nombre } y tengo { edad }' )

# Recibir datos por teclado
ciudad = input('Digite la ciudad donde vives: ')
print( f'La ciudad donde vives es: { ciudad }' )

# Recivir datos numericos por teclado
numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese un numero: '))

print( f'El numero uno es: { numero1 } y el numero dos es: { numero2 }' );

# Operadores alitmeticos
# Basicos( +, -, *, /, % )
suma = numero1 + numero2
print( f'La suma del numero1 + numero2 es { suma }' )