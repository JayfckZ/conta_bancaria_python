from functions import carregar_dados, salvar_dados, gerar_conta, valida_senha
from time import sleep
from models import User

def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Cadastrar novo usuário")
    print("2. Login")
    print("3. Sair")
    return input("Selecione uma opção: ")

def menu_bancario(usuario):
    print("\n--- Menu Bancário ---")
    print(f"Nome: {usuario.get_nome()}")
    print(f"Saldo: {usuario.get_saldo()}")
    print("\n1. Depositar")
    print("2. Sacar")
    print("3. Transferir")
    print("4. Deslogar")
    return input("Selecione uma opção: ")

usuarios = carregar_dados()

while True:
    opcao = menu_principal()

    if opcao == "1":
        nome = input("Nome: ")
        conta = gerar_conta(usuarios)
        senha = valida_senha()

        usuario = User(nome, conta, senha)
        usuarios.append(usuario)
        salvar_dados(usuarios)

        print(f"Conta criada para {nome}. Nº de Conta: {conta}")
    
    elif opcao == "2":
        conta = input("Conta: ")
        senha = input("Senha: ")

        for user in usuarios:
            if user.get_conta() == conta and user.get_senha() == senha:
                print(f"Bem-vindo, {user.get_nome()}")
                
                logado = True
                while logado:
                    opcao2 = menu_bancario(user)

                    if opcao2 == "1":
                        try:
                            add_saldo = float(input("Valor a depositar: "))
                            print("Realizando transferência...")
                            sleep(2.5)
                            user.add_saldo(add_saldo)
                            print(f"Saldo atual: {user.get_saldo()}")
                        except ValueError as e:
                            print(f"\033[31;1mErro: {e}\033[m")
                            sleep(2.5)
                        
                    elif opcao2 == "2":
                        try:
                            dec_saldo = float(input("Valor a depositar: "))
                            print("Realizando transferência...")
                            sleep(2.5)
                            user.dec_saldo(dec_saldo)
                            print(f"Saldo atual: {user.get_saldo()}")
                        except ValueError as e:
                            print(f"\033[31;1mErro: {e}\033[m")
                            sleep(2.5)

                    elif opcao2 == "4":
                        print("Saindo...")
                        sleep(2.5)
                        logado = False
                        
                    else:
                        print("Opção não encontrada. Tente novamente.")

                    salvar_dados(usuarios)
            else:
                print("\033[33;1mConta ou senha inválidos.\033[m")
                sleep(2.5)

    elif opcao == "3":
        salvar_dados(usuarios)
        print("Sessão encerrada.")
        break

    else:
        print("Opção não encontrada. Tente novamente.")