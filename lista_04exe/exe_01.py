import random

class Bingo:
    def __init__(self, numBolas: int):
        self.numBolas = numBolas
        self.bolas = []
        self.__todas_bolas = list(range(1, numBolas + 1))
    def Sortear(self) -> int:
        if len(self.bolas) >= self.numBolas:
            return -1
        bola = random.choice([b for b in self.__todas_bolas if b not in self.bolas])
        self.bolas.append(bola)
        return bola

    def Sorteados(self) -> list[int]:
        return self.bolas
class BingoUI:
    @staticmethod
    def Main():
        bingo = None
        while True:
            opcao = BingoUI.Menu()
            if opcao == 1:
                bingo = BingoUI.IniciarJogo()
            elif opcao == 2:
                if bingo:
                    BingoUI.Sortear(bingo)
                else:
                    print("Primeiro inicie um jogo.")
            elif opcao == 3:
                if bingo:
                    BingoUI.Sorteados(bingo)
                else:
                    print("Primeiro inicie um jogo.")
            elif opcao == 4:
                print("Saindo do jogo. Até logo!")
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def Menu() -> int:
        print("\n====== MENU DO BINGO ======")
        print("1 - Iniciar novo jogo")
        print("2 - Sortear número")
        print("3 - Ver números sorteados")
        print("4 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @staticmethod
    def IniciarJogo() -> Bingo:
        try:
            num = int(input("Informe a quantidade de bolas: "))
            if num <= 0:
                print("Número deve ser maior que zero.")
                return None
            print(f"Novo jogo iniciado com {num} bolas!")
            return Bingo(num)
        except ValueError:
            print("Entrada inválida.")
            return None

    @staticmethod
    def Sortear(b: Bingo):
        resultado = b.Sortear()
        if resultado == -1:
            print("Todas as bolas já foram sorteadas!")
        else:
            print(f"Bola sorteada: {resultado}")

    @staticmethod
    def Sorteados(b: Bingo):
        bolas = b.Sorteados()
        if not bolas:
            print("Nenhuma bola foi sorteada ainda.")
        else:
            print(f"Bolas sorteadas até agora: {sorted(bolas)}")
if __name__ == "__main__":
    BingoUI.Main()
