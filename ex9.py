salario = float(input("Digite o valor do seu salário: "))
#campo para informar o salário
despesas = float(input("Digite o valor das suas despesas mensais: "))

economiaMensal = salario - despesas
#economiaAnual = economiaMensal * 12 
umMilhao = 1000000/economiaMensal
umMiAno = umMilhao//12
umMiMes = umMilhao%12


print("Você será um milionário em {} anos e {} meses".format(umMiAno, umMiMes))
