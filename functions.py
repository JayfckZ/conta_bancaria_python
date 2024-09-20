import csv
import os
import random
from user import User


def salvar_dados(usuarios, arquivo="usuarios.csv"):
    with open(arquivo, mode="w", newline="") as arq:
        writer = csv.writer(arq)
        writer.writerow(["Nome", "Conta", "Senha", "Saldo"])
        for user in usuarios:
            writer.writerow(
                [user.get_nome(), user.get_conta(), user.get_senha(), user.get_saldo()]
            )


def carregar_dados(arquivo="usuarios.csv"):
    usuarios = []

    if not os.path.exists(arquivo):
        with open(arquivo, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Conta", "Senha", "Saldo"])

    try:
        with open(arquivo, mode="r") as arq:
            reader = csv.DictReader(arq)
            for row in reader:
                nome = row["Nome"]
                conta = row["Conta"]
                senha = row["Senha"]
                saldo = row["Saldo"]
                usuario = User(nome, conta, senha, saldo)

                usuarios.append(usuario)
    except FileNotFoundError:
        print(f"O {arquivo} não foi encontrado.")

    return usuarios


def gerar_conta(usuarios):
    while True:
        n_conta = str(random.randint(0, 9999)).zfill(4)
        if not any(user.get_conta() == n_conta for user in usuarios):
            return n_conta


def valida_senha():
    while True:
        try:
            senha = input("Digite uma senha de 6 dígitos: ")
            if (len(senha) == 6) and (senha.isdigit()):
                return senha
            print("\033[31;1mA senha deve conter exatamente 6 dígitos.\033[m\n")
        except:
            print("\033[31;1mA senha deve conter exatamente 6 dígitos.\033[m\n")

def encontra_conta(usuarios, conta):
    for user in usuarios:
        if conta == user.get_conta():
            return user
    
    return None
