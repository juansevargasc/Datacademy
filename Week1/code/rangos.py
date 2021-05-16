def game(low_bound, upper_bound, game_number):
    if game_number > low_bound and game_number < upper_bound:
        print(game_number)
    else:
        print(game_number)
        game_number = int( input('Reintroduce un número: ') )
        return game(low_bound, upper_bound, game_number)

def run():
    print('Rangos Cambiantes\n')
    low = int( input('Mínimo: ') )
    upper = int( input('Máximo: ') )
    num = int( input('Tu número: ') )

    game(low, upper, num)

if __name__ == '__main__':
    run()
