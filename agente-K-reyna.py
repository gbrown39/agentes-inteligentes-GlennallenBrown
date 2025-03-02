def es_seguro(tablero, fila, col):
    for i in range(fila):
        if tablero[i][col] == 1:
            return False
    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = fila, col
    while i >= 0 and j < len(tablero):
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def resolver_n_reinas(tablero, fila):
    if fila >= len(tablero):
        return True
    for col in range(len(tablero)):
        if es_seguro(tablero, fila, col):
            tablero[fila][col] = 1
            if resolver_n_reinas(tablero, fila + 1):
                return True
            tablero[fila][col] = 0
    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(['Q' if x == 1 else '.' for x in fila]))

N = 3
tablero = [[0] * N for _ in range(N)]
if resolver_n_reinas(tablero, 0):
    imprimir_tablero(tablero)
else:
    print("No se encontró una solución.")
