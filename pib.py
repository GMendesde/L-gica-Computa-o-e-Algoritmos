import matplotlib.pyplot # pip install matploitlib
import numpy as np # nao foi usado no projeto

def preparar_dados():
    arquivo = open('Assessment_PIBs.csv', 'r', encoding='utf-8') # O arquivo pib esta na pasta do projeto
    dados = arquivo.read()
    linhas = dados.splitlines()
    dados_rotulos = linhas[0]
    lista_rotulos = dados_rotulos.split(",")
    dados_paises = linhas[1:]
    pib_pais = []
    lista_rot_paises = []

    for ano in dados_paises:
        ano = ano.split(',')
        ano[0] = ano[0].upper()
        pib_pais.append(ano)

    for pais in linhas:
        rot_pais = pais.split(',')
        lista_rot_paises.append(rot_pais[0].upper())

    lista_rot_paises.pop(0)

    return lista_rotulos, pib_pais, lista_rot_paises

rotulos, pib, paises = preparar_dados()


def verificar_pais(pais):
    if pais in paises:
        return True
    else:
        return False

def Pais():
    pais = input("Informe um país: ").upper()
    while not verificar_pais(pais):
        print(Exception("País não disponível. Tente outro país."))
        pais = input("Informe um país: ").upper()
    return pais

# Resposta letra A.

pais =Pais()

ano = int(input("Informe um ano entre 2013 e 2020: "))

while ano < 2013 or ano > 2020:
    print(Exception("Valor inválido."))
    ano = int(input("Informe um ano entre 2013 e 2020: "))


print("\nResposta alternativa A:\n")

def questao_A(pib):
    valorPIB = ''
    for pib in pib:
        if pais == pib[0]:
            valorPIB = pib[rotulos.index(str(ano))]

    print("PIB {} em 2020: US${} trilhões.".format(pais.capitalize(), valorPIB))

questao_A(pib)

# Resposta letra B.

print("\nResposta alternativa B:\n")
def questao_B():
    for paises in pib:
        pais = paises[0]
        variacao = (float(paises[-1]) / float(paises[1]) - 1) * 100
        print("{:<20} Variação de {:.2f}% entre {} e {}.".format(pais.capitalize(), variacao, rotulos[1], rotulos[-1]))

questao_B()


# Resposta letra C.

print("\nResposta alternativa C:\n")

local = Pais()

def grafico_valor(local, pib):
    vetor_valores = ""
    for index in pib:
        if local == index[0]:
            vetor_valores = index
            continue
    vetor_valores.pop(0)
    vetor_valores = [float(i) for i in vetor_valores]
    matplotlib.pyplot.title('Evolução do PIB - {}'.format(local))
    matplotlib.pyplot.ylabel('Valor em trilhões US$')
    rotulos.pop(0)
    matplotlib.pyplot.plot(rotulos, vetor_valores, 'r-o')
    matplotlib.pyplot.show()

grafico_valor(local, pib)
