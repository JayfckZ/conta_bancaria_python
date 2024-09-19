import csv
import os
from models import User


def salvar_dados(usuarios, arquivo="usuarios.csv"):
    with open(arquivo, mode="w", newline="") as arq:
        writer = csv.writer(arq)
        writer.writerow(["Nome", "Conta", "Senha", "Saldo"])
        for user in usuarios:
            writer.writerow([user.get_nome(), user.get_conta(), user.get_senha(), user.get_saldo()])

def carregar_dados(arquivo='usuarios.csv'):
    usuarios = []

    if not os.path.exists(arquivo):
        with open(arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Conta', "Senha", 'Saldo'])
    
    try:
        with open(arquivo, mode="r") as arq:
            reader = csv.DictReader(arq)
            for row in reader:
                nome = row["Nome"]
                conta = conta["Conta"]
                senha = row["Senha"]
                saldo = saldo["Saldo"]
                usuario = User(nome, conta, senha, saldo)
                
                usuarios.append(usuario)
    except FileNotFoundError:
        print(f"O {arquivo} não foi encontrado.")

    return usuarios