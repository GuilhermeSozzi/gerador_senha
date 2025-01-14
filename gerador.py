import random
import string

lista_caracteres = '!@#$%¨&*()_-+=\|:;/?<>,.[]{}'
letras = string.ascii_letters
nummeros = string.digits

lista_caracteres = lista_caracteres + letras + nummeros

def sorteador(quantidade):
    sorteado = ''
    for i in range(quantidade):
        sorteado = sorteado + random.choice(lista_caracteres)
    return sorteado

while True:
    senha_aleatoria = ''
    tamanho_senha = 0

    try:
        tamanho_senha = int(input("\nDigite o tamanho desejado da senha:"))
    except ValueError:
        print("Entrada inválida.")
        continue

    senha_aleatoria = sorteador(tamanho_senha)
    print(f"\nA seguinte senha foi gerada: {senha_aleatoria}\n")
    opcao = input("Digite qualquer tecla para aceitar a senha ou 1 para gerar uma nova.")

    if opcao == '1':
        continue
    else:
        break