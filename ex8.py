valorBoleto = float(input("Digite o valor do boleto: "))
#campo para digitar o valor do boleto
percentualJuros = 10/100
diasAtraso = int(input("Digite os dias de atraso: "))

novoValor = valorBoleto + (valorBoleto * percentualJuros) * diasAtraso 

print("O valor do boleto atualizado a ser pago é de {} ".format(novoValor))