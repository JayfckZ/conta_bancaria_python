class User:
    def __init__(self, nome, conta, senha, saldo=0):
        self.nome = nome
        self.conta = conta
        self.__senha = senha
        self.__saldo = float(saldo)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_conta(self):
        return self.conta

    # --- Métodos de senha ---
    def get_senha(self):
        return self.__senha

    def set_senha(self, nova_senha):
        if len(nova_senha) == 6:
            if nova_senha.isdigit():
                self.__senha = nova_senha
                return
            raise ValueError("A senha contém caracteres inválidos.")

        raise ValueError("A senha deve conter 6 números.")

    def autenticar(self, senha):
        return self.__senha == senha

    # --- Métodos de saldo ---
    def get_saldo(self):
        return f"{self.__saldo:.2f}"

    def add_saldo(self, add_saldo):
        if type(add_saldo) == float:
            if add_saldo > 0:
                self.__saldo += add_saldo
                return
            elif add_saldo == 0:
                raise ValueError("O valor não pode ser 0.")

            raise ValueError("O valor deve ser um número positivo.")

        raise ValueError("O valor não é um número.")

    def dec_saldo(self, dec_saldo):
        if type(dec_saldo) == float:
            if dec_saldo > 0:
                self.__saldo -= dec_saldo
                return
            elif dec_saldo == 0:
                raise ValueError("O valor não pode ser 0.")

            raise ValueError("O valor deve ser um número positivo.")

        raise ValueError("O valor não é um número.")
