from Transacao import Transacao
from banco import Banco
from cliente import Cliente
class contaBancaria:
    def __init__(self, numero,titular,banco,saldo):
        if numero is not None and numero > 0:
            self.numero = numero
        self.saldo = saldo
        self.titular = titular
        self.banco = banco
        self.transacoes = []
        
        if saldo >= 0:
            self.saldo = saldo
        else:
            self.saldo = 0.0

        if banco is not None:
            self.banco = banco
        
        if titular is not None: 
            self.titular = titular

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            transacao_deposito = Transacao("DEPOSITO",valor)
            self.transacoes.append(transacao_deposito)
            return True     
            
    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            transacao_saque = Transacao("SAQUE", valor)
            self.transacoes.append(transacao_saque)
            return True
        return False
    
    def transferir(self,valor, conta_destino):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            transacao_transferencia = Transacao("TRANSFERENCIA ENVIADA",valor)
            self.transacoes.append(transacao_transferencia)
            conta_destino.creditar(valor)
            return True
        return False
        
    def creditar(self,valor):
        self.saldo += valor
        transacao_creditar = Transacao("TRANSFERENCIA RECEBIDA", valor)
        self.transacoes.append(transacao_creditar)

    def mostrar_extrato(self):
        print("=" * 60)
        print("EXTRATO BANCÁRIO")
        print("=" * 60)
        print(f"Cliente: {self.getTitular().getNome()}")
        print(f"Banco: {self.banco.getNome()}")
        print(f"Conta: {self.banco.getCodigo()}")
        print("-" * 60)
        print("DATA |  TIPO  |  VALOR")
        for t in self.transacoes:
            print(t)
        print("-" * 60)
        print(f"SALDO FINAL: R$ {self.consultarSaldo():.2f}")

    def consultarSaldo(self):
        return self.saldo
        
    def getTitular(self):
        return self.titular
        
    def getBanco(self):
        return self.banco
        
    def estaAtiva(self):
        return self.saldo > 0
        
    def getNumero(self):
        return self.numero
