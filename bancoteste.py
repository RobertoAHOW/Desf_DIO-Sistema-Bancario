#Código de um sistema bancário simples, que permite ao usuário realizar depósitos, saques e exibir o extrato da conta.

class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.limite = 500.0
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        """
        Realiza um depósito na conta.
        :param valor: Valor a ser depositado (float).
        :return: Mensagem de sucesso ou falha.
        """
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        """
        Realiza um saque na conta, considerando saldo, limite e número máximo de saques.
        :param valor: Valor a ser sacado (float).
        :return: Mensagem de sucesso ou falha.
        """
        if valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        """
        Exibe o extrato da conta, mostrando todas as movimentações e o saldo atual.
        """
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def executar(self):
        """
        Executa o sistema bancário, permitindo ao usuário escolher entre as opções de menu.
        """
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """

        while True:
            opcao = input(menu).lower()

            if opcao == "d":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    self.depositar(valor)
                except ValueError:
                    print("Valor inválido. Tente novamente.")

            elif opcao == "s":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    self.sacar(valor)
                except ValueError:
                    print("Valor inválido. Tente novamente.")

            elif opcao == "e":
                self.exibir_extrato()

            elif opcao == "q":
                print("Saindo do sistema. Até logo!")
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":''
banco = Banco()
banco.executar()