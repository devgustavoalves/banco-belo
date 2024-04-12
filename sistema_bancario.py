menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == "1":
        print("========== DEPÓSITOS ==========")
        valor = float(input("Qual valor deseja depositar? ")) 
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"Seu saldo agora é R$ {saldo:.2f}\n")
            print("Obrigado por ser nosso cliente")
        else:
            print("Operação Falhou! O valor informado é inválido.")
    elif opcao == "2":
        print("========== SAQUES ==========")
        if numero_saques == LIMITE_SAQUES:
            print("Você já atingiu o seu limite de 3 saques diários.")
        else:
            valor = float(input("Qual valor deseja sacar? ")) 
            if valor > saldo:
                print("Você não tem dinheiro o suficiente para realizar esse saque")
            elif valor > 0 and valor <= 500:
                numero_saques = numero_saques + 1
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                print(f"Seu saldo agora é R$ {saldo:.2f}\n") 
                print("Obrigado por ser nosso cliente")
            else:
                print("O seu limite de saque por operação é de R$500,00. Insira um valor menor para efetuar o saque.")
    elif opcao == "3":
        print("========== EXTRATO ==========")
        print("Nenhuma movimentação foi realizada" if not extrato else extrato)
        print(f"Seu saldo atual é R${saldo:.2f}")
    elif opcao == "4":
        print("Obrigado pela preferência")
        break
    else:
        print("Digite uma opção válida")
 
        
