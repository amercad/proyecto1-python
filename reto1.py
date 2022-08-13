numero = int(input( 'Digite un número: ' ))

resultado = numero % 5

# Condicional simple

if ( resultado == 0  ):
    print( f'El numero { numero } es multiplo de de 5' )
else:
    print( f'El numero { numero } no es multiplo de 5' )
print( f'Fin del programa' )