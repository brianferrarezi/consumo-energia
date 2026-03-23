# Consumo mensal de energia elétrica
# Autor: Brian Ferrarezi
# Entrada
Aparelho = input ('Digite o nome do aparelho: ')
Potência = float(input('Digite a potência do aparelho em watts (w): '))
Horas = int(input('Digite o tempo médio de uso diário do aparelho em horas:'))
# Processamento
ConsumoMensal = (Potência *Horas* 30)/1000
ValorPagar = ConsumoMensal * 0.75
#Saída
print('O consumo mensal do aparelho', Aparelho, 'é de', ConsumoMensal, 'kWh/mês')
print('O valor a pagar pelo consumo do aparelho', Aparelho, 'é de R$', f"{ValorPagar:.2f}")


 
