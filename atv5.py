from banco import Banco
from cliente import Cliente
from contaBancaria import contaBancaria

banco = Banco("Banco IFAL", 1001)


cliente1 = Cliente("João Lucas","01234566789","82987641360","joao@gmail.com")
cliente2 = Cliente("Vitor","98765432101","85999557720","vitor@gmailcom")
cliente3 = Cliente("Ana Gabriela","24681357901","21988562301","ana@gmail.com")

conta1 = contaBancaria(1, cliente1, banco, 1000.00)
conta2 = contaBancaria(2, cliente2, banco, 5000.00)
conta3 = contaBancaria(3, cliente3, banco, 900.00)
conta4 = contaBancaria(4, cliente3, banco, 8000.00)

banco.criar_contas(conta1)
banco.criar_contas(conta2)
banco.criar_contas(conta3)
banco.criar_contas(conta4)

conta1.depositar(300)
conta2.depositar(400)
conta3.depositar(1000)
conta4.depositar(100)

conta1.saque(100)
conta2.saque(200)
conta3.saque(150)
conta4.saque(600)


conta1.mostrar_extrato()