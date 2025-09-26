class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

    def saudacao(self):
        return "Olá, usuário"


class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)  # chama o construtor de Usuario
        self.saldo = saldo

    # Sobrescrevendo o método saudacao

    def saudacao(self):
        return "Olá, cliente"


# Instanciando um Cliente
cliente1 = Cliente("Maria", "maria@email.com", 500)

# Acessando atributos
print(cliente1.nome)
print(cliente1.email)
print(cliente1.saldo)

# Chamando método herdado
cliente1.exibir_informacoes()

# Chamando método sobrescrito
print(cliente1.saudacao())

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo


class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, departamento):
        super().__init__(nome, email, cargo)
        self.departamento = departamento


# Instanciando um gerente
gerente1 = Gerente("João", "joao@email.com", "Gerente", "Vendas")

# Acessando atributos
print("\n--- Dados do gerente ---")
print("Nome:", gerente1.nome)
print("Email:", gerente1.email)
print("Cargo:", gerente1.cargo)
print("Departamento:", gerente1.departamento)

class Autenticacao:
    def login(self):
        print("Usuário logado.")

    def status(self):
        return "Status de Autenticacao"


class Permissao:
    def verificar_permissao(self):
        print("Permissão verificada.")

    def status(self):
        return "Status de Permissao"


class Administrador(Autenticacao, Permissao):
    pass


# Usando os métodos herdados
adm = Administrador()
adm.login()
adm.verificar_permissao()

# Qual versão de status() será chamada?
print("\nStatus chamado:", adm.status())

# Ordem de resolução de métodos (MRO)
print("\nOrdem de herança (MRO):")
print(Administrador.__mro__)
