import textwrap
import re
import json

ARQUIVO_USUARIOS = "usuarios.json"

usuarios = {}
usuario_logado = None

def carregar_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def salvar_usuarios(usuarios):
    usuarios_existentes = carregar_usuarios()
    usuarios_existentes.update(usuarios)
    with open(ARQUIVO_USUARIOS, 'w') as arquivo:
        json.dump(usuarios_existentes, arquivo)

def verificar_cpf(cpf):
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(padrao_cpf, cpf) is not None

def solicitar_cpf():
    while True:

        cpf = input("Insira seu CPF (no formato XXX.XXX.XXX-XX): ")
        if verificar_cpf(cpf):
            return
        else:
            print("CPF inválido. Digite um CPF no formato XXX.XXX.XXX-XX")

def menu_inicial():
    menu_inicial = """
    [1] Cadastro
    [2] Login
    [3] Sair
    => """
    return input(textwrap.dedent(menu_inicial))

def criar_usuario():
    print("=========== CRIAR USUARIO ==========")
    nome = input("Insira seu nome: ")
    cpf = solicitar_cpf()
    numero_conta = input("Insira o número da sua conta: ")
    senha = input("Insira a senha da sua conta: ")
    usuarios = carregar_usuarios()
    usuarios[numero_conta] = {"nome": nome, "cpf": cpf, "senha": senha, "saldo": 0, "extrato": "", "limite": 500, "numero_saques": 0, "saques_feitos": 0}
    usuarios = salvar_usuarios(usuarios)
    print("Usuario cadastrado com sucesso! Seja bem-vindo(a) ao banco Belo", nome)

def login():
    global usuario_logado
    print("========== LOGIN ==========")
    numero_conta = input("Insira o número da conta: ")
    senha = input("Insira sua senha: ")

    usuarios = carregar_usuarios()

    if numero_conta not in usuarios:
        print("Número da conta não cadastrado. Cadastre-se e tente novamente")
        return criar_usuario()

    if usuarios[numero_conta]["senha"] == senha:
        print("Login bem-sucedido!\n")
        usuario_logado = usuarios[numero_conta]
        return True
    else:
        print("Senha incorreta. Tente novamente.\n")
        return False

    
   
def menu_principal():
    global usuario_logado
    while True:
        opcao = input(textwrap.dedent("""
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Sair
            => """))

        if opcao == "1":
            depositar(usuario_logado)
        elif opcao == "2":
            sacar(usuario_logado)
        elif opcao == "3":
            extrato(usuario_logado)
        elif opcao == "4":
            print("Obrigado por usar nosso sistema.")
            usuario_logado = None 
            return
        else:
            print("Opção inválida. Tente novamente.")

def depositar(usuario_atual):
    valor = float(input("Digite o valor a ser depositado: "))
    usuario_atual["saldo"] += valor
    usuario_atual["extrato"] += f"Depósito: +{valor}\n"
    print("Depósito realizado com sucesso.")

def sacar(usuario_atual):
    if usuario_atual["saques_feitos"] >= 3:
        print("Limite de saques atingido para esta sessão.")
        return

    valor = float(input("Digite o valor a ser sacado (limite de 500 por saque): "))
    if valor > usuario_atual["limite"]:
        print("Limite de saque excedido.")
        return

    if valor > usuario_atual["saldo"]:
        print("Saldo insuficiente.")
    else:
        usuario_atual["saldo"] -= valor
        usuario_atual["extrato"] += f"Saque: -{valor}\n"
        usuario_atual["numero_saques"] += 1
        usuario_atual["saques_feitos"] += 1
        print("Saque realizado com sucesso.")

def extrato(usuario_atual):
    print("Extrato:")
    print(usuario_atual["extrato"])
    print(f"Saldo atual: {usuario_atual['saldo']}")

def main():
    global usuario_logado
    while True:
        opcao = menu_inicial()

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            if login():
                menu_principal()
        elif opcao == "3":
            print("Obrigado por usar nosso sistema.")
            break
        else:
            print("Digite uma opção válida")

main()
