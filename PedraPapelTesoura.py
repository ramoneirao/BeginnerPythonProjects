import random 

def play():
    usuario = input('\nQual a seu escolha? \n[R] para Pedra \n[P] para Papel \n[T] para Tesoura: ').lower()
    computador = random.choice(['r', 'p', 't'])

    if computador == usuario:
        print(f'Você e o computador escolheram {computador}')
        return 'Empate :|'
    
    print(f'Você escolheu {usuario} e o computador {computador}')
    if ganhou(usuario, computador):
        return 'Você Gnahou! :)'
    
    return 'Você Perdeu! :('
    

def ganhou(player, computador):
    if (player == 'r' and computador == 't') or (player == 't' and computador == 'p') or (player == 'p' and computador == 'r'):
        return True

print(play())