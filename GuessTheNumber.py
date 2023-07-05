from random import randint

def guess(x):
    print('Advinhe o número escolhido pelo computador!')
    random_number = randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Escolha um número de 1 até {x}: '))
        if guess < random_number:
            print('Tente novamente. Muito baixo!')
        elif guess > random_number:
            print('Tente novamente. Muito alto!')
    print(f'Uhul, parabéns. Você acertou o número {random_number} corretamente!')


def computer_guess(x):
    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if baixo != alto:
            guess = randint(baixo, alto)
        else:
            guess = baixo

        feedback = input(f'O número {guess} é mais alto (A), mais baixo (B) ou correto (C)?').lower
        if feedback == 'a':
            alto = guess - 1
        elif feedback == 'b':
            baixo = guess + 1
    print('Uhul, o computador acertou o seu número')

computer_guess(10)