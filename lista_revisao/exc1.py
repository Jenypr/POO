from datetime import datetime

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.id = id
        self.data = datetime.strptime(data, "%d/%m/%Y")
        self.distancia = float(distancia)
        self.tempo = tempo

    def ToString(self):
        return (f"ID: {self.id}\n"
                f"Data: {self.data.strftime('%d/%m/%Y')}\n"
                f"Distância: {self.distancia:.2f} km\n"
                f"Tempo: {self.tempo}")

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data.strftime("%d/%m/%Y")

    def get_distancia(self):
        return self.distancia

    def get_tempo(self):
        return self.tempo

    def set_id(self, id):
        self.id = id

    def set_data(self, data):
        self.data = datetime.strptime(data, "%d/%m/%Y")

    def set_distancia(self, distancia):
        self.distancia = float(distancia)

    def set_tempo(self, tempo):
        self.tempo = tempo

def main():
    print("Cadastro de Treino")
    id = input("ID do treino: ")
    data = input("Data do treino (dd/mm/aaaa): ")
    distancia = input("Distância percorrida (em km): ")
    tempo = input("Tempo da corrida (ex: 00:45:00): ")

    treino = Treino(id, data, distancia, tempo)

    print("\nDados do treino cadastrados:")
    print(treino.ToString())

    alterar = input("\nDeseja alterar o tempo da corrida? (s/n): ")
    if alterar.lower() == 's':
        novo_tempo = input("Novo tempo (ex: 00:40:00): ")
        treino.set_tempo(novo_tempo)
        print("\nDados atualizados:")
        print(treino.ToString())

class TreinoUI:
    def __init__(self):
        self.lista = []

    def menu(self):
        while True:
            print("\n MENU")
            print("1. inserir novo treino")
            print("2. listar todos os treinos")
            print("3. listar treinos por id")
            print("4.")
            print("\n MENU")
            print("\n MENU")
            print("\n MENU")
            print("\n MENU")
        
if __name__ == "__main__":
    main()

