class ContaBancaria():
    def __init__(self, numero, nome, tipo):
        self.numero=numero
        self.nome=nome
        self.tipo=tipo
        self.status=False
        self.limite=0
        self.saldo=0

    def ativarconta (self,ativarconta):
        print(f"{self.nome} ativou a conta")

    def verificarsaldo (self,verificarsaldo):
        print(f"{self.nome} seu saldo é {verificarsaldo}")

    def depositar (self,valor):
        valor = float(input("Qual o valor do deposito? "))
        self.saldo=+ valor
        print(f"{self.nome} depositou {valor} e seu saldo atual é {self.saldo}")

    def sacar (self,saque):
        saque = float(input("Qual o valor do saque? "))
        self.saldo=-saque
        print(f"{self.nome} sacou {saque} e seu saldo atual é {self.saldo}")
