from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.codBarras = cod
        self.dateEmissao = emissao
        self.dataVencimento = venc
        self.dataPago = None
        self.valorBoleto (valor)
        self.valorPago = 0.0
        self.situacaoPagamento = Pagamento.EmAberto

    def Pagar(self, valorPago):
        if valorPago <= 0:
            print("Valor inválido.")
            return

        if self.valorPago + valorPago > self.valorBoleto:
            print("O valor excede o valor do boleto.")
            return

        self.valorPago += valorPago
        self.dataPago = datetime.today()

        if self.valorPago == 0:
            self.situacaoPagamento = Pagamento.EmAberto
        elif self.valorPago < self.valorBoleto:
            self.situacaoPagamento = Pagamento.PagoParcial
        else:
            self.situacaoPagamento = Pagamento.Pago

        print(f"Pagamento de R${valorPago:.2f} realizado.")

    def Situacao(self) -> Pagamento:
        return self.situacaoPagamento

    def ToString(self):
        data_pago_str = self.dataPago.strftime("%d/%m/%Y %H:%M") if self.dataPago else "Não pago"
        return (f"Código de Barras: {self.codBarras}\n"
                f"Data de Emissão: {self.dateEmissao.strftime('%d/%m/%Y')}\n"
                f"Data de Vencimento: {self.dataVencimento.strftime('%d/%m/%Y')}\n"
                f"Data do Pagamento: {data_pago_str}\n"
                f"Valor do Boleto: R${self.valorBoleto:.2f}\n"
                f"Valor Pago: R${self.valorPago:.2f}\n"
                f"Situação: {self.situacaoPagamento.name}")

def main():
    print("=== Cadastro de Boleto ===")
    cod = input("Código de Barras: ")
    emissao_str = input("Data de Emissão (dd/mm/aaaa): ")
    venc_str = input("Data de Vencimento (dd/mm/aaaa): ")
    valor = float(input("Valor do Boleto: R$"))

    emissao = datetime.strptime(emissao_str, "%d/%m/%Y")
    venc = datetime.strptime(venc_str, "%d/%m/%Y")

    boleto = Boleto(cod, emissao, venc, valor)

    while True:
        print("\n--- MENU ---")
        print("1 - Ver Boleto")
        print("2 - Fazer Pagamento")
        print("3 - Ver Situação")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n" + boleto.ToString())
        elif opcao == "2":
            valor_pagamento = float(input("Valor a pagar: R$"))
            boleto.Pagar(valor_pagamento)
        elif opcao == "3":
            print("Situação atual:", boleto.Situacao().name)
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()