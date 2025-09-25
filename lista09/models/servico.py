
class Servico:
    def __init__(self, id_servico: int, descricao: str, preco: float):
        self.__id_servico = id_servico
        self.__descricao = descricao
        self.__preco = preco

    def get_id_servico(self):
        return self.__id_servico

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def __str__(self):
        return f"Serviço {self.__id_servico}: {self.__descricao} - R$ {self.__preco:.2f}"