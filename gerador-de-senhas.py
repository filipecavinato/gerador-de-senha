# Script criado por Filipe Cavinato

from utilidades.menus import menu
from utilidades.geradores import gerar_senha
from rich import print

menu('Gerador de Senha')
while True:
    try:
       tamanho = int(input('Quantidade de Caracteres: '))
    except ValueError:
        print('[red] Erro: Digite um número inteiro valido![/]')
    except KeyboardInterrupt:
        print('\n[red] Aviso: Usuário finalizou o programa manualmente.[/]')
        break
    else:
        print(f'Senha = [blue]{gerar_senha(tamanho)}[/]')
        break
