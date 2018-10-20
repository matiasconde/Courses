import pygame, random

def dibujar_tablero(board):
    """Ingresar una lista del estilo [1,2,6,4], donde la posición de la lista indica la columba del tablero y el valor de cada item
     me da la posición de la fila."""

    pygame.init()
    surface_size = 480
    n = len(board)
    square_size = 480//n
    surface_size = square_size*n

    tablero = pygame.display.set_mode((surface_size,surface_size))

    color_t = ((68,117,239),(255,255,255))

    ficha = pygame.image.load("Ficha de dama blanca.png")

    offset = (square_size-ficha.get_width())//2

    while True:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            break

        for row in range(n):
            index_color = row % 2

            for col in range(n):

                casillero = (row*square_size,col*square_size,square_size,square_size)
                tablero.fill(color_t[index_color],casillero)

                index_color = (index_color+1)%2

        for col,row in enumerate(board):

            tablero.blit(ficha,(square_size*col + offset,square_size*row + offset))

        pygame.display.flip()

    pygame.quit()

def mod(x):
    if x<0:
        return -x
    else:
        return x

def has_clashes(board):
    """ verifica que ninguna reina se cruce ni diagonalmente ni horizontalmente con un rival, el cruce vertical
     se evita ya que la misma lista del tablero separa las columnas distintas"""
    Value = False
    for col, row in enumerate(board):
        board_clone = board
        board_reduced = board[0:col]+board[col+1:]
        if row in board_reduced:
            Value = True
            return Value
        else:
            for col2,row2 in enumerate(board):
                if col2 == col:
                    continue
                elif mod(col2-col) == (row2-row):
                    Value = True
                    return Value
    return Value

def N_Queens_problem(n,max_tries):

    """ para empezar las listas de tablero que toma el juego jamás tendrán coincidencias en columna por la construcción de la lista, cada item una columna
    distinta, es un caso trivial, no interesa"""

    board = list(range(n))
    q_solutions = 0
    q_solutions_distintas = 0
    tries = 0
    list_of_solutions = []

    while tries < max_tries:
        tries += 1
        random.shuffle(board)

        if not has_clashes(board):
            q_solutions += 1
            boardok = board[:] #antes lo asignaba con objeto y todo y tenia problemas de aliasinG !!!!
            list_of_solutions.append(boardok)
            print(boardok)


    print("se encontraron {0} soluciones en {1} intentos".format(q_solutions,tries))
    print(list_of_solutions)
    for i,v in enumerate(list_of_solutions):
        if v not in list_of_solutions[0:i]+list_of_solutions[i+1:]:
            q_solutions_distintas += 1
            dibujar_tablero(v)
    print("se encontraron {0} soluciones distintas en {1} intentos".format(q_solutions_distintas, tries))

"""
if __name__ == "__main__":
    dibujar_tablero([3,7,0,7,6,1,5,2])
"""

N_Queens_problem(10,10000)



#a = [3,7,0,4,6,1,5,6]
#print(has_clashes(a))
#dibujar_tablero(a)
