cont = "s"
while cont == "s":
    gas = float(input("Informe o valor da galosina R$:\n"))
    alc = float(input("Informe o valor do alcool R$:\n"))
    valor = alc / gas
    if valor > 0.7:
        print("Gasolina vale mais a pena")
    elif valor == 0.7:
        print("Tanto faz abastecer com qualquer um dos dois")
    else:
        print("Alcool vale mais a pena")
    cont= input("Deseja continuar?\nS --> SIM\nN --. NÂO\n").lower()
print("Programa finalizado")
    

