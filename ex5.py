precoGasolina = float(input("Digite o valor do combustível: "))
#campo para informar o valor do combustível
abastece = float(input("Digite o valor que deseja abastecer: "))

emLitros = abastece/precoGasolina

print("Você pagou {} reais e abasteceu {} litros".format(abastece, emLitros))