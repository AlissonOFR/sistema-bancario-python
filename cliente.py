class Cliente:
    def __init__(self,nome,cpf,telefone=None, email=None):
        self.nome = None
        self.cpf = None
        self.telefone = telefone
        self.email = email


        if self.validar_nome(nome):
            self.nome = nome


        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        if self.validar_cpf(cpf_limpo):
            self.cpf = cpf_limpo


        self.validar_telefone(telefone)


        self.validar_email(email)


    def getNome(self):
        return self.nome


    def getCpf(self):
        return self.cpf


    def getTelefone(self):
        return self.telefone


    def getEmail(self):
        return self.email


    def alterarTelefone(self, telefone):
        if self.validar_telefone(telefone):
            self._telefone = telefone


    def alterarEmail(self, email):
        if self.validar_email(email):
            self._email = email


    def validar_nome(self, nome):
        return nome is not None and len(nome.strip()) >= 5


    def validar_cpf(self, cpf):
        return cpf is not None and len(cpf) == 11 and cpf.isdigit()
       
    def validar_telefone(self, telefone):
        if len(telefone) >= 10 or len(telefone) <= 11:
            return True
        if telefone not in "0123456789":
            return False
        if telefone is None:
            return False
        return False


    def validar_email(self, email):
        if "@" not in email:
            return False
        if email is None:
            return False
        return True
