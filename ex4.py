cotaçãoDolar = float(input("Digite a cotação do dolar: "))
#campo para digitação do dólar
reais = float(input("Digite o quanto você possui em reais: "))

emDolar = reais/cotaçãoDolar
print("Pela quantidade de {} reais, convertendo em dólar você possui {} dolares".format(reais, emDolar))
