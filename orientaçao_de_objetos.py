from os import system
from time import sleep

restaurantes = [
                {'nome' : 'Camarada Camarão',  'categoria' : 'Seafood', 'ativo' : True},
                {'nome' : 'Izu', 'categoria' : 'Japanese', 'ativo' : True},
                {'nome' : 'Kabanas', 'categoria' : 'Brazilianfood', 'ativo' : True},
                {'nome' : 'Cerrado', 'categoria' : 'Brazilianfood', 'ativo' : True},
                {'nome' : 'Grego', 'categoria' : 'Brazilianfood', 'ativo' : True},
                {'nome' : 'Madero', 'categoria' : 'Steakhouses', 'ativo' : True},
                {'nome' : 'Favo De Mel', 'categoria' : 'Steakhouses', 'ativo' : True},
                {'nome' : 'Pobre Juan', 'categoria' : 'Steakhouses', 'ativo' : True},
                {'nome' : 'JP', 'categoria' : 'Steakhouses', 'ativo' : True},
                {'nome' : 'El Argentino', 'categoria' : 'Steakhouses', 'ativo' : True},
                {'nome' : 'Outback', 'categoria' : 'Steakhouses', 'ativo' : True}]

cor_preta = '\033[30m'
cor_vermelha = '\033[31m'
cor_verde = '\033[32m'
cor_amarela = '\033[33m'
cor_azul = '\033[34m'
cor_roxa = '\033[35m'
cor_ciano = '\033[36m'
cor_cinza = '\033[37m'
fechamento_cor = '\033[m'

cores = [
cor_preta,
cor_vermelha,
cor_verde,
cor_amarela,
cor_azul,
cor_roxa,
cor_ciano,
cor_cinza,
fechamento_cor
]

def exibir_nome_do_programa():
    print(f'''

{cores[5]} ██████╗  █████╗ {cores[8]}{cores[6]}██████╗ ███████╗ ██████╗████████╗██╗   ██╗██╗ ██████╗ █████╗ ██████╗{cores[8]}
{cores[5]}██╔════╝ ██╔══██╗{cores[8]}{cores[6]}██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║   ██║██║██╔════╝██╔══██╗██╔══██╗{cores[8]}
{cores[5]}██║  ██╗ ██║  ██║{cores[8]}{cores[6]}██████╔╝█████╗  ╚█████╗    ██║   ╚██╗ ██╔╝██║╚█████╗ ██║  ██║██████╔╝{cores[8]}
{cores[5]}██║  ╚██╗██║  ██║{cores[8]}{cores[6]}██╔══██╗██╔══╝   ╚═══██╗   ██║    ╚████╔╝ ██║ ╚═══██╗██║  ██║██╔══██╗{cores[8]}
{cores[5]}╚██████╔╝╚█████╔╝{cores[8]}{cores[6]}██║  ██║███████╗██████╔╝   ██║     ╚██╔╝  ██║██████╔╝╚█████╔╝██║  ██║{cores[8]}
{cores[5]} ╚═════╝  ╚════╝ {cores[8]}{cores[6]}╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝      ╚═╝   ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝{cores[8]}
      ''')

def exibir_opcoes():
    print(f' {cores[3]} 1{cores[8]} {cores[6]}●{cores[8]} Cadastrar restaurante')
    print(f' {cores[3]} 2{cores[8]} {cores[6]}●{cores[8]} Listar restaurante')
    print(f' {cores[3]} 3{cores[8]} {cores[6]}●{cores[8]} Ativar/Desativar restaurante') 
    print(f' {cores[3]} 4{cores[8]} {cores[6]}●{cores[8]} Sair')

def escolher_opcao():
    try: 
        opcao_escolhida = str(input('Escolha uma opção: ')).strip()

        if opcao_escolhida == '1':
            cadastrar_novo_restaurante()
        elif opcao_escolhida == '2': # da mais continuidade
            listar_restaurantes()
        elif opcao_escolhida == '3':
            alternar_estado_do_restaurante()
        elif opcao_escolhida == '4':
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
''' sem usar try e except
 def escolher_opcao():
     opcao_escolhida = str(input('Escolha uma opção: ')).strip()

     if opcao_escolhida == '1':
         print('Cadastrar restaaurante')
     elif opcao_escolhida == '2': # da mais continuidade
         print('Listar restaurantes')
     elif opcao_escolhida == '3':
         print('Ativar restaurante')
     elif opcao_escolhida == '4':
         finalizar_app()
     else:
        opcao_invalida()'''

def voltar_ao_menu_principal():
    input(f'\n {cores[4]} Aperte a tecla Enter para voltar ao menu principal {cores[8]} ')
    main()

def exibir_subtitulo(texto):
    system('cls') # system('clear') no mac
    print(texto)
    print()

def finalizar_app():
    exibir_subtitulo(f'{cores[1]} Finalizando o app {cores[8]}')  

def opcao_invalida():
    exibir_subtitulo(f'{cores[1]} OPÇÃO INVALIDA {cores[8]}') 
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo(f'{cores[5]} CADASTRO DE NOVOS RESTAURANTES {cores[8]}')
    
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ').title().strip()
    categoria_do_restaurante = input('\nDigite a categoria do restaurante que deseja cadastrar: ')
    novo_restaurante = {'nome' : nome_do_restaurante,
                        'categoria' : categoria_do_restaurante,
                        'ativo' : False}
    restaurantes.append(novo_restaurante)

    print(f'\n{cores[2]}O restaurante {nome_do_restaurante} foi cadastrado com sucesso!{cores[8]}')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo(f'{cores[5]}LISTANDO OS RESTAURANTES...{cores[8]}')
    sleep(3)

    for restaurante in restaurantes:
        nome_restaurantes = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        if ativo == 'Ativado':
            cor_ativo = f'{cores[2]}●{cores[8]}'
        else:
                cor_ativo = f'{cores[1]}●{cores[8]}'
        print(f'{cores[3]}●{cores[8]} {nome_restaurantes}\n    {cores[5]}●{cores[8]} {cores[0]}{categoria}{cores[8]}\n    {cor_ativo} {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo(f'{cores[5]} ATIVAR/DESATIVAR ESTADO DO RESTAURANTE {cores[8]}')
    nome_restaurante = str(input('Digite o nome do restaurante que deseja alterar o estado: ')).strip().title()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo']:
                print(f'O restaurante {nome_restaurante} foi {cores[2]}ativado{cores[8]} com {cores[6]}sucesso{cores[8]}')
            else:
                print(f'O restaurante {nome_restaurante} foi {cores[1]}destivado{cores[8]} com {cores[6]}sucesso{cores[8]}')
    
    if not restaurante_encontrado:
        print(f'{cores[1]} O RESTAURANTE NÃO FOI ENCONTRADO {cores[8]}')

    voltar_ao_menu_principal()

def main():
    system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()
