class Pais:
    def __init__(self, i: int, n: str, p: int, a: float):
        self.__id = i
        self.__nome = n
        self.__populacao = p
        self.__area = a

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_populacao(self):
        return self.__populacao
    
    def get_area(self):
        return self.__area
    
    def set_nome(self, n: str):
        self.__nome = n

    def set_populacao(self, p: int):
        self.__populacao = p

    def set_area(self, a: float):
        self.__area = a

    def densidade(self) -> float:
        return self.__populacao / self.__area if self.__area != 0 else 0

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome} - População: {self.__populacao} - Área: {self.__area} km² - Densidade: {self.densidade():.2f} hab/km²"


class PaisUI:
    __paises = []

    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = cls.menu()
            if op == 1:
                cls.inserir()
            elif op == 2:
                cls.listar()
            elif op == 3:
                cls.atualizar()
            elif op == 4:
                cls.excluir()
            elif op == 5:
                cls.mais_populoso()
            elif op == 6:
                cls.mais_povoado()

    @classmethod
    def menu(cls) -> int:
        print("\n--- CADASTRO DE PAÍSES ---")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - País mais populoso")
        print("6 - País mais povoado (densidade)")
        print("7 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @classmethod
    def inserir(cls):
        try:
            i = int(input("ID: "))
            if any(p.get_id() == i for p in cls.__paises):
                print("Erro: ID já cadastrado.")
                return
            n = input("Nome: ")
            p = int(input("População: "))
            a = float(input("Área (em km²): "))
            pais = Pais(i, n, p, a)
            cls.__paises.append(pais)
            print("País inserido com sucesso!")
        except ValueError:
            print("Dados inválidos.")

    @classmethod
    def listar(cls):
        if not cls.__paises:
            print("Nenhum país cadastrado.")
        else:
            print("\n--- Lista de Países ---")
            for p in cls.__paises:
                print(p)

    @classmethod
    def atualizar(cls):
        try:
            id_pais = int(input("Informe o ID do país a atualizar: "))
            for p in cls.__paises:
                if p.get_id() == id_pais:
                    n = input("Novo nome: ")
                    pop = int(input("Nova população: "))
                    area = float(input("Nova área (km²): "))
                    p.set_nome(n)
                    p.set_populacao(pop)
                    p.set_area(area)
                    print("País atualizado com sucesso.")
                    return
            print("País não encontrado.")
        except ValueError:
            print("Erro nos dados inseridos.")

    @classmethod
    def excluir(cls):
        try:
            id_pais = int(input("Informe o ID do país a excluir: "))
            for i, p in enumerate(cls.__paises):
                if p.get_id() == id_pais:
                    del cls.__paises[i]
                    print("País removido com sucesso.")
                    return
            print("País não encontrado.")
        except ValueError:
            print("ID inválido.")

    @classmethod
    def mais_populoso(cls):
        if not cls.__paises:
            print("Nenhum país cadastrado.")
        else:
            mais = max(cls.__paises, key=lambda p: p.get_populacao())
            print("\nPaís mais populoso:")
            print(mais)

    @classmethod
    def mais_povoado(cls):
        if not cls.__paises:
            print("Nenhum país cadastrado.")
        else:
            povoado = max(cls.__paises, key=lambda p: p.densidade())
            print("\nPaís mais povoado (maior densidade demográfica):")
            print(povoado)


# Para executar o programa:
if __name__ == "__main__":
    PaisUI.main()
