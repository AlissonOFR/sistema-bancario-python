
class Banco:
    def __init__(self, nome, codigo):
        self._nome = ""
        self._codigo = 0
        self._contas = [] # Coleção de contas
        
        if nome is not None and len(nome) >= 3:
            self._nome = nome
            
        if codigo is not None and codigo > 0:
            self._codigo = codigo

    def adicionarConta(self, conta):
        # Verifica se a conta já existe no banco pelo número
        for c in self._contas:
            if c.getNumero() == conta.getNumero():
                return False # Já existe uma conta com esse número
        
        self._contas.append(conta)
        return True

    def removerConta(self, numero):
        for conta in self._contas:
            if conta.getNumero() == numero:
                self._contas.remove(conta)
                return True
        return False

    def buscarConta(self, numero):
        for conta in self._contas:
            if conta.getNumero() == numero:
                return conta
        return None

    def quantidadeContas(self):
        return len(self._contas)

    def listarContas(self):
        return self._contas
    
    def getNome(self):
        return self._nome
    
    def getCodigo(self):
        return self._codigo