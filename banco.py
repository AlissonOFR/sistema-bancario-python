class Banco:
    def __init__(self,nomeBanco,codigo):
        self.nomeBanco =  nomeBanco if nomeBanco is not None and len(nomeBanco) >= 3 else None
        self.codigo = codigo if codigo > 0 else 0
        self.contas = []
            
    
    
    def criar_contas(self, conta):
        for c in self.contas:
            if c.getNumero() == conta.getNumero():
                return False
        self.contas.append(conta)
        return True
    
    def remover_contas(self, numero_conta):
        for conta in self.contas:
            if conta.getNumero() == numero_conta.getNumero():
                self.contas.remove(conta)
                return True
        return False

    def busca_contas(self, numero):
        for conta in self.contas:
            if conta.getNumero() == numero:
                return conta
        return None
    
    def quantidade_contas(self):
        return len(self.contas)
    
    def listar_contas(self  ):
        return self.contas
    
    def getNome(self):
        return self.nomeBanco
    
    def getCodigo(self):
        return self.codigo



