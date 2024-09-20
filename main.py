from functions import carregar_dados, salvar_dados, gerar_conta, valida_senha, encontra_conta
from time import sleep
from user import User

def menu_principal():
    print("\n========== Menu Principal ==========")
    print("1. Cadastrar novo usuário")
    print("2. Login")
    print("3. Sair")
    return input("Selecione uma opção: ")

def menu_bancario(usuario):
    print("\n========== Menu Bancário ==========")
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

        print(f"\n\nConta criada para {nome}. Nº de Conta: \033[33;1m{conta}\033[m")
    
    elif opcao == "2":
        conta = input("Conta: ")
        senha = input("Senha: ")

        i = 0
        for user in usuarios:
            if user.autenticar(conta, senha):
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
                            print("Realizando saque...")
                            sleep(2.5)
                            user.dec_saldo(dec_saldo)
                            print(f"Saldo atual: {user.get_saldo()}")
                        except ValueError as e:
                            print(f"\033[31;1mErro: {e}\033[m")
                            sleep(2.5)

                    elif opcao2 == "3":
                        try:
                            conta_transf = input("Digite a conta para qual deseja transferir: ")
                            
                            if conta_transf == user.get_conta():
                                raise ValueError("Não é possível realizar transferências para sua própria conta.")
                            
                            user_encontrado = encontra_conta(usuarios, conta_transf)    

                            if not user_encontrado:
                                raise ValueError("Conta não encontrada.")

                            print(f"Transferindo para: {user_encontrado.get_nome()}")
                            saldo_transf = float(input("Digite o valor a transferir (0 para cancelar): "))
                            if saldo_transf == 0:
                                print("\033[31;1mCancelando...\033[m")
                                sleep(1.5)
                            else:
                                print("Realizando transferência...")
                                sleep(2.5)
                                user.dec_saldo(saldo_transf)
                                user_encontrado.add_saldo(saldo_transf)
                                print(f"\033[32;1mTransferência realizada com sucesso!\033[m")
                                sleep(2.5)
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
                break

            else:
                i += 1
                if i == len(usuarios):
                    print("\033[33;1mConta ou senha inválidos.\033[m")
                    sleep(2.5)

    elif opcao == "3":
        salvar_dados(usuarios)
        print("\nSessão encerrada.")
        break

    else:
        print("Opção não encontrada. Tente novamente.")