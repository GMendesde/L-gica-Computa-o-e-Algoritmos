import matplotlib.pyplot

vetor_valores = []


def juros_compostos(val_inicial, rend_periodo, aporte_periodo, total_periodos):
    valor = val_inicial
    for i in range(1, total_periodos + 1):
        valor += valor * (rend_periodo / 100) + aporte_periodo
        vetor_valores.append(valor)
    return valor


def grafico_valor():
    matplotlib.pyplot.title('Evolução juros compostos')
    matplotlib.pyplot.xlabel('Períodos')
    matplotlib.pyplot.ylabel('Valor acumulado em R$')
    matplotlib.pyplot.plot(vetor_valores)
    matplotlib.pyplot.show()


def tela():
    for i in range(0, len(vetor_valores)):
        print("Após {} períodos(s), o montante será de R${:.2f}.".format(i + 1, vetor_valores[i]))


valor_Inicial = float(input("Valor inicial: R$"))
ren_Periodo = float(input("Redimento por período (%): "))
ap_Periodo = float(input("Aporte a cada período: R$"))
total_Periodos = int(input("Total de períodos: "))


juros_compostos(valor_Inicial, ren_Periodo, ap_Periodo, total_Periodos)

tela()

grafico_valor()
