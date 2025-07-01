class Contato:
    def __init__(self, i: int, n: str, e: str, f: str):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_email(self, email: str):
        self.__email = email

    def set_fone(self, fone: str):
        self.__fone = fone

    def ToString(self) -> str:
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    def __str__(self):
        return self.ToString()


class ContatoUI:
    __contatos = []

    @classmethod
    def Main(cls):
        while True:
            op = cls.Menu()
            if op == 1:
                cls.Inserir()
            elif op == 2:
                cls.Listar()
            elif op == 3:
                cls.Atualizar()
            elif op == 4:
                cls.Excluir()
            elif op == 5:
                cls.Pesquisar()
            elif op == 6:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

    @classmethod
    def Menu(cls) -> int:
        print("\n--- MENU CONTATOS ---")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Pesquisar")
        print("6 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @classmethod
    def Inserir(cls):
        try:
            i = int(input("ID: "))
            n = input("Nome: ")
            e = input("E-mail: ")
            f = input("Fone: ")
            novo = Contato(i, n, e, f)
            cls.__contatos.append(novo)
            print("Contato inserido com sucesso.")
        except ValueError:
            print("Erro ao inserir contato. Verifique os dados.")

    @classmethod
    def Listar(cls):
        if not cls.__contatos:
            print("Nenhum contato cadastrado.")
        else:
            print("\n--- Lista de Contatos ---")
            for c in cls.__contatos:
                print(c)

    @classmethod
    def Atualizar(cls):
        try:
            id_alvo = int(input("Informe o ID do contato a atualizar: "))
            for c in cls.__contatos:
                if c.get_id() == id_alvo:
                    novo_nome = input("Novo nome: ")
                    novo_email = input("Novo e-mail: ")
                    novo_fone = input("Novo fone: ")
                    c.set_nome(novo_nome)
                    c.set_email(novo_email)
                    c.set_fone(novo_fone)
                    print("Contato atualizado com sucesso.")
                    return
            print("Contato não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")

    @classmethod
    def Excluir(cls):
        try:
            id_alvo = int(input("Informe o ID do contato a excluir: "))
            for i, c in enumerate(cls.__contatos):
                if c.get_id() == id_alvo:
                    del cls.__contatos[i]
                    print("Contato excluído com sucesso.")
                    return
            print("Contato não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")

    @classmethod
    def Pesquisar(cls):
        nome = input("Informe o nome para busca: ").lower()
        encontrados = [c for c in cls.__contatos if c.get_nome().lower().startswith(nome)]
        if encontrados:
            print("\n--- Contatos encontrados ---")
            for c in encontrados:
                print(c)
        else:
            print("Nenhum contato encontrado com esse nome.")


# Execução principal
if __name__ == "__main__":
    ContatoUI.Main()
