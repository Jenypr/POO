from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
   
    def Idade(self):
        hoje = datetime.today()
        anos = hoje.year - self.nascimento.year
        meses = hoje.month - self.nascimento.month


        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"
   
    def ToString(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Telefone: {self.telefone}\n"
                f"Nascimento: {self.nascimento.strftime('%d/%m/%Y')}\n"
                f"Idade: {self.Idade()}")
   
    def get_nome(self):
        return self.nome
   
    def get_cpf(self):
        return self.cpf
   
    def get_telefone(self):
        return self.telefone
   
    def get_nascimento(self):
        return self.nascimento.strftime('%d/%m/%Y')
   
    def set_nome(self, nome):
        self.nome = nome
   
    def set_cpf(self, cpf):
        self.cpf = cpf
   
    def set_telefone(self, telefone):
        self.telefone = telefone
   
    def set_nascimento(self, nascimento):
        self.nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

def main():
    print("Cadastro de Paciente")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")


    paciente = Paciente(nome, cpf, telefone, nascimento)
    print("\nDados do paciente cadastrados:")
    print(paciente.ToString())
   
    alterar = input("\nDeseja alterar o telefone? (s/n): ")
    if alterar.lower() == 's':
        novo_telefone = input("Novo telefone: ")
        paciente.set_telefone(novo_telefone)
        print("\nDados atualizados:")
        print(paciente.ToString())


if __name__ == "__main__":
    main()