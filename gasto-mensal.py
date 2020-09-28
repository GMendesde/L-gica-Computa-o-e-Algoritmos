def diagnostico(renda, valor_gasto, recomendado, tipo):
    valor_margem = renda * (recomendado / 100)
    if valor_gasto < valor_margem:
        print("Seus gastos totais com {} comprometem {:.1f}% de sua renda total. "
              "O máximo recomendado é de {}%. Seus gastos estão dentro da margem recomendada.".format(tipo, (valor_gasto/renda*100),
                                                                                                      recomendado))
    else:
        print("Seus gastos totais com {} comprometem {:.1f}% de sua renda total. "
              "O máximo recomendado é de {}%. Portanto, idealmente, o máximo de sua renda "
              "comprometida com moradia deveria ser de R$ {:.2f}.".format(tipo, (valor_gasto/renda*100), recomendado, renda * (recomendado/100)))



r_moradia = 30
r_educacao = 20
r_transporte = 15

renda_mensal = float(input("Renda mensal total: R$"))
gastos_moradia = float(input("Gastos totais com moradia: R$"))
gastos_educacao = float(input("Gastos totais com educação: R$"))
gastos_transporte = float(input("Gastos totais com transporte: R$"))

diagnostico(renda_mensal, gastos_moradia, r_moradia, "moradia")
diagnostico(renda_mensal, gastos_educacao, r_educacao, "educação")
diagnostico(renda_mensal, gastos_transporte, r_transporte, "transporte")
