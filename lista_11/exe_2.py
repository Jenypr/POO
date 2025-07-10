class Contato:
    __proximo_id = 1
    
    def __init__(self, n, e, f):
        self.__id = Contato.__proximo_id
        Contato.__proximo_id += 1
        self.__nome = n
        self.__email = e
        self.__fone = f

    def get_id(self):
        return self.__id    

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
        
class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()

    @classmethod
    def menu(cls):
        print("\n1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def email_existe(cls, email):
        for contato in cls.__contatos:
            if contato.get_email() == email:
                return True
        return False

    @classmethod
    def inserir(cls):
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        if cls.email_existe(email):
            print("Erro: já existe um contato com esse e-mail.")
            return
        fone = input("Informe o fone: ")
        c = Contato(nome, email, fone)
        cls.__contatos.append(c)
        print("Contato inserido com sucesso.")

    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0:
            print("Nenhum contato cadastrado")
        for c in cls.__contatos:
            print(c)

    @classmethod
    def listar_id(cls, id):
        for c in cls.__contatos:
            if c.get_id() == id: return c
        return None    

    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser atualizado: "))
        c = cls.listar_id(id)
        if c == None:
            print("Esse contato não existe")
        else:
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            if email != c.get_email() and cls.email_existe(email):
                print("Erro: já existe um contato com esse e-mail.")
                return
            fone = input("Informe o novo fone: ")
            cls.__contatos.remove(c)
            novo = Contato(nome, email, fone)
            novo._Contato__id = id  # Manter o mesmo ID
            cls.__contatos.append(novo)
            print("Contato atualizado com sucesso.")

    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        c = cls.listar_id(id)
        if c == None: 
            print("Esse contato não existe")
        else:
            cls.__contatos.remove(c)
            print("Contato excluído.")

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        encontrados = False
        for c in cls.__contatos:
            if c.get_nome().lower().startswith(nome.lower()):
                print(c)
                encontrados = True
        if not encontrados:
            print("Nenhum contato encontrado com esse nome.")

ContatoUI.main()