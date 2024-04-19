import textwrap

def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair


    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print(f"Seu saldo agora é R$ {saldo:.2f}\n")
        print("Obrigado por ser nosso cliente")
    else:
        print("Operação Falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques ):
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques == limite_saques
        excedeu_limite = valor > limite
        if excedeu_saques:
            print("Você já atingiu o seu limite de 3 saques diários.")
        elif excedeu_saldo:
            print("Você não tem dinheiro o suficiente para realizar esse saque")
        elif excedeu_limite:
            print("O seu limite de saque por operação é de R$500,00. Insira um valor menor para efetuar o saque.")
             
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            print(f"Seu saldo agora é R$ {saldo:.2f}\n") 
            print("Obrigado por ser nosso cliente")
            numero_saques += 1 
            print(numero_saques, limite_saques)

        else:
            print("O valor informado é invalido ")
        
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("========== EXTRATO ==========")
    print("Nenhuma movimentação foi realizada" if not extrato else extrato)
    print(f"Seu saldo atual é R${saldo:.2f}")

def main():
             
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3


    while True:
        opcao = menu()  

        if opcao == "1":
            print("========== DEPÓSITOS ==========")
            valor = float(input("Qual valor deseja depositar? ")) 
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            print("========== SAQUES ==========")
            valor = float(input("Qual valor deseja sacar? ")) 
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
      
        elif opcao == "3":
             exibir_extrato(saldo, extrato = extrato)
            
        elif opcao == "4":
            print("Obrigado pela preferência")
            break
        else:
            print("Digite uma opção válida")

main()
 
        
