import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o id")
        email = st.text_input("Informe a descrição")
        fone = st.text_input("Informe o valor")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de Serviços", clientes)
            email = st.text_input("Informe o novo id", op.get_nome())
            nome = st.text_input("Informe a nova descrição", op.get_email())
            fone = st.text_input("Informe o novo valor", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                View.cliente_atualizar(id, nome, email, fone)
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviços", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                View.cliente_excluir(id)
                st.success("Serviço excluído com sucesso")
                time.sleep(2)
                st.rerun()