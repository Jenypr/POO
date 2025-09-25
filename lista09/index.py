import streamlit as st


class Cliente:
    def __init__(self, id_cliente: int, nome: str, telefone: str):
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__telefone = telefone

    def get_id_cliente(self):
        return self.__id_cliente

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def __str__(self):
        return f"Cliente {self.__id_cliente}: {self.__nome} - Tel: {self.__telefone}"


class ClienteDAO:
    __clientes = []

    @classmethod
    def inserir(cls, cliente: Cliente):
        cls.__clientes.append(cliente)

    @classmethod
    def listar(cls):
        return cls.__clientes

    @classmethod
    def remover(cls, id_cliente: int):
        for cliente in cls.__clientes:
            if cliente.get_id_cliente() == id_cliente:
                cls.__clientes.remove(cliente)
                return True
        return False


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


class ServicoDAO:
    __servicos = []

    @classmethod
    def inserir(cls, servico: Servico):
        cls.__servicos.append(servico)

    @classmethod
    def listar(cls):
        return cls.__servicos

    @classmethod
    def remover(cls, id_servico: int):
        for servico in cls.__servicos:
            if servico.get_id_servico() == id_servico:
                cls.__servicos.remove(servico)
                return True
        return False

st.set_page_config(page_title="Sistema de Agendamento", layout="centered")

st.title("Sistema de Agendamento")

menu = st.sidebar.radio("Menu", ["Início", "Clientes", "Serviços"])


if menu == "Clientes":
    st.header("Cadastro de Clientes")

    with st.form("form_cliente"):
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        nome = st.text_input("Nome")
        telefone = st.text_input("Telefone")
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            if nome.strip() == "" or telefone.strip() == "":
                st.warning("Preencha todos os campos!")
            else:
                cliente = Cliente(id_cliente, nome, telefone)
                ClienteDAO.inserir(cliente)
                st.success("Cliente cadastrado com sucesso!")

    st.subheader("Lista de Clientes")
    clientes = ClienteDAO.listar()
    if clientes:
        for c in clientes:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(str(c))
            with col2:
                if st.button("Excluir", key=f"del_cliente_{c.get_id_cliente()}"):
                    ClienteDAO.remover(c.get_id_cliente())
                    st.rerun()
    else:
        st.info("Nenhum cliente cadastrado.")

elif menu == "Serviços":
    st.header("Cadastro de Serviços")

    with st.form("form_servico"):
        id_servico = st.number_input("ID do Serviço", min_value=1, step=1)
        descricao = st.text_input("Descrição")
        preco = st.number_input("Preço", min_value=0.0, step=0.5, format="%.2f")
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            if descricao.strip() == "":
                st.warning("Preencha a descrição!")
            else:
                servico = Servico(id_servico, descricao, preco)
                ServicoDAO.inserir(servico)
                st.success("Serviço cadastrado com sucesso!")

    st.subheader("Lista de Serviços")
    servicos = ServicoDAO.listar()
    if servicos:
        for s in servicos:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(str(s))
            with col2:
                if st.button("Excluir", key=f"del_servico_{s.get_id_servico()}"):
                    ServicoDAO.remover(s.get_id_servico())
                    st.rerun()
    else:
        st.info("Nenhum serviço cadastrado.")

else:
    st.subheader("Bem-vindo ao sistema de agendamento!")
    st.write("Use o menu lateral para navegar entre **Clientes** e **Serviços**.")