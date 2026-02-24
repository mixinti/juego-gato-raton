TAM = 5 # tablero de 5x5
PROFUNDIDAD = 3 # que tan adelante piensa cada uno
MAX_TURNOS = 10 # limite de turnos

MOVS = [(-1,0),(1,0),(0,-1),(0,1)]

# Funciones basicas

def distancia(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def movimientos(pos):
    lista = []
    for dx, dy in MOVS:
        x = pos[0] + dx
        y = pos[1] + dy
        if 0 <= x < TAM and 0 <= y < TAM:
            lista.append((x,y))
    return lista

# Minimax con poda alfa-beta para mejores jugadas

def minimax(gato, raton, profundidad, turno_raton, alpha, beta):

    # caso base
    if profundidad == 0 or gato == raton:
        return distancia(gato, raton)

    if turno_raton:
        # MAX (ratón)
        valor = -float("inf")
        for mov in movimientos(raton):
            valor = max(valor, minimax(gato, mov, profundidad-1, False, alpha, beta))
            alpha = max(alpha, valor)

            # poda
            if beta <= alpha:
                break

        return valor

    else:
        # MIN (gato)
        valor = float("inf")
        for mov in movimientos(gato):
            valor = min(valor, minimax(mov, raton, profundidad-1, True, alpha, beta))
            beta = min(beta, valor)

            # poda
            if beta <= alpha:
                break

        return valor

# Movimientos

def mejor_mov_gato(gato, raton):
    mejor_val = float("inf")
    mejor = gato

    for mov in movimientos(gato):
        val = minimax(mov, raton, PROFUNDIDAD, True, -float("inf"), float("inf"))
        if val < mejor_val:
            mejor_val = val
            mejor = mov

    return mejor

def mejor_mov_raton(gato, raton):
    mejor_val = -float("inf")
    mejor = raton

    for mov in movimientos(raton):
        val = minimax(gato, mov, PROFUNDIDAD, False, -float("inf"), float("inf"))
        if val > mejor_val:
            mejor_val = val
            mejor = mov

    return mejor

# VIsualizacion

def mostrar(gato, raton):
    for i in range(TAM):
        for j in range(TAM):
            if (i,j) == gato:
                print("🐱", end=" ")
            elif (i,j) == raton:
                print("🐭", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Juego

def main():
    gato = (0,0)
    raton = (TAM-1, TAM-1)
    turnos = 0

    print("\nGATO VS RATÓN\n")

    while turnos < MAX_TURNOS:

        mostrar(gato, raton)

        # turno ratón
        raton = mejor_mov_raton(gato, raton)
        if gato == raton:
            print("El gato atrapó al ratón.")
            return

        # turno gato
        gato = mejor_mov_gato(gato, raton)
        if gato == raton:
            print("El gato atrapó al ratón.")
            return

        turnos += 1

    print("El ratón escapó.")

if __name__ == "__main__":

    main()
