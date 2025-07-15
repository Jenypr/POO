from datetime import datetime

class Contato:
    def __init__(self, i, n, e, f, d):
        self.id = i
        self.nome = n
        self.email = e
        self.fone = f
        self.nascimento = d

    def ToString(self):
        return (f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"E-mail: {self.email}\n"
                f"Telefone: {self.fone}\n"
                f"Nascimento: {self.nascimento.strftime('%d/%m/%Y')}")

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_email(self): return self.email
    def get_fone(self): return self.fone
    def get_nascimento(self): return self.nascimento

    def set_nome(self, nome): self.nome = nome
    def set_email(self, email): self.email = email
    def set_fone(self, fone): self.fone = fone
    def set_nascimento(self, nascimento): self.nascimento = nascimento


class ContatoUI:
    contatos = []

    @staticmethod
    def Main():
        while True:
            opcao = ContatoUI.Menu()
            if opcao == 1:
                ContatoUI.Inserir()
            elif opcao == 2:
                ContatoUI.Listar()
            elif opcao == 3:
                ContatoUI.Atualizar()
            elif opcao == 4:
                ContatoUI.Excluir()
            elif opcao == 5:
                ContatoUI.Pesquisar()
            elif opcao == 6:
                ContatoUI.Aniversariantes()
            elif opcao == 7:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def Menu() -> int:
        print("\n==== AGENDA DE CONTATOS ====")
        print("1 - Inserir Contato")
        print("2 - Listar Contatos")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Pesquisar Contato")
        print("6 - Ver Aniversariantes")
        print("7 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except:
            return 0

    @staticmethod
    def Inserir():
        try:
            i = int(input("ID: "))
            n = input("Nome: ")
            e = input("E-mail: ")
            f = input("Telefone: ")
            d = datetime.strptime(input("Data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
            novo = Contato(i, n, e, f, d)
            ContatoUI.contatos.append(novo)
            print("Contato inserido com sucesso.")
        except:
            print("Erro ao inserir contato. Verifique os dados.")

    @staticmethod
    def Listar():
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
            return
        for c in ContatoUI.contatos:
            print("\n" + c.ToString())

    @staticmethod
    def Atualizar():
        try:
            i = int(input("Informe o ID do contato para atualizar: "))
            for c in ContatoUI.contatos:
                if c.get_id() == i:
                    print("Deixe em branco se não quiser alterar.")
                    nome = input(f"Novo nome ({c.get_nome()}): ")
                    email = input(f"Novo email ({c.get_email()}): ")
                    fone = input(f"Novo telefone ({c.get_fone()}): ")
                    nasc = input(f"Nova data de nascimento ({c.get_nascimento().strftime('%d/%m/%Y')}): ")

                    if nome: c.set_nome(nome)
                    if email: c.set_email(email)
                    if fone: c.set_fone(fone)
                    if nasc: c.set_nascimento(datetime.strptime(nasc, "%d/%m/%Y"))

                    print("Contato atualizado.")
                    return
            print("Contato não encontrado.")
        except:
            print("Erro na atualização.")

    @staticmethod
    def Excluir():
        try:
            i = int(input("Informe o ID do contato para excluir: "))
            for c in ContatoUI.contatos:
                if c.get_id() == i:
                    ContatoUI.contatos.remove(c)
                    print("Contato excluído.")
                    return
            print("Contato não encontrado.")
        except:
            print("Erro ao excluir contato.")

    @staticmethod
    def Pesquisar():
        termo = input("Digite o início do nome a pesquisar: ").lower()
        encontrados = [c for c in ContatoUI.contatos if c.get_nome().lower().startswith(termo)]
        if encontrados:
            for c in encontrados:
                print("\n" + c.ToString())
        else:
            print("Nenhum contato encontrado.")

    @staticmethod
    def Aniversariantes():
        try:
            mes = int(input("Informe o número do mês (1 a 12): "))
            aniversariantes = [c for c in ContatoUI.contatos if c.get_nascimento().month == mes]
            if aniversariantes:
                for c in aniversariantes:
                    print("\n" + c.ToString())
            else:
                print("Nenhum aniversariante neste mês.")
        except:
            print("Mês inválido.")


if __name__ == "__main__":
    ContatoUI.Main()
