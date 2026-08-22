# 🏦 Sistema Bancário em Python

Projeto desenvolvido em **Python** durante meus estudos de **Análise e Desenvolvimento de Sistemas**, com o objetivo de aplicar na prática conceitos de **Tipos Abstratos de Dados (TADs)**, **Programação Orientada a Objetos (POO)**, encapsulamento, modularização e organização de código.

O projeto representa um sistema bancário simplificado, permitindo o gerenciamento de clientes, contas e transações bancárias.

## 🎯 Objetivos

* Aplicar conceitos de Programação Orientada a Objetos;
* Praticar encapsulamento e modularização;
* Trabalhar com diferentes classes e suas responsabilidades;
* Desenvolver operações bancárias;
* Criar um histórico de transações;
* Desenvolver um extrato bancário;
* Utilizar Git e GitHub para acompanhar a evolução do projeto.

## ⚙️ Funcionalidades

Atualmente, o sistema possui:

* [x] Cadastro de clientes
* [x] Criação de contas bancárias
* [x] Validação básica dos dados
* [x] Depósitos
* [x] Saques
* [x] Controle de saldo
* [x] Transferências entre contas
* [x] Registro de transações
* [x] Histórico de transações
* [x] Exibição de extrato bancário

## 🏗️ Estrutura do projeto

```text
sistema-bancario-python/
│
├── banco.py
├── cliente.py
├── contaBancaria.py
├── Transacao.py
├── atv5.py
├── teste.py
├── .gitignore
└── README.md
```

### Principais classes

**Banco**

Responsável pelo gerenciamento das contas bancárias e pelas informações do banco.

**Cliente**

Armazena as informações dos titulares das contas.

**ContaBancaria**

Responsável pelo saldo, operações bancárias e histórico de transações da conta.

**Transacao**

Representa uma operação realizada na conta, armazenando informações como tipo, valor e data/hora.

## 🔄 Funcionamento

O sistema utiliza objetos para representar os principais elementos de um banco:

```text
Banco
 ├── Contas
 │    ├── Cliente
 │    └── Transações
 │         ├── Depósito
 │         ├── Saque
 │         └── Transferência
```

As operações realizadas pela `ContaBancaria` alteram o saldo e registram uma nova `Transacao` no histórico da conta.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Git**
* **GitHub**

## 📚 Conceitos praticados

Durante o desenvolvimento estão sendo praticados conceitos como:

* Programação Orientada a Objetos;
* Classes e objetos;
* Encapsulamento;
* Abstração;
* Modularização;
* Métodos e atributos;
* Composição entre objetos;
* Listas e estruturas de dados;
* Validação de dados;
* Manipulação de data e hora;
* Controle de versão com Git.

## 🚧 Próximos passos

O projeto ainda está em desenvolvimento. Algumas funcionalidades que pretendo implementar ou aprimorar:

* [ ] Melhorar a interface do sistema;
* [ ] Melhorar a formatação do extrato;
* [ ] Adicionar tratamento de exceções;
* [ ] Implementar abertura de conta como uma transação registrada;
* [ ] Melhorar as validações;
* [ ] Criar testes automatizados;
* [ ] Adicionar persistência de dados;
* [ ] Avaliar a implementação de um banco de dados;
* [ ] Melhorar a documentação do projeto.

## 📈 Evolução do projeto

Este projeto também funciona como um registro da minha evolução nos estudos de programação.

A ideia é desenvolver novas funcionalidades gradualmente, utilizando o Git para registrar as principais etapas e mudanças realizadas durante o desenvolvimento.

## 👨‍💻 Autor

**Alisson Ferro**

Estudante de Análise e Desenvolvimento de Sistemas e Sistemas de Informação, atualmente desenvolvendo conhecimentos em programação, desenvolvimento de sistemas e backend.
