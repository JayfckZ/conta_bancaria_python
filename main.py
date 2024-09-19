from functions import carregar_dados, salvar_dados, gerar_conta, valida_senha
from models import User

def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Cadastrar novo usuário")
    print("2. Login")
    print("3. Sair")
    return input("Selecione uma opção: ")

usuarios = carregar_dados()

while True:
    #   REMOVER APÓS PRIMEIROS TESTES !!!!!!!!!!!!!!
    for usuario in usuarios:
        print(f"Nome: {usuario.get_nome()}, Conta: Nº {usuario.get_conta()}, Senha: {usuario.get_senha()}, Saldo: R$ {usuario.get_saldo()}")
    
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
        pass

    elif opcao == "3":
        salvar_dados(usuarios)
        print("Sessão encerrada.")
        break

    else:
        print("Opção não encontrada. Tente novamente.")