# ContaBancaria
class ContaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo  # atributo privado

    # Getter
    def get_saldo(self):
        return self.__saldo

    # Setter (regra: saldo não pode ser negativo)
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Erro: o saldo não pode ser negativo.")


# Pessoa
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf          # privado
        self.__identidade = identidade  # privado

    # Getter e Setter
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    # Getter e Setter para Identidade
    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade


# Exemplo
conta = ContaBancaria(100)
print("Saldo inicial:", conta.get_saldo())
conta.set_saldo(200)
print("Saldo atualizado:", conta.get_saldo())
conta.set_saldo(-50)  # vai dar erro

pessoa = Pessoa("Julia", "10/05/1990", "173.456.679-00", "RG18345")
print("\nNome:", pessoa.nome)
print("CPF:", pessoa.get_cpf())
print("Identidade:", pessoa.get_identidade())

pessoa.set_cpf("987.654.321-00")
print("CPF atualizado:", pessoa.get_cpf())
