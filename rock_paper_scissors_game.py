import random

def run():
    #1-piedra. 2-papel 3-tijera
    list_select=[1,2,3]

    print('BIENVENIDO. Juego de piedra papel o tijera \n')
    player_select = input_revision_selec()
    while player_select < 0 or player_select > 3:
        print("\n Xx_Opcion invalida_xX\n")
        player_select=input_revision_selec()

    if player_select !=0:
        pc_select = random.choice(list_select)
        print("Tu eleccion: " +print_select(player_select) + '   VS    Eleccion bot: '+ print_select(pc_select))

        if player_select == pc_select:
            print("__EMPATE__")
        elif player_select ==  1:
            if pc_select == 2:
                print('PERDISTE... Gana bot')
            elif pc_select == 3:
                print('GANASTE!!!')
        elif player_select == 2:
            if pc_select == 1:
                print('GANASTE!!!')
            elif pc_select == 3:
                print('PERDISTE... Gana bot')
        elif player_select == 3:
            if pc_select == 1:
                print('PERDISTE... Gana bot')
            elif pc_select == 2:
                print('GANASTE!!!')
    else:
        print('ADIOS!!!')

        # #usuario piedra
        # if player_select == 1:
        #     if pc_select == 1:
        #         print("__EMPATE__")
        #     elif pc_select == 2:
        #         print('PERDISTE... Gana bot')
        #     elif pc_select == 3:
        #         print('GANASTE!!!')
        # #usuario papel
        # elif player_select == 2:
        #     if pc_select == 1:
        #         print('GANASTE!!!')
        #     elif pc_select == 2:
        #         print("__EMPATE__")
        #     elif pc_select == 3:
        #         print('PERDISTE... Gana bot')
        # #usuario tijera
        # if player_select == 3:
        #     if pc_select == 1:
        #         print('PERDISTE... Gana bot')
        #     elif pc_select == 2:
        #         print('GANASTE!!!')
        #     elif pc_select == 3:
        #         print("__EMPATE__")

    

def print_select(numb):
    if numb == 1:
        return "Piedra"
    elif numb ==2:
        return "Papel"
    elif numb ==3:
        return "Tijera"

def input_revision_selec():
    try:
        print('Elige \n 1-piedra.\n 2-papel \n 3-tijera\n 0-Salir')
        selec_player = int (input("Ingrese numero: " ))
        return selec_player
    except ValueError :
        print('ERROR: sXx_Opcion invalida_xX')
        input_revision_selec()

if __name__ == '__main__':
    run()