import random
from time import sleep

def passwordGenerator(tamanho):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    spc_char = '!@#$%&*'

    all_chars = char + num + spc_char

    password = ''.join(random.choice(all_chars) for c in range(tamanho))
    
    return password

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def passwordUX():
    while True:
        var_choice = str(input('Deseja inicializar o gerador de senhas? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_tamanho = int(input('Digite o tamanho da senha: '))

            var_senha = passwordGenerator(var_tamanho)

            print(f'Sua senha foi gerada: {var_senha}')
            print('')
            var_choice = str(input('Deseja gerar outra senha? (Sim/Não): '))

            if var_choice == 'sim':
                passwordUX()
                print()
            elif var_choice == 'não':
                exit()
                break
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: unexpected_choice!\33[m')
if __name__ == '__main__':
    passwordUX()